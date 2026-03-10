from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"

if __name__ == "__main__":
    os.chdir(SITE)
    server = ThreadingHTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
    print("Serving site at http://0.0.0.0:8000")
    server.serve_forever()
