import urllib.request
import os
import sys

if not os.path.exists('raw-denoise.html'):
    print("Error: 'raw-denoise.html' not found. Make sure it's in the same folder.")
    sys.exit(1)

CDN_BASE = "https://cdn.jsdelivr.net/npm/libraw-wasm@1.1.2/dist/"
FILES_TO_FETCH = ["libraw.js", "worker.js", "libraw.wasm", "index.js"]

print("📥 Downloading WebAssembly dependencies...")
for file in FILES_TO_FETCH:
    print(f"  -> Fetching {file}...")
    urllib.request.urlretrieve(CDN_BASE + file, file)

print("\n🔧 Patching HTML...")
with open("raw-denoise.html", "r", encoding="utf-8") as f:
    html = f.read()

# Swap the CDN URL for the local index.js file we just downloaded
html = html.replace(
    "const LIBRAW_CDN = 'https://cdn.jsdelivr.net/npm/libraw-wasm@1.1.2/dist/index.js';",
    "const LIBRAW_CDN = './index.js';"
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("\n✅ Done! Your standalone deployment is ready.")
print("Upload the following 5 files to your GitHub repository:")
print("  1. index.html")
print("  2. index.js")
print("  3. libraw.js")
print("  4. worker.js")
print("  5. libraw.wasm")
