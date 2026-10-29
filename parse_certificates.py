import os
import json
import hashlib
import re
from pypdf import PdfReader

CERT_DIR = r"c:\Users\Karunesh P\OneDrive\Desktop\karu\certificates"
OUTPUT_JSON = r"c:\Users\Karunesh P\OneDrive\Desktop\karu\certificates_metadata.json"

def get_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return "0x" + h.hexdigest().upper()

def extract_pdf_info(filepath):
    try:
        reader = PdfReader(filepath)
        text = ""
        for page in reader.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
        meta = reader.metadata or {}
        return text.strip(), meta
    except Exception as e:
        return "", {}

files = [f for f in os.listdir(CERT_DIR) if not f.startswith("._") and f != "__MACOSX"]
results = []

for filename in sorted(files):
    filepath = os.path.join(CERT_DIR, filename)
    file_size = os.path.getsize(filepath)
    ext = os.path.splitext(filename)[1].lower()
    sha256 = get_sha256(filepath)
    
    extracted_text = ""
    pdf_meta = {}
    if ext == ".pdf":
        extracted_text, pdf_meta = extract_pdf_info(filepath)
    
    clean_lines = [line.strip() for line in extracted_text.splitlines() if line.strip()]
    first_few_lines = clean_lines[:15]
    summary_text = " | ".join(first_few_lines)
    
    results.append({
        "filename": filename,
        "extension": ext,
        "size_bytes": file_size,
        "sha256": sha256,
        "extracted_snippet": summary_text[:500],
        "pdf_title": str(pdf_meta.get("/Title", "")),
        "pdf_author": str(pdf_meta.get("/Author", "")),
        "pdf_subject": str(pdf_meta.get("/Subject", ""))
    })

with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"Processed {len(results)} certificate files. Metadata saved to {OUTPUT_JSON}")
