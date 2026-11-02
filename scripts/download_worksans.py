import urllib.request
import os

FONTS_DIR = os.path.join('assets', 'fonts')
CSS_FILE = os.path.join('assets', 'css', 'dreamlab.webflow.css')

fonts = {
    'WorkSans-Regular.ttf': 'https://fonts.gstatic.com/s/worksans/v24/QGY_z_wNahGAdqQ43RhVcIgYT2Xz5u32K0nXNig.ttf',
    'WorkSans-Medium.ttf': 'https://fonts.gstatic.com/s/worksans/v24/QGY_z_wNahGAdqQ43RhVcIgYT2Xz5u32K3vXNig.ttf',
    'WorkSans-SemiBold.ttf': 'https://fonts.gstatic.com/s/worksans/v24/QGY_z_wNahGAdqQ43RhVcIgYT2Xz5u32K5fQNig.ttf'
}

for fname, url in fonts.items():
    dest = os.path.join(FONTS_DIR, fname)
    if not os.path.exists(dest):
        print(f"Downloading {fname}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            with open(dest, 'wb') as f:
                f.write(resp.read())

font_faces = """
@font-face {
  font-family: 'Work Sans';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url('../fonts/WorkSans-Regular.ttf') format('truetype');
}
@font-face {
  font-family: 'Work Sans';
  font-style: normal;
  font-weight: 500;
  font-display: swap;
  src: url('../fonts/WorkSans-Medium.ttf') format('truetype');
}
@font-face {
  font-family: 'Work Sans';
  font-style: normal;
  font-weight: 600;
  font-display: swap;
  src: url('../fonts/WorkSans-SemiBold.ttf') format('truetype');
}
"""

with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

if 'WorkSans-Regular.ttf' not in css:
    css = font_faces + "\n" + css
    with open(CSS_FILE, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Injected local Work Sans @font-face into dreamlab.webflow.css")
else:
    print("Work Sans already present in CSS.")
