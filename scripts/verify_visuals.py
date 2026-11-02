import os
import subprocess
from PIL import Image

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

def capture_screenshot(html_rel, output_png, width=1280, height=900):
    html_abs = os.path.join(ROOT_DIR, html_rel)
    out_abs = os.path.join(ROOT_DIR, output_png)
    cmd = [
        CHROME,
        '--headless=new',
        f'--screenshot={out_abs}',
        f'--window-size={width},{height}',
        f'file:///{html_abs}'
    ]
    subprocess.run(cmd, capture_output=True, check=True)
    print(f"Captured: {output_png}")
    return out_abs

# Capture homepage
capture_screenshot('index.html', 'verify_home.png', width=1280, height=2400)

# Load and crop key sections
img = Image.open(os.path.join(ROOT_DIR, 'verify_home.png'))
print(f"Homepage screenshot size: {img.size}")

# 1. Header crop (top 120px)
header_crop = img.crop((0, 0, 1280, 120))
header_crop.save(os.path.join(ROOT_DIR, 'verify_header.png'))

# 2. Hero section crop (100px to 600px)
hero_crop = img.crop((0, 100, 1280, 650))
hero_crop.save(os.path.join(ROOT_DIR, 'verify_hero.png'))

print("Visual verification captures saved.")
