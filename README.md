# PDF to Markdown Tools

Two tools that convert PDF files to Markdown — one runs locally (Python), one uses the Claude AI API (React).

---

## 1. Local Converter — `pdf_to_md.py`

No API key needed. Uses `pdfplumber` to extract text and tables directly from the PDF.

### Install dependency

```bash
pip install -r requirements.txt
```

### Commands

```bash
# Basic — converts file.pdf and saves file.md in the same folder
python3 pdf_to_md.py file.pdf

# Custom output path
python3 pdf_to_md.py file.pdf -o /path/to/output.md

# Convert multiple files at once
python3 pdf_to_md.py file1.pdf file2.pdf file3.pdf

# Print result to terminal instead of saving
python3 pdf_to_md.py file.pdf --stdout
```

### Where to put your files

Drop your PDF anywhere and pass its path to the script.
The easiest option is to put it in this folder:

```
/workspaces/Tools/
├── pdf_to_md.py
├── your-file.pdf     ← here
```

Then run:

```bash
python3 /workspaces/Tools/pdf_to_md.py /workspaces/Tools/your-file.pdf
```

The output `your-file.md` is saved next to the PDF automatically.

---

## 2. AI Converter — `ConvertToMd.JSX`

A React component that sends the PDF to Claude (claude-sonnet-4-6) and gets back clean Markdown. Handles formatting, tables, headings, and bold/italic better than the local tool.

### Requires

- React 18+
- An Anthropic API key → [console.anthropic.com](https://console.anthropic.com)

### Usage

1. Drop `ConvertToMd.JSX` into your React project
2. Import it where needed:
   ```jsx
   import PdfToMd from "./ConvertToMd";

   export default function App() {
     return <PdfToMd />;
   }
   ```
3. Enter your API key in the key field (saved to localStorage)
4. Drag a PDF onto the drop zone or click to browse
5. Copy or download the resulting `.md` file

---

## 3. Google Drive Integration (Python CLI only)

### One-time setup

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create a project → **Enable the Google Drive API**
3. Go to **APIs & Services → Credentials → Create Credentials → OAuth 2.0 Client ID**
4. Choose **Desktop app** → Download the JSON file
5. Rename it to `credentials.json` and place it in this folder

On the first Drive command, a browser window opens for you to log in and approve access. A `token.json` is saved automatically for future runs — **do not share or commit either file**.

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

**Where to find the file/folder ID:**
- Open the file or folder in Google Drive
- The ID is the long string in the URL after `/d/` or `/folders/`

---

## When to use which

| Situation | Use |
|---|---|
| No internet / no API key | `pdf_to_md.py` |
| Simple text-heavy PDFs | `pdf_to_md.py` |
| Complex layout, mixed content | `ConvertToMd.JSX` |
| Need best formatting quality | `ConvertToMd.JSX` |
