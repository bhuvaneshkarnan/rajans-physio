import subprocess
import sys

scripts = [
    'scripts/build_full_website_master.py',
    'scripts/build_all_service_pages.py',
    'scripts/update_legal_pages.py',
    'scripts/update_blog_pages.py'
]

for s in scripts:
    print(f"Running {s}...")
    res = subprocess.run([sys.executable, s], capture_output=True, text=True, encoding='utf-8')
    if res.returncode != 0:
        print(f"Error running {s}:")
        print(res.stderr)
        sys.exit(1)
    else:
        print(f"Completed {s}: {res.stdout.strip()[:100]}...")

print("\n--- ALL PAGES REGENERATED SUCCESSFULLY ---")
