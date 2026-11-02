import os
import re

SITE_URL = "https://rajans-physio.vercel.app"
DEFAULT_OG_IMAGE = f"{SITE_URL}/assets/images/og-share-card.jpg"

HTML_DIR = "."
SERVICE_PAGES = {
    "dorn-spinal-therapy": "Dorn Spinal Therapy & Gentle Alignment",
    "laser-therapy": "Advanced Scanning Laser Therapy (LASERSTIM)",
    "shockwave-therapy": "Radial Shockwave Therapy (ESWT)",
    "dry-needling": "Dry Needling Therapy (CDNT USA)",
    "tecar-therapy": "TECAR Radiofrequency Deep Tissue Repair",
    "cupping-iastm": "Cupping Therapy & IASTM Myofascial Release",
    "electrotherapy": "Electrotherapy & Therapeutic Ultrasound",
    "sports-rehabilitation": "Sports Injury Rehabilitation & Athletic Performance",
    "home-physiotherapy": "In-Home Physiotherapy & Bedside Rehabilitation",
    "about": "About Dr. Prabhu Rajan, PT & Clinical Team",
    "pricing": "Transparent Clinical Pricing & Assessment Packages",
    "faq": "Frequently Asked Patient Questions",
    "contact": "Contact & Location - Chromepet, Chennai",
    "free-assessment": "Free Online Pain Assessment & Symptom Checker",
    "blog": "Physiotherapy & Pain Relief Health Articles",
    "privacy-policy": "Privacy Policy",
    "privacy-practices": "Notice of Privacy Practices",
    "medical-terms": "Medical Terms of Care",
    "membership-terms": "Terms of Clinical Service",
    "non-discrimination": "Non-Discrimination Policy"
}

# 1. Update clinic-custom.css
CSS_PATH = os.path.join("assets", "css", "clinic-custom.css")
with open(CSS_PATH, "r", encoding="utf-8") as f:
    css = f.read()

# Replace or inject minimal hamburger styles
minimal_hamburger_css = """
  /* ========================================================
     CLEAN & MINIMALIST HAMBURGER BUTTON (ZERO BOX, SLEEK LINES)
     ======================================================== */
  .menu-button,
  .w-nav-button {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 40px !important;
    height: 40px !important;
    padding: 0 !important;
    margin: 0 !important;
    background: transparent !important;
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    outline: none !important;
    border-radius: 8px !important;
    cursor: pointer !important;
    z-index: 10001 !important;
    transition: background-color 0.2s ease, opacity 0.2s ease, transform 0.15s ease !important;
    -webkit-tap-highlight-color: transparent !important;
  }

  .menu-button:hover,
  .w-nav-button:hover,
  .menu-button:active,
  .w-nav-button:active {
    background: rgba(35, 62, 133, 0.06) !important;
    background-color: rgba(35, 62, 133, 0.06) !important;
  }

  .menu-button.open,
  .w-nav-button.w--open {
    background: transparent !important;
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
  }

  /* Sleek, Minimalist SVG Hamburger Lines */
  .hamburger-icon {
    display: block !important;
    width: 24px !important;
    height: 24px !important;
    overflow: visible !important;
  }

  .hamburger-icon line {
    stroke: #233E85 !important;
    stroke-width: 1.8 !important;
    stroke-linecap: round !important;
    transition: transform 0.26s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.2s ease, stroke 0.2s ease !important;
    transform-origin: 12px 12px !important;
  }

  /* Smooth Transform to Clean Minimal 'X' on Open */
  .menu-button.open .hamburger-icon line:nth-child(1),
  .w-nav-button.w--open .hamburger-icon line:nth-child(1) {
    transform: translateY(5px) rotate(45deg) !important;
    stroke: #233E85 !important;
  }

  .menu-button.open .hamburger-icon line:nth-child(2),
  .w-nav-button.w--open .hamburger-icon line:nth-child(2) {
    opacity: 0 !important;
    transform: scaleX(0) !important;
  }

  .menu-button.open .hamburger-icon line:nth-child(3),
  .w-nav-button.w--open .hamburger-icon line:nth-child(3) {
    transform: translateY(-5px) rotate(-45deg) !important;
    stroke: #233E85 !important;
  }
"""

