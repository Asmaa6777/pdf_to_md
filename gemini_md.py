import os
import io
import re
import sys
import time
import hashlib
from concurrent.futures import ThreadPoolExecutor

import pdfplumber

DEFAULT_MODEL = "gemini-2.5-flash"
CACHE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".slide_cache")

SYSTEM_PROMPT = """You convert a single lecture/presentation slide image into clean Markdown.

Rules:
- Start with the slide title as a level-2 heading (## Title). If there is no visible title, invent a short descriptive one.
- Reproduce all text faithfully. Keep bullet hierarchy using nested "-" lists (2-space indent per level).
- Real tabular data -> Markdown table. Do NOT turn layout boxes into tables.
- Code or pseudo-code -> fenced code block with the right language tag.
- Math -> LaTeX ($...$ inline, $$...$$ block).
- For EVERY picture, diagram, chart, or screenshot, add a block quote right after the related text:
  > **Figure:** <what it shows>
  Explain the meaning, not just the appearance: for UML/flowcharts/state machines describe the
  elements and their relationships (classes, attributes, associations, multiplicities, transitions);
  for charts describe axes, trends and key values; for photos describe what is relevant to the lecture.
- Ignore slide numbers, footers, logos, decorative shapes and watermarks.
- If the slide is blank or only a section divider, output just the heading.
- Output ONLY the Markdown for this slide, with no preamble and no surrounding code fence."""


def parse_pages(spec, total):
    """Turn '1-3,7' into sorted 0-based page indexes."""
    if not spec:
        return list(range(total))
    pages = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            pages.update(range(int(a), int(b) + 1))
        elif part:
            pages.add(int(part))
    return sorted(p - 1 for p in pages if 1 <= p <= total)


def render_pages(pdf_source, pages_spec=None, resolution=150):
    """Return [(slide_number, png_bytes), ...]."""
    images = []
    with pdfplumber.open(pdf_source) as pdf:
        for idx in parse_pages(pages_spec, len(pdf.pages)):
            buf = io.BytesIO()
            pdf.pages[idx].to_image(resolution=resolution).original.save(buf, format="PNG")
            images.append((idx + 1, buf.getvalue()))
    return images


def _strip_fence(text):
    text = text.strip()
    m = re.match(r"^```(?:markdown|md)?\s*\n(.*)\n```$", text, re.DOTALL)
    return m.group(1).strip() if m else text


def _get_client():
    try:
        from dotenv import load_dotenv
        load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))
    except ImportError:
        pass
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not set.\n"
            "  Get a key at https://aistudio.google.com/apikey and either\n"
            "  set it as an environment variable or put GEMINI_API_KEY=... in a .env file here."
        )
    from google import genai
    return genai.Client(api_key=api_key)


def _convert_slide(client, model, png, lang, retries=5):
    from google.genai import types, errors

    prompt = "Convert this slide to Markdown."
    if lang:
        prompt += f" Write the figure explanations in {lang}; keep the slide text in its original language."

    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model=model,
                contents=[types.Part.from_bytes(data=png, mime_type="image/png"), prompt],
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    temperature=0.2,
                ),
            )
            if not response.text:
                raise ValueError("empty response (possibly blocked)")
            return _strip_fence(response.text)
        except errors.APIError as e:
            retryable = e.code == 429 or (e.code or 0) >= 500
            if not retryable or attempt == retries - 1:
                raise
        except ValueError:
            if attempt == retries - 1:
                raise
        time.sleep(2 ** attempt * 2)


def _cache_path(png, model, lang):
    key = hashlib.sha256(png + model.encode() + (lang or "").encode() + SYSTEM_PROMPT.encode()).hexdigest()
    return os.path.join(CACHE_DIR, key[:32] + ".md")


def gemini_to_markdown(pdf_source, title=None, model=DEFAULT_MODEL, pages=None,
                       lang=None, workers=4, use_cache=True):
    """Convert a PDF (path or BytesIO) to Markdown, one Gemini request per slide."""
    client = _get_client()
    slides = render_pages(pdf_source, pages)
    if not slides:
        return ""
    os.makedirs(CACHE_DIR, exist_ok=True)

    done = 0

    def work(item):
        nonlocal done
        number, png = item
        cache = _cache_path(png, model, lang)
        if use_cache and os.path.exists(cache):
            with open(cache, encoding="utf-8") as f:
                md = f.read()
        else:
            try:
                md = _convert_slide(client, model, png, lang)
            except Exception as e:
                print(f"\n  Slide {number} failed: {e}", file=sys.stderr)
                return number, f"## Slide {number}\n\n> ⚠️ Conversion failed: {e}"
            with open(cache, "w", encoding="utf-8") as f:
                f.write(md)
        done += 1
        print(f"  Slides: {done}/{len(slides)}", end="\r", file=sys.stderr)
        return number, md

    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        results = list(pool.map(work, slides))
    print(file=sys.stderr)

    parts = [f"# {title}\n"] if title else []
    for number, md in results:
        parts.append(f"<!-- Slide {number} -->\n{md}\n")
    return "\n---\n\n".join(parts)
