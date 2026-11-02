import os
import re
import json
from urllib.parse import unquote, urlparse

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
IMAGES_DIR = os.path.join(ROOT_DIR, 'assets', 'images')

def normalize_name(name):
    # Unquote first (e.g. %20 -> space)
    unq = unquote(name)
    # Replace spaces and special chars
    clean = re.sub(r'[\s%]+', '_', unq)
    clean = re.sub(r'[\\/*?:"<>|()]', '_', clean)
    clean = re.sub(r'_+', '_', clean)
    return clean

# Step 1: Rename files in assets/images
renamed_map = {}
for fname in os.listdir(IMAGES_DIR):
    clean = normalize_name(fname)
    if clean != fname:
        src = os.path.join(IMAGES_DIR, fname)
        dst = os.path.join(IMAGES_DIR, clean)
        # Avoid overwriting different files
        if os.path.exists(dst) and src != dst:
            name, ext = os.path.splitext(clean)
            clean = f"{name}_norm{ext}"
            dst = os.path.join(IMAGES_DIR, clean)
        os.rename(src, dst)
        renamed_map[fname] = clean
    else:
        renamed_map[fname] = fname

print(f"Renamed {sum(1 for k, v in renamed_map.items() if k != v)} files with spaces/special characters.")

# Step 2: Update url_to_local_img mapping
with open(os.path.join(ROOT_DIR, 'discovered_assets.json')) as f:
    discovered = json.load(f)

new_url_map = {}
for u in discovered:
    parsed = urlparse(u)
    base_name = os.path.basename(parsed.path)
    clean_base = normalize_name(base_name)
    
    # Find matching file in IMAGES_DIR
    matched_file = None
    if os.path.exists(os.path.join(IMAGES_DIR, clean_base)):
        matched_file = clean_base
    else:
        # Search among files
        clean_no_ext = os.path.splitext(clean_base)[0]
        for f in os.listdir(IMAGES_DIR):
            if f.startswith(clean_no_ext[:30]):
                matched_file = f
                break
                
    if matched_file:
        new_url_map[u] = matched_file
        new_url_map[f"{parsed.scheme}://{parsed.netloc}{parsed.path}"] = matched_file
        new_url_map[f"//{parsed.netloc}{parsed.path}"] = matched_file
        new_url_map[parsed.path] = matched_file
        new_url_map[unquote(parsed.path)] = matched_file
        new_url_map[base_name] = matched_file
        new_url_map[unquote(base_name)] = matched_file

with open(os.path.join(ROOT_DIR, 'url_to_local_img.json'), 'w') as f:
    json.dump(new_url_map, f, indent=2)

print(f"Updated url_to_local_img.json with {len(new_url_map)} mapped entries.")
