import os
import json
import hashlib
import re
from pypdf import PdfReader

CERT_DIR = r"c:\Users\Karunesh P\OneDrive\Desktop\karu\certificates"
OUTPUT_JSON = r"c:\Users\Karunesh P\OneDrive\Desktop\karu\curated_certificates.json"

def get_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return "0x" + h.hexdigest().upper()

def extract_pdf_full(filepath):
    try:
        reader = PdfReader(filepath)
        text = ""
        for page in reader.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
        return text.strip()
    except Exception:
        return ""

files = [f for f in os.listdir(CERT_DIR) if not f.startswith("._") and f != "__MACOSX"]
curated = []

for filename in sorted(files):
    filepath = os.path.join(CERT_DIR, filename)
    file_size = os.path.getsize(filepath)
    ext = os.path.splitext(filename)[1].lower()
    sha256 = get_sha256(filepath)
    raw_text = ""
    if ext == ".pdf":
        raw_text = extract_pdf_full(filepath)
    
    curated.append({
        "filename": filename,
        "extension": ext,
        "size_bytes": file_size,
        "sha256": sha256,
        "raw_text": raw_text
    })

with open(r"c:\Users\Karunesh P\OneDrive\Desktop\karu\raw_certs.json", "w", encoding="utf-8") as f:
    json.dump(curated, f, indent=2, ensure_ascii=False)

print("Saved raw_certs.json")