# Replace previous Hamburger Button block in clinic-custom.css
old_hamburger_pattern = r'/\*\s*Hamburger Button\s*\*/.*?(?=/\*\s*Mobile Slide-down Navigation Drawer)'
if re.search(old_hamburger_pattern, css, re.DOTALL):
    css = re.sub(old_hamburger_pattern, minimal_hamburger_css + "\n  ", css, flags=re.DOTALL)
    print("Replaced old hamburger styles in clinic-custom.css")
else:
    # Append inside media query
    css += "\n" + minimal_hamburger_css
    print("Appended minimal hamburger styles to clinic-custom.css")

with open(CSS_PATH, "w", encoding="utf-8") as f:
    f.write(css)

# Also ensure dreamlab.webflow.css overrides any background on .w-nav-button.w--open
WEBFLOW_CSS_PATH = os.path.join("assets", "css", "dreamlab.webflow.css")
with open(WEBFLOW_CSS_PATH, "r", encoding="utf-8") as f:
    wf_css = f.read()

wf_override = "\n.w-nav-button{background-color:transparent !important;}\n.w-nav-button.w--open{background-color:transparent !important; color:#233E85 !important;}\n"
if ".w-nav-button{background-color:transparent" not in wf_css:
    wf_css += wf_override
    with open(WEBFLOW_CSS_PATH, "w", encoding="utf-8") as f:
        f.write(wf_css)
    print("Added transparent override to dreamlab.webflow.css")


# Clean minimal SVG for all HTML files
CLEAN_HAMBURGER_HTML = """<div class="menu-button w-nav-button" aria-label="Toggle navigation" role="button" tabindex="0">
          <svg class="hamburger-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#233E85" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="display:block; flex-shrink:0;">
            <line x1="4" y1="7" x2="20" y2="7"></line>
            <line x1="4" y1="12" x2="20" y2="12"></line>
            <line x1="4" y1="17" x2="20" y2="17"></line>
          </svg>
        </div>"""

def generate_social_meta(rel_path):
    base_name = os.path.splitext(os.path.basename(rel_path))[0]
    if base_name == "index" and os.path.dirname(rel_path) != "":
        base_name = os.path.basename(os.path.dirname(rel_path))
    
    is_home = (rel_path in ["index.html", "./index.html"] or base_name in ["index", ""])
    
    if is_home:
        page_title = "Rajan's Physiotherapy & Pain Relief Centre | Chromepet, Chennai (Since 2009)"
        page_desc = "17+ Years of Clinical Excellence in Chromepet, Chennai. Over 15,000+ patients healed without surgery. Specializing in Dorn spinal therapy, high-power laser & shockwave rehabilitation. Practo 99% Recommended."
        page_url = f"{SITE_URL}/"
    else:
        label = SERVICE_PAGES.get(base_name, base_name.replace("-", " ").title())
        page_title = f"{label} | Rajan's Physiotherapy & Pain Relief Centre"
        page_desc = f"Expert {label} at Rajan's Physiotherapy & Pain Relief Centre, Chromepet, Chennai. Led by Dr. Prabhu Rajan, PT (17+ Yrs Exp). Evidence-informed non-invasive care."
        page_url = f"{SITE_URL}/{base_name}.html"

    meta_block = f"""  <!-- PRIMARY SEARCH & SOCIAL META (WHATSAPP, FACEBOOK, TWITTER, LINKEDIN) -->
  <title>{page_title}</title>
  <meta name="description" content="{page_desc}">
  <link rel="canonical" href="{page_url}">

  <!-- Open Graph / Facebook / WhatsApp Preview -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{page_url}">
  <meta property="og:site_name" content="Rajan's Physiotherapy &amp; Pain Relief Centre">
  <meta property="og:title" content="{page_title}">
  <meta property="og:description" content="{page_desc}">
  <meta property="og:image" content="{DEFAULT_OG_IMAGE}">
  <meta property="og:image:secure_url" content="{DEFAULT_OG_IMAGE}">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Rajan's Physiotherapy &amp; Pain Relief Centre Chromepet">

  <!-- Twitter / X Large Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="{page_url}">
  <meta name="twitter:title" content="{page_title}">
  <meta name="twitter:description" content="{page_desc}">
  <meta name="twitter:image" content="{DEFAULT_OG_IMAGE}">

  <!-- Favicon & Mobile Icons -->
  <link rel="shortcut icon" href="{SITE_URL}/assets/images/clinic_favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="{SITE_URL}/assets/images/clinic_logo.png">
  <meta name="theme-color" content="#233E85">"""

    if is_home:
        schema_json = f"""
  <!-- Schema.org MedicalBusiness / Physiotherapy Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Physiotherapy",
    "name": "Rajan's Physiotherapy & Pain Relief Centre",
    "image": "{DEFAULT_OG_IMAGE}",
    "logo": "{SITE_URL}/assets/images/clinic_logo.png",
    "@id": "{SITE_URL}/",
    "url": "{SITE_URL}/",
    "telephone": "+919042612895",
    "priceRange": "₹₹",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "No. 9 / 29C, 1st Cross Street, Nagappa Nagar / New Colony, Behind Chromepet Police Station",
      "addressLocality": "Chromepet, Chennai",
      "postalCode": "600044",
      "addressRegion": "Tamil Nadu",
      "addressCountry": "IN"
    }},
    "geo": {{
      "@type": "GeoCoordinates",
      "latitude": 12.9516,
      "longitude": 80.1462
    }},
    "openingHoursSpecification": [
      {{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "opens": "09:30",
        "closes": "20:30"
      }},
      {{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": "Saturday",
        "opens": "09:00",
        "closes": "17:00"
      }}
    ],
    "medicalSpecialty": "Physiotherapy",
    "aggregateRating": {{
      "@type": "AggregateRating",
      "ratingValue": "4.9",
      "reviewCount": "730",
      "bestRating": "5"
    }}
  }}
  </script>"""
        meta_block += schema_json

    return meta_block


