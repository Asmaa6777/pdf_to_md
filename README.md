# PDF to Markdown

Convert PDF slides to Markdown with `pdf_to_md.py`. Each slide is sent to Gemini as an image, so the output keeps the structure (headings, bullets, tables, code) and **explains every picture and diagram** in the slide. An offline `pdfplumber` engine is also available. Supports Google Drive as both a source and destination.

---

## Getting started

```bash
pip install -r requirements.txt
```

Get a Gemini API key at [aistudio.google.com/apikey](https://aistudio.google.com/apikey), then either set it as an environment variable or create a `.env` file in this folder:

```
GEMINI_API_KEY=your-key-here
```

`.env` is git-ignored — **never commit your key**.

---

## Gemini options

```bash
# Default: Gemini 2.5 Flash, all slides
python3 pdf_to_md.py lecture.pdf

# Use a stronger model for diagram-heavy slides
python3 pdf_to_md.py lecture.pdf --model gemini-2.5-pro

# Only some slides
python3 pdf_to_md.py lecture.pdf --pages 1-5,8

# Explain figures in another language (slide text stays as-is)
python3 pdf_to_md.py lecture.pdf --lang Arabic

# Parallel requests (lower this if you hit rate limits on the free tier)
python3 pdf_to_md.py lecture.pdf --workers 2

# Offline, text-only extraction (no images, no API key needed)
python3 pdf_to_md.py lecture.pdf --engine pdfplumber
```

Each slide's result is cached in `.slide_cache/`, so re-running after an error only calls Gemini for the slides that are missing. Use `--no-cache` to force a fresh conversion. Rate-limit (429) and server errors are retried automatically. If a slide still fails, a warning is written in its place and the rest of the deck continues.

---

## Basic usage

```bash
# Convert a PDF — saves file.md in the same folder
python3 pdf_to_md.py file.pdf

# Custom output path
python3 pdf_to_md.py file.pdf -o /path/to/output.md

# Convert multiple files at once
python3 pdf_to_md.py file1.pdf file2.pdf file3.pdf

# Print to terminal instead of saving
python3 pdf_to_md.py file.pdf --stdout
```

---

## Google Drive

### One-time setup

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create a project → **Enable the Google Drive API**
3. Go to **APIs & Services → Credentials → Create Credentials → OAuth 2.0 Client ID**
4. Choose **Desktop app** → Download the JSON file
5. Rename it to `credentials.json` and place it in this folder

On the first Drive command, a browser window opens for you to log in. A `token.json` is saved automatically for future runs — **do not share or commit either file**.

### Commands

```bash
# Convert a local PDF and upload the .md to your Drive root
python3 pdf_to_md.py report.pdf --to-drive

# Upload into a specific Drive folder (copy the folder ID from its URL)
python3 pdf_to_md.py report.pdf --to-drive --drive-folder FOLDER_ID

# Download a PDF from Drive, convert it, save .md locally
python3 pdf_to_md.py --from-drive FILE_ID
python3 pdf_to_md.py --from-drive "https://drive.google.com/file/d/FILE_ID/view"

# Download from Drive, convert, and upload the .md back to Drive
python3 pdf_to_md.py --from-drive FILE_ID --to-drive

# Download → convert → upload to a specific folder
python3 pdf_to_md.py --from-drive FILE_ID --to-drive --drive-folder FOLDER_ID

# Save the .md to a custom local path when downloading from Drive
python3 pdf_to_md.py --from-drive FILE_ID -o ~/Desktop/output.md
```

**Where to find the file/folder ID:** open the file or folder in Google Drive — the ID is the long string in the URL after `/d/` or `/folders/`.
