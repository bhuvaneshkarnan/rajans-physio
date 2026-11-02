import os
import subprocess
import shutil
from PIL import Image

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
ART_DIR = r'C:\Users\bhuva\.gemini\antigravity\brain\0c98d42e-15a8-45b3-9794-ac6925e26ede'

def capture(html_path, out_name, width, height):
    out_path = os.path.join(ROOT_DIR, out_name)
    cmd = [
        CHROME,
        '--headless=new',
        f'--screenshot={out_path}',
        f'--window-size={width},{height}',
        f'file:///{html_path}'
    ]
    subprocess.run(cmd, capture_output=True, check=True)
    return out_path

# 1. Desktop captures (1280px)
desk_home = capture(os.path.join(ROOT_DIR, 'index.html'), 'desk_home_full.png', 1280, 3600)
img_desk = Image.open(desk_home)

# Crop Desktop Header
crop_desk_header = img_desk.crop((0, 0, 1280, 110))
crop_desk_header.save(os.path.join(ROOT_DIR, 'desktop_header.png'))
shutil.copy(os.path.join(ROOT_DIR, 'desktop_header.png'), os.path.join(ART_DIR, 'desktop_header.png'))

# Crop Desktop Streamlined Footer
crop_desk_footer = img_desk.crop((0, img_desk.height - 460, 1280, img_desk.height))
crop_desk_footer.save(os.path.join(ROOT_DIR, 'desktop_footer.png'))
shutil.copy(os.path.join(ROOT_DIR, 'desktop_footer.png'), os.path.join(ART_DIR, 'desktop_footer.png'))

# 2. Mobile captures (390px - iPhone 14 / modern standard)
mob_home = capture(os.path.join(ROOT_DIR, 'index.html'), 'mob_home_full.png', 390, 4800)
img_mob = Image.open(mob_home)

# Crop Mobile Header + Hero
crop_mob_hero = img_mob.crop((0, 0, 390, 680))
crop_mob_hero.save(os.path.join(ROOT_DIR, 'mobile_hero.png'))
shutil.copy(os.path.join(ROOT_DIR, 'mobile_hero.png'), os.path.join(ART_DIR, 'mobile_hero.png'))

# Crop Mobile Streamlined Footer
crop_mob_footer = img_mob.crop((0, img_mob.height - 720, 390, img_mob.height))
crop_mob_footer.save(os.path.join(ROOT_DIR, 'mobile_footer.png'))
shutil.copy(os.path.join(ROOT_DIR, 'mobile_footer.png'), os.path.join(ART_DIR, 'mobile_footer.png'))

print("Desktop and mobile screenshots generated and copied to artifact directory.")