# Process all HTML files
html_files = []
for root, dirs, files in os.walk("."):
    if ".git" in root or ".gemini" in root or "node_modules" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.relpath(os.path.join(root, f), "."))

print(f"Found {len(html_files)} HTML files to update.")

updated_count = 0
for rel_path in html_files:
    with open(rel_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace menu-button SVG with clean minimal SVG
    menu_pattern = r'<div class="menu-button w-nav-button".*?</div>'
    if re.search(menu_pattern, content, re.DOTALL):
        content = re.sub(menu_pattern, CLEAN_HAMBURGER_HTML, content, count=1, flags=re.DOTALL)

    # 2. Update head meta tags
    head_start = content.find("<head>")
    head_end = content.find("</head>")
    if head_start != -1 and head_end != -1:
        head_content = content[head_start:head_end]
        
        # Remove existing title, description, og:, twitter:, canonical tags to avoid duplicates
        cleaned_head = head_content
        cleaned_head = re.sub(r'<title>.*?</title>', '', cleaned_head, flags=re.DOTALL | re.IGNORECASE)
        cleaned_head = re.sub(r'<meta[^>]+name=[\'"]description[\'"][^>]*>', '', cleaned_head, flags=re.IGNORECASE)
        cleaned_head = re.sub(r'<meta[^>]+property=[\'"]og:[^>]+>', '', cleaned_head, flags=re.IGNORECASE)
        cleaned_head = re.sub(r'<meta[^>]+name=[\'"]twitter:[^>]+>', '', cleaned_head, flags=re.IGNORECASE)
        cleaned_head = re.sub(r'<link[^>]+rel=[\'"]canonical[\'"][^>]*>', '', cleaned_head, flags=re.IGNORECASE)
        cleaned_head = re.sub(r'<script type="application/ld\+json">.*?</script>', '', cleaned_head, flags=re.DOTALL)
        
        new_meta = generate_social_meta(rel_path)
        
        # Inject right after <head>
        updated_head = cleaned_head.replace("<head>", f"<head>\n{new_meta}\n")
        content = content[:head_start] + updated_head + content[head_end:]

    with open(rel_path, "w", encoding="utf-8") as f:
        f.write(content)
    updated_count += 1

print(f"Successfully updated {updated_count} HTML files with clean minimal hamburger and full social sharing metadata.")
