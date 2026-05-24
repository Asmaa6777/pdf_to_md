import os
import io
import re

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/drive"]
_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN_PATH = os.path.join(_DIR, "token.json")
CREDS_PATH = os.path.join(_DIR, "credentials.json")


def get_service():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDS_PATH):
                raise FileNotFoundError(
                    "credentials.json not found.\n"
                    "  1. Go to console.cloud.google.com\n"
                    "  2. Create a project → Enable Google Drive API\n"
                    "  3. Create OAuth 2.0 credentials (Desktop app)\n"
                    "  4. Download and save as credentials.json in this folder"
                )
            flow = InstalledAppFlow.from_client_secrets_file(CREDS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, "w") as f:
            f.write(creds.to_json())
    return build("drive", "v3", credentials=creds)


def parse_file_id(id_or_url: str) -> str:
    """Accept a Drive URL or a bare file ID."""
    m = re.search(r"/d/([a-zA-Z0-9_-]+)", id_or_url)
    if m:
        return m.group(1)
    m = re.search(r"[?&]id=([a-zA-Z0-9_-]+)", id_or_url)
    if m:
        return m.group(1)
    return id_or_url


def download_pdf(service, file_id: str) -> tuple[bytes, str]:
    """Return (pdf_bytes, original_filename)."""
    meta = service.files().get(fileId=file_id, fields="name").execute()
    filename = meta.get("name", "downloaded.pdf")
    request = service.files().get_media(fileId=file_id)
    buf = io.BytesIO()
    downloader = MediaIoBaseDownload(buf, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        if status:
            pct = int(status.progress() * 100)
            print(f"  Downloading... {pct}%", end="\r")
    print()
    return buf.getvalue(), filename


def upload_md(service, md_path: str, folder_id: str = None) -> str:
    """Upload .md file to Drive; return web view link."""
    name = os.path.basename(md_path)
    meta = {"name": name, "mimeType": "text/markdown"}
    if folder_id:
        meta["parents"] = [folder_id]
    media = MediaFileUpload(md_path, mimetype="text/markdown", resumable=False)
    result = service.files().create(
        body=meta, media_body=media, fields="id,webViewLink"
    ).execute()
    return result.get("webViewLink") or f"https://drive.google.com/file/d/{result['id']}/view"
