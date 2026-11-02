import os
import subprocess
from PIL import Image
import numpy as np

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

html_abs = os.path.join(ROOT_DIR, 'index.html')
out_abs = os.path.join(ROOT_DIR, 'verify_home_full.png')

cmd = [
    CHROME,
    '--headless=new',
    f'--screenshot={out_abs}',
    '--window-size=1280,3800',
    f'file:///{html_abs}'
]
subprocess.run(cmd, capture_output=True, check=True)

img = Image.open(out_abs)
print(f"Full homepage screenshot size: {img.size}")

# Search for yellow underline pixels around y=1600..2600
arr = np.array(img.convert('RGB'))
yellow_mask = (arr[:, :, 0] > 230) & (arr[:, :, 1] > 180) & (arr[:, :, 2] < 150)
coords = np.argwhere(yellow_mask)
print(f"Total yellow underline pixels: {len(coords)}")

# Group occurrences by Y
y_coords = coords[:, 0]
unique_y_blocks = []
for y in np.unique(y_coords):
    if not unique_y_blocks or y - unique_y_blocks[-1][-1] > 20:
        unique_y_blocks.append([y])
    else:
        unique_y_blocks[-1].append(y)

print(f"Found {len(unique_y_blocks)} distinct underlined heading sections:")
for idx, b in enumerate(unique_y_blocks):
    y_start, y_end = b[0], b[-1]
    mask_b = (coords[:, 0] >= y_start) & (coords[:, 0] <= y_end)
    x_start, x_end = coords[mask_b, 1].min(), coords[mask_b, 1].max()
    print(f"  Underline {idx+1}: y={y_start}..{y_end}, x={x_start}..{x_end}")
    
    # Crop a nice frame around it
    crop = img.crop((max(0, x_start - 120), max(0, y_start - 60), min(1280, x_end + 120), min(img.height, y_end + 50)))
    crop_path = os.path.join(ROOT_DIR, f'verify_underline_{idx+1}.png')
    crop.save(crop_path)
    print(f"  Saved: verify_underline_{idx+1}.png")

print("Underline verification complete.")
