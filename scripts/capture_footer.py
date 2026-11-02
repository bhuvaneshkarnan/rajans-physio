import subprocess
import os
import shutil
from PIL import Image

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
art_dir = r'C:\Users\bhuva\.gemini\antigravity\brain\0c98d42e-15a8-45b3-9794-ac6925e26ede'

out_contact = os.path.join(ROOT_DIR, 'verify_contact.png')
html_contact = os.path.join(ROOT_DIR, 'contact.html')

cmd_contact = [
    CHROME,
    '--headless=new',
    f'--screenshot={out_contact}',
    '--window-size=1280,1800',
    f'file:///{html_contact}'
]
subprocess.run(cmd_contact, capture_output=True, check=True)

img = Image.open(out_contact)
print('Contact page screenshot size:', img.size)

# Crop the footer at the bottom of the contact page
footer_crop = img.crop((0, img.height - 450, 1280, img.height))
out_footer = os.path.join(ROOT_DIR, 'verify_footer.png')
footer_crop.save(out_footer)

shutil.copy(out_footer, os.path.join(art_dir, 'verify_footer.png'))
print('Footer captured and copied to artifact directory.')
