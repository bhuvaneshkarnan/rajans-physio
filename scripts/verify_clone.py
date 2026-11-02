import os
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

html_files = []
for root, dirs, files in os.walk(ROOT_DIR):
    # skip .git or node_modules if any
    if 'assets' in root or '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith('.html') and f != 'target_index.html':
            html_files.append(os.path.join(root, f))

print(f"Total HTML files to verify: {len(html_files)}")

missing_assets = []
external_cdn_references = []

for hpath in html_files:
    rel_html = os.path.relpath(hpath, ROOT_DIR)
    dir_name = os.path.dirname(hpath)
    
    with open(hpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    
    # Check CSS
    for link in soup.find_all('link', rel='stylesheet'):
        href = link.get('href')
        if not href:
            continue
        if 'website-files.com' in href:
            external_cdn_references.append((rel_html, 'CSS', href))
        elif not href.startswith('http') and not href.startswith('//'):
            target_asset = os.path.normpath(os.path.join(dir_name, href))
            if not os.path.exists(target_asset) or os.path.getsize(target_asset) == 0:
                missing_assets.append((rel_html, 'CSS', href, target_asset))

    # Check JS
    for s in soup.find_all('script', src=True):
        src = s['src']
        if 'website-files.com' in src or 'cloudfront.net' in src:
            external_cdn_references.append((rel_html, 'JS', src))
        elif not src.startswith('http') and not src.startswith('//'):
            target_asset = os.path.normpath(os.path.join(dir_name, src))
            if not os.path.exists(target_asset) or os.path.getsize(target_asset) == 0:
                missing_assets.append((rel_html, 'JS', src, target_asset))

    # Check Images
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            if 'website-files.com' in src:
                external_cdn_references.append((rel_html, 'IMG src', src))
            elif not src.startswith('http') and not src.startswith('//') and not src.startswith('data:'):
                target_asset = os.path.normpath(os.path.join(dir_name, src))
                if not os.path.exists(target_asset) or os.path.getsize(target_asset) == 0:
                    missing_assets.append((rel_html, 'IMG src', src, target_asset))

        srcset = img.get('srcset')
        if srcset:
            for item in srcset.split(','):
                u = item.strip().split(' ')[0]
                if not u:
                    continue
                if 'website-files.com' in u:
                    external_cdn_references.append((rel_html, 'IMG srcset', u))
                elif not u.startswith('http') and not u.startswith('//') and not u.startswith('data:'):
                    target_asset = os.path.normpath(os.path.join(dir_name, u))
                    if not os.path.exists(target_asset) or os.path.getsize(target_asset) == 0:
                        missing_assets.append((rel_html, 'IMG srcset', u, target_asset))

    # Check Favicon / Touch Icons
    for link in soup.find_all('link', rel=lambda r: r and any(x in r for x in ['icon', 'apple-touch-icon'])):
        href = link.get('href')
        if href:
            if 'website-files.com' in href:
                external_cdn_references.append((rel_html, 'ICON', href))
            elif not href.startswith('http') and not href.startswith('//'):
                target_asset = os.path.normpath(os.path.join(dir_name, href))
                if not os.path.exists(target_asset) or os.path.getsize(target_asset) == 0:
                    missing_assets.append((rel_html, 'ICON', href, target_asset))

# Check CSS file itself
css_path = os.path.join(ROOT_DIR, 'assets', 'css', 'dreamlab.webflow.css')
css_dir = os.path.dirname(css_path)
with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
    css_text = f.read()

urls_in_css = re.findall(r'url\([\'"]?([^\'"\)]+)[\'"]?\)', css_text)
for u in urls_in_css:
    if u.startswith('data:'):
        continue
    if 'website-files.com' in u:
        external_cdn_references.append(('dreamlab.webflow.css', 'CSS url', u))
    elif not u.startswith('http') and not u.startswith('//'):
        target_asset = os.path.normpath(os.path.join(css_dir, u))
        if not os.path.exists(target_asset) or os.path.getsize(target_asset) == 0:
            missing_assets.append(('dreamlab.webflow.css', 'CSS url', u, target_asset))

print(f"\nMissing local assets count: {len(missing_assets)}")
for m in missing_assets[:10]:
    print("  MISSING:", m)

print(f"\nExternal CDN references remaining: {len(external_cdn_references)}")
for c in external_cdn_references[:10]:
    print("  CDN REF:", c)
