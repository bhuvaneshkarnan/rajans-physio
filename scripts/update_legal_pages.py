import os
import re
from build_full_website import get_global_head, get_global_nav, get_global_footer

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

LEGAL_PAGES = [
    ("privacy-policy", "Privacy Policy | Rajan's Physiotherapy Centre", "Privacy Policy and patient data handling practices for Rajan's Physiotherapy & Pain Relief Centre, Chromepet, Chennai."),
    ("privacy-practices", "Notice of Privacy Practices | Rajan's Physiotherapy", "Notice of Privacy Practices in compliance with clinical and healthcare privacy guidelines."),
    ("medical-terms", "Medical Terms of Care & Consent | Rajan's Physiotherapy", "Medical terms of care, informed consent and rehabilitation protocol terms for Rajan's Physiotherapy."),
    ("membership-terms", "Terms of Service & Clinical Care | Rajan's Physiotherapy", "Terms of clinical care and appointment policies for Rajan's Physiotherapy & Pain Relief Centre."),
    ("non-discrimination", "Non-Discrimination Policy | Rajan's Physiotherapy", "Equal care and non-discrimination commitment of Rajan's Physiotherapy & Pain Relief Centre."),
]

def update_legal_page(slug, title, desc):
    filepath = os.path.join(ROOT_DIR, f"{slug}.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract title from h1 or hero
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL | re.IGNORECASE)
    h1_text = h1_match.group(1).strip() if h1_match else slug.replace('-', ' ').title()

    # Extract the main article/legal text
    # In webflow legal pages, it's typically inside a rich-text or container
    body_text_match = re.search(r'<div[^>]*class="[^"]*(?:rich-text|text-rich|legal__content|container)[^"]*"[^>]*>(.*?)</div>\s*</div>\s*</div>', html, re.DOTALL | re.IGNORECASE)
    
    # Or let's grab everything between the end of navbar and the start of footer
    nav_end = html.find('</header>')
    if nav_end == -1:
        nav_end = html.find('</div></div></div>') # after navbar
    if nav_end == -1:
        nav_end = 0
    else:
        nav_end += 9

    footer_start = html.find('<footer')
    if footer_start == -1:
        footer_start = html.find('class="footer"')
    if footer_start == -1:
        footer_start = len(html) - 200

    content_inner = html[nav_end:footer_start].strip()
    
    # Clean up content_inner from old dreamlab references and teal colors
    content_inner = content_inner.replace('#19535F', '#233E85').replace('#19535f', '#233E85')
    content_inner = content_inner.replace('#133E47', '#172A5C').replace('#E8F1F2', '#EEF3FA')
    content_inner = content_inner.replace('Dreamlab', "Rajan's Physiotherapy")
    content_inner = content_inner.replace('dreamlab', "Rajan's Physiotherapy")

    def render(depth_prefix):
        asset_prefix = f"{depth_prefix}assets/" if depth_prefix else "assets/"
        home_link = depth_prefix if depth_prefix else "./"
        if not home_link.endswith(('/', 'index.html')):
            home_link = home_link + "index.html" if home_link else "./index.html"

        # Fix relative image/css links inside content_inner
        inner = content_inner
        if depth_prefix:
            inner = re.sub(r'src="assets/', f'src="{depth_prefix}assets/', inner)
            inner = re.sub(r'href="assets/', f'href="{depth_prefix}assets/', inner)

        return f"""{get_global_head(title, desc, asset_prefix)}
{get_global_nav(depth_prefix, "")}

  <main style="background:#FAF9F6; min-height:80vh; padding:60px 0 80px 0;">
    <div class="container w-container" style="max-width:860px; background:#FFFFFF; padding:48px 56px; border-radius:20px; border:1px solid #DCE5F5;">
      <div style="font-size:12px; font-weight:700; letter-spacing:1px; text-transform:uppercase; color:#ED1D7F; margin-bottom:12px;">
        LEGAL &amp; PATIENT CARE POLICIES
      </div>
      <h1 style="font-family:'Recoleta',Georgia,serif; font-size:36px; line-height:1.2; color:#233E85; margin-bottom:24px;">
        {h1_text}
      </h1>
      <div style="font-size:13.5px; color:#536B88; margin-bottom:32px; padding-bottom:16px; border-bottom:1px solid #DCE5F5;">
        Last Updated: Clinical Year 2026 &bull; Rajan's Physiotherapy &amp; Pain Relief Centre, Chromepet, Chennai
      </div>
      <div style="font-size:15px; line-height:1.75; color:#374151;">
        {inner}
      </div>
    </div>
  </main>

{get_global_footer(depth_prefix)}"""

    root_html = render("")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(root_html)

    sub_path = os.path.join(ROOT_DIR, slug, "index.html")
    os.makedirs(os.path.dirname(sub_path), exist_ok=True)
    sub_html = render("../")
    with open(sub_path, 'w', encoding='utf-8') as f:
        f.write(sub_html)

    print(f"Updated legal page: {slug}.html & {slug}/index.html")

for slug, title, desc in LEGAL_PAGES:
    update_legal_page(slug, title, desc)

print("All legal pages updated successfully!")
