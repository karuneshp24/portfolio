import subprocess
import time
import sys
import re

print("Starting Auto-Reconnect Tunnel Keeper...")

cmd = [
    "ssh",
    "-R", "80:localhost:8080",
    "-o", "StrictHostKeyChecking=no",
    "-o", "ServerAliveInterval=15",
    "-o", "ServerAliveCountMax=3",
    "-o", "ExitOnForwardFailure=yes",
    "nokey@localhost.run"
]

while True:
    try:
        print("[TunnelKeeper] Connecting to localhost.run...")
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        for line in process.stdout:
            sys.stdout.write(line)
            sys.stdout.flush()
            if "tunneled with tls termination" in line:
                match = re.search(r"https://[a-zA-Z0-9\.\-]+", line)
                if match:
                    url = match.group(0)
                    with open(r"c:\Users\Karunesh P\OneDrive\Desktop\karu\live_url.txt", "w", encoding="utf-8") as f:
                        f.write(url)
                    print(f"\n>>> ACTIVE PUBLIC URL: {url} <<<\n", flush=True)

        process.wait()
        print(f"[TunnelKeeper] Process exited with code {process.returncode}. Reconnecting in 3 seconds...")
        time.sleep(3)
    except Exception as e:
        print(f"[TunnelKeeper] Error: {e}. Retrying in 5 seconds...")
        time.sleep(5)
