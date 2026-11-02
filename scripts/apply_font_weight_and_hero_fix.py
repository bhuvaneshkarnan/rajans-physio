import os
import re

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

FONT_FACES_CSS = """/* ========================================================
   OFFICIAL BRAND TYPOGRAPHY & TRUE BOLD FONT FAMILIES
   ======================================================== */
@font-face {
  font-family: 'Recoleta';
  src: url('../fonts/Recoleta.woff') format('woff');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Recoleta';
  src: url('../fonts/Recoleta-Bold.woff') format('woff');
  font-weight: 600;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Recoleta';
  src: url('../fonts/Recoleta-Bold.woff') format('woff');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Recoleta';
  src: url('../fonts/Recoleta-Bold.woff') format('woff');
  font-weight: 800;
  font-style: normal;
  font-display: swap;
}

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

@font-face {
  font-family: 'Work Sans';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url('../fonts/WorkSans-Bold.ttf') format('truetype');
}

@font-face {
  font-family: 'Work Sans';
  font-style: normal;
  font-weight: 800;
  font-display: swap;
  src: url('../fonts/WorkSans-Bold.ttf') format('truetype');
}
"""

def update_css():
    css_path = os.path.join(ROOT_DIR, 'assets', 'css', 'clinic-custom.css')
    with open(css_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Prepend font-faces if not present
    if "src: url('../fonts/Recoleta-Bold.woff')" not in text:
        text = FONT_FACES_CSS + "\n" + text
        print("Injected font-face definitions into clinic-custom.css")

    # Update base typography for Headings & Paragraphs
    old_h1_rule = """h1, .heading-1 {
  font-family: 'Recoleta', Georgia, serif !important;
  font-size: clamp(34px, 4.4vw, 50px) !important;
  line-height: 1.15 !important;
  font-weight: 700 !important;
  color: #233E85;
  margin-top: 0 !important;
  margin-bottom: 16px !important;
  letter-spacing: -0.02em;
}"""

    new_h1_rule = """h1, .heading-1, .hero-title {
  font-family: 'Recoleta', Georgia, serif !important;
  font-size: clamp(36px, 4.8vw, 54px) !important;
  line-height: 1.14 !important;
  font-weight: 800 !important;
  color: #233E85;
  margin-top: 0 !important;
  margin-bottom: 18px !important;
  letter-spacing: -0.02em;
  font-synthesis: weight style !important;
  -webkit-font-synthesis: weight style !important;
}"""
    text = text.replace(old_h1_rule, new_h1_rule)

    # Enhance paragraph contrast
    old_p_rule = """p, .text, .body-text {
  font-family: 'Work Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 15px !important;
  line-height: 1.62 !important;
  color: #4A5568;
  margin-top: 0;
  margin-bottom: 14px;
}"""

    new_p_rule = """p, .text, .body-text {
  font-family: 'Work Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 15.5px !important;
  line-height: 1.65 !important;
  color: #2D3748 !important; /* Richer, crisper contrast on mobile retina */
  font-weight: 450 !important;
  margin-top: 0;
  margin-bottom: 14px;
}"""
    text = text.replace(old_p_rule, new_p_rule)

    # Lead text
    old_lead = """.text-lead {
  font-size: 16.5px !important;
  line-height: 1.65 !important;
  color: #374151;
}"""
    new_lead = """.text-lead {
  font-size: 17px !important;
  line-height: 1.65 !important;
  color: #1A202C !important;
  font-weight: 500 !important;
}"""
    text = text.replace(old_lead, new_lead)

    # Mobile typography in Section 12 (@media (max-width: 767px))
    old_mob_typography = """  /* Typography Hierarchy */
  h1, .heading-1 {
    font-size: clamp(24px, 6.2vw, 32px) !important;
    line-height: 1.2 !important;
    margin-bottom: 12px !important;
  }
  h2, .heading-2, .section-title {
    font-size: clamp(26px, 7vw, 34px) !important;
    line-height: 1.22 !important;
    margin-bottom: 14px !important;
  }
  h3, .heading-3 {
    font-size: 18px !important;
    line-height: 1.26 !important;
    margin-bottom: 8px !important;
  }
  p, .text, .body-text {
    font-size: 14.5px !important;
    line-height: 1.58 !important;
    margin-bottom: 12px !important;
  }
  .text-lead {
    font-size: 15.5px !important;
    line-height: 1.6 !important;
  }"""

    new_mob_typography = """  /* Typography Hierarchy (Larger, Bolder & High Contrast on Mobile) */
  h1, .heading-1, .hero-title {
    font-size: clamp(34px, 8.8vw, 44px) !important;
    line-height: 1.15 !important;
    font-weight: 800 !important;
    margin-bottom: 16px !important;
    letter-spacing: -0.02em !important;
  }
  h2, .heading-2, .section-title {
    font-size: clamp(28px, 7.2vw, 36px) !important;
    line-height: 1.2 !important;
    font-weight: 700 !important;
    margin-bottom: 14px !important;
    letter-spacing: -0.015em !important;
  }
  h3, .heading-3 {
    font-size: 20px !important;
    line-height: 1.26 !important;
    font-weight: 700 !important;
    margin-bottom: 10px !important;
  }
  p, .text, .body-text {
    font-size: 15px !important;
    line-height: 1.62 !important;
    color: #2D3748 !important;
    font-weight: 450 !important;
    margin-bottom: 14px !important;
  }
  .text-lead {
    font-size: 16.5px !important;
    line-height: 1.62 !important;
    color: #1A202C !important;
    font-weight: 500 !important;
    margin-bottom: 22px !important;
  }"""

    if old_mob_typography in text:
        text = text.replace(old_mob_typography, new_mob_typography)
        print("Updated Section 12 mobile typography.")
    else:
        # Try regex replacement
        text = re.sub(
            r'/\* Typography Hierarchy \*/\s*h1, \.heading-1 \{.*?\}.*?\.text-lead \{.*?\}',
            new_mob_typography.strip(),
            text,
            flags=re.DOTALL
        )
        print("Updated Section 12 mobile typography via regex.")

    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated clinic-custom.css successfully.")


def update_webflow_css():
    wf_path = os.path.join(ROOT_DIR, 'assets', 'css', 'dreamlab.webflow.css')
    with open(wf_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Prepend Recoleta-Bold and WorkSans-Bold if not present
    if "Recoleta-Bold.woff" not in text:
        text = FONT_FACES_CSS + "\n" + text
        with open(wf_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print("Injected font-faces into dreamlab.webflow.css")


def update_master_py():
    master_path = os.path.join(ROOT_DIR, 'scripts', 'build_full_website_master.py')
    with open(master_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Homepage Hero H1
    old_h1 = '<h1 class="heading-1" style="font-size:clamp(32px, 4vw, 46px); line-height:1.18 !important; margin-bottom:16px;">'
    new_h1 = '<h1 class="heading-1 hero-title" style="font-size:clamp(36px, 4.8vw, 54px); line-height:1.14 !important; font-weight:800 !important; margin-bottom:18px;">'
    content = content.replace(old_h1, new_h1)

    with open(master_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated build_full_website_master.py hero H1 successfully.")


def update_service_pages_py():
    service_path = os.path.join(ROOT_DIR, 'scripts', 'build_all_service_pages.py')
    with open(service_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Service Page Hero H1
    old_h1 = '<h1 style="font-family:\'Recoleta\',Georgia,serif; font-size:clamp(30px, 3.8vw, 44px); line-height:1.18 !important; color:#233E85 !important; margin-bottom:16px;">'
    new_h1 = '<h1 class="heading-1 hero-title" style="font-family:\'Recoleta\',Georgia,serif; font-size:clamp(34px, 4.4vw, 50px); line-height:1.16 !important; font-weight:800 !important; color:#233E85 !important; margin-bottom:18px;">'
    content = content.replace(old_h1, new_h1)

    with open(service_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated build_all_service_pages.py hero H1 successfully.")


if __name__ == '__main__':
    update_css()
    update_webflow_css()
    update_master_py()
    update_service_pages_py()
