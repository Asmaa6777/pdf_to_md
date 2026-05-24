import pdfplumber
import sys
import os
import re
import io
import argparse


def pdf_to_markdown(pdf_source):
    """Accept a file path (str) or a file-like object (BytesIO)."""
    md_lines = []

    with pdfplumber.open(pdf_source) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()

            for table in tables:
                if not table:
                    continue
                header = table[0]
                md_lines.append("| " + " | ".join(cell or "" for cell in header) + " |")
                md_lines.append("| " + " | ".join("---" for _ in header) + " |")
                for row in table[1:]:
                    md_lines.append("| " + " | ".join((cell or "").replace("\n", " ") for cell in row) + " |")
                md_lines.append("")

            text = page.extract_text()
            if not text:
                continue

            for line in text.split("\n"):
                line = line.strip()
                if not line:
                    md_lines.append("")
                    continue

                if line.isupper() and len(line) < 60:
                    md_lines.append(f"## {line.title()}")
                elif re.match(r"^\d+\.\s+\S", line):
                    md_lines.append(line)
                elif re.match(r"^[-•●▪]\s+", line):
                    md_lines.append(re.sub(r"^[-•●▪]\s+", "- ", line))
                else:
                    md_lines.append(line)

            md_lines.append("")

    return "\n".join(md_lines)


def convert_file(pdf_path, out_path=None, stdout=False):
    if not os.path.exists(pdf_path):
        print(f"Error: file not found: {pdf_path}", file=sys.stderr)
        return False

    print(f"Converting: {pdf_path}")
    markdown = pdf_to_markdown(pdf_path)

    if stdout:
        print(markdown)
        return True

    if out_path is None:
        out_path = os.path.splitext(pdf_path)[0] + ".md"

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"  Saved: {out_path}")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF files to Markdown using pdfplumber."
    )
    parser.add_argument("pdfs", nargs="*", metavar="FILE.pdf",
                        help="One or more local PDF files to convert")
    parser.add_argument("-o", "--output", metavar="OUT.md",
                        help="Output path (single file only)")
    parser.add_argument("--stdout", action="store_true",
                        help="Print Markdown to stdout instead of saving a file (single file only)")

    # Google Drive options
    drive_group = parser.add_argument_group("Google Drive")
    drive_group.add_argument("--from-drive", metavar="FILE_ID_OR_URL",
                             help="Download a PDF from Google Drive (file ID or share URL)")
    drive_group.add_argument("--to-drive", action="store_true",
                             help="Upload the converted .md file to Google Drive")
    drive_group.add_argument("--drive-folder", metavar="FOLDER_ID",
                             help="Google Drive folder ID to upload into (default: My Drive root)")

    args = parser.parse_args()

    if not args.pdfs and not args.from_drive:
        parser.error("Provide at least one FILE.pdf or use --from-drive")
    if len(args.pdfs) > 1 and args.output:
        parser.error("-o/--output cannot be used with multiple input files")
    if len(args.pdfs) > 1 and args.stdout:
        parser.error("--stdout cannot be used with multiple input files")
    if args.from_drive and args.pdfs:
        parser.error("--from-drive cannot be combined with local FILE.pdf arguments")

    # Lazy-load Drive only when needed
    service = None
    if args.from_drive or args.to_drive:
        try:
            import drive_utils
        except ImportError:
            print("Error: Google Drive packages not installed. Run:\n"
                  "  pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib",
                  file=sys.stderr)
            sys.exit(1)
        print("Authenticating with Google Drive…")
        service = drive_utils.get_service()

    ok = True

    if args.from_drive:
        file_id = drive_utils.parse_file_id(args.from_drive)
        print(f"Downloading from Drive: {file_id}")
        pdf_bytes, original_name = drive_utils.download_pdf(service, file_id)
        base_name = os.path.splitext(original_name)[0]

        print(f"Converting: {original_name}")
        markdown = pdf_to_markdown(io.BytesIO(pdf_bytes))

        if args.stdout:
            print(markdown)
        else:
            # Save locally first (needed for Drive upload too)
            out_path = args.output or (base_name + ".md")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(markdown)
            print(f"  Saved: {out_path}")

            if args.to_drive:
                url = drive_utils.upload_md(service, out_path, folder_id=args.drive_folder)
                print(f"  Uploaded to Drive: {url}")
    else:
        for pdf_path in args.pdfs:
            if not convert_file(pdf_path, out_path=args.output, stdout=args.stdout):
                ok = False
                continue
            if args.to_drive and not args.stdout:
                out_path = args.output or (os.path.splitext(pdf_path)[0] + ".md")
                url = drive_utils.upload_md(service, out_path, folder_id=args.drive_folder)
                print(f"  Uploaded to Drive: {url}")

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()