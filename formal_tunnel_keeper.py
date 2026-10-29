import subprocess
import time
import sys
import re

PORT = 8080
SUBDOMAIN = "karunesh-portfolio"
URL_FILE = r"c:\Users\Karunesh P\OneDrive\Desktop\karu\formal_live_url.txt"

print(f"Starting Formal Tunnel Keeper for port {PORT} with subdomain '{SUBDOMAIN}'...")

while True:
    try:
        cmd = f"npx --yes localtunnel --port {PORT} --subdomain {SUBDOMAIN}"
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        assigned_url = None
        for line in iter(process.stdout.readline, ''):
            clean_line = line.strip()
            print(clean_line)
            match = re.search(r'(https://[a-zA-Z0-9\-\.]+\.loca\.lt)', clean_line)
            if match:
                assigned_url = match.group(1)
                print(f"\n>>> ACTIVE FORMAL URL: {assigned_url} <<<\n")
                with open(URL_FILE, "w", encoding="utf-8") as f:
                    f.write(assigned_url)
        
        process.wait()
        print("Tunnel process disconnected. Reconnecting in 3 seconds...")
        time.sleep(3)
    except Exception as e:
        print(f"Error: {e}. Retrying in 5 seconds...")
        time.sleep(5)
