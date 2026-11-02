import os
import re

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def update_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig_len = len(content)
    for old, new in replacements:
        content = content.replace(old, new)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {os.path.basename(filepath)}: {orig_len} -> {len(content)} bytes")


# 1. Update build_all_service_pages.py
replacements_service = [
    ("#19535F", "#233E85"),
    ("#19535f", "#233E85"),
    ("#133E47", "#172A5C"),
    ("#E8F1F2", "#EEF3FA"),
    ("#e8f1f2", "#EEF3FA"),
    ("color:#5A6E72;", "color:#536B88;"),
]
update_file(os.path.join(ROOT_DIR, "scripts", "build_all_service_pages.py"), replacements_service)

# 2. Update build_full_website_master.py
replacements_master = [
    ("#19535F", "#233E85"),
    ("#19535f", "#233E85"),
    ("#133E47", "#172A5C"),
    ("#E8F1F2", "#EEF3FA"),
    ("#e8f1f2", "#EEF3FA"),
    ("color:#5A6E72;", "color:#536B88;"),
]
update_file(os.path.join(ROOT_DIR, "scripts", "build_full_website_master.py"), replacements_master)

print("Brand colors applied to builder scripts.")
