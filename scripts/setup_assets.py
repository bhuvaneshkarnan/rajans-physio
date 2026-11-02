import os
import re
import sys
import json
import urllib.request
from urllib.parse import urljoin, urlparse, unquote
from bs4 import BeautifulSoup

BASE_URL = 'https://dreamlab-website-e0f709d63d04003d95aaea.webflow.io'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

PAGES = [
    '/',
    '/about',
    '/blog',
    '/blog/10-things-nobody-told-you-about-being-a-web-designer',
    '/blog/10-web-design-blogs-you-cant-miss',
    '/blog/7-must-have-tools-for-web-designers',
    '/blog/7-of-the-best-examples-of-beautiful-blog-design',
    '/faq',
    '/free-assessment',
    '/medical-terms',
    '/membership-terms',
    '/non-discrimination',
    '/pricing',
    '/privacy-policy',
    '/privacy-practices'
]

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets')
CSS_DIR = os.path.join(ASSETS_DIR, 'css')
JS_DIR = os.path.join(ASSETS_DIR, 'js')
FONTS_DIR = os.path.join(ASSETS_DIR, 'fonts')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')

for d in [CSS_DIR, JS_DIR, FONTS_DIR, IMAGES_DIR]:
    os.makedirs(d, exist_ok=True)

def download_binary(url, dest_path):
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 0:
        return True
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read()
            with open(dest_path, 'wb') as f:
                f.write(content)
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def download_text(url):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error downloading text from {url}: {e}")
        return ""

print("Step 1: Downloading core CSS, JS, and Fonts...")

# 1. Download Font
recoleta_url = 'https://assets.website-files.com/6475b366ed49970529d05c4c/6475b366ed49970529d05cb5_92cd2256-c74e-421f-bd64-a207c4063918.woff'
font_dest = os.path.join(FONTS_DIR, 'Recoleta.woff')
print("Downloading Recoleta font...")
download_binary(recoleta_url, font_dest)

# 2. Download JS files
js_map = {
    'https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js?site=6475b366ed49970529d05c4c': 'jquery.min.js',
    'https://assets-global.website-files.com/6475b366ed49970529d05c4c/js/webflow.e17b4ef07.js': 'webflow.js',
    'https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js': 'webfont.js',
    'https://cdn.jsdelivr.net/npm/@finsweet/attributes-scrolldisable@1/scrolldisable.js': 'scrolldisable.js',
    'https://bundle.trysavvy.com/bundle.js': 'savvy-bundle.js'
}

for jurl, fname in js_map.items():
    print(f"Downloading JS {fname}...")
    download_binary(jurl, os.path.join(JS_DIR, fname))

# 3. Read discovered images
with open('discovered_assets.json') as f:
    discovered = json.load(f)

# Filter images & icons
image_extensions = ('.svg', '.png', '.jpg', '.jpeg', '.webp', '.gif', '.ico')
image_urls = [u for u in discovered if any(ext in u.lower() for ext in image_extensions)]

print(f"Total image/icon URLs to download: {len(image_urls)}")

# URL -> filename mapping
url_to_local_img = {}
used_filenames = {}

for u in image_urls:
    parsed = urlparse(u)
    base_fname = os.path.basename(parsed.path)
    base_fname = unquote(base_fname)
    base_fname = re.sub(r'[\\/*?:"<>|]', '_', base_fname)
    if not base_fname:
        base_fname = f"img_{abs(hash(u))}.png"
    
    # Handle possible filename collisions
    if base_fname in used_filenames and used_filenames[base_fname] != u:
        name, ext = os.path.splitext(base_fname)
        base_fname = f"{name}_{abs(hash(u)) % 10000}{ext}"
    
    used_filenames[base_fname] = u
    url_to_local_img[u] = base_fname
    
    # Also map variations without query string or scheme
    url_no_query = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    url_to_local_img[url_no_query] = base_fname
    url_to_local_img[f"//{parsed.netloc}{parsed.path}"] = base_fname
    url_to_local_img[parsed.path] = base_fname

print("Step 2: Downloading all images...")
for u, fname in list(url_to_local_img.items()):
    if u.startswith('http'):
        img_dest = os.path.join(IMAGES_DIR, fname)
        download_binary(u, img_dest)

print("Downloaded all images.")

# 4. Download and rewrite CSS
print("Step 3: Downloading and rewriting CSS...")
css_url = 'https://assets-global.website-files.com/6475b366ed49970529d05c4c/css/dreamlab-website-e0f709d63d04003d95aaea.webflow.925915b99.min.css'
css_content = download_text(css_url)

# Replace Recoleta font url
css_content = re.sub(
    r'https://assets\.website-files\.com/6475b366ed49970529d05c4c/6475b366ed49970529d05cb5_92cd2256-c74e-421f-bd64-a207c4063918\.woff',
    '../fonts/Recoleta.woff',
    css_content
)

# Replace all image URLs in CSS
for orig_url, fname in url_to_local_img.items():
    if orig_url in css_content:
        css_content = css_content.replace(orig_url, f'../images/{fname}')

with open(os.path.join(CSS_DIR, 'dreamlab.webflow.css'), 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Saved assets/css/dreamlab.webflow.css.")

with open('url_to_local_img.json', 'w') as f:
    json.dump(url_to_local_img, f, indent=2)

print("Setup completed successfully.")
