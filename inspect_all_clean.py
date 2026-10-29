import json

with open(r"c:\Users\Karunesh P\OneDrive\Desktop\karu\raw_certs.json", "r", encoding="utf-8") as f:
    certs = json.load(f)

lines = []
for i, c in enumerate(certs):
    fn = c["filename"]
    txt = " ".join(c["raw_text"].split())
    lines.append(f"[{i+1}] {fn} ==> {txt[:140]}")

with open(r"c:\Users\Karunesh P\OneDrive\Desktop\karu\cert_summary.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("Summary written to cert_summary.txt")
