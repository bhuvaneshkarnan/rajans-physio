import os
import json

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

with open(os.path.join(ROOT_DIR, 'extracted_data', 'clinic_data.json'), 'r', encoding='utf-8') as f:
    clinic_data = json.load(f)

def get_head(title, desc, asset_prefix):
    return f"""<!DOCTYPE html>
<html data-wf-domain="rajansphysio.com" lang="en">
<head>
  <meta charset="utf-8"/>
  <title>{title}</title>
  <meta content="{desc}" name="description"/>
  <meta content="{title}" property="og:title"/>
  <meta content="width=device-width, initial-scale=1" name="viewport"/>
  <link href="{asset_prefix}css/dreamlab.webflow.css" rel="stylesheet" type="text/css"/>
  <link href="{asset_prefix}images/6475b366ed49970529d05ce3_Favicon.svg" rel="shortcut icon" type="image/x-icon"/>
  <link href="{asset_prefix}images/6475b366ed49970529d05ce4_Touch_icon.svg" rel="apple-touch-icon"/>
  <style>
    html, body {{
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      font-feature-settings: "liga","kern";
      color: #19535F;
    }}
    .clinic-badge {{
      display: inline-block;
      padding: 6px 14px;
      border-radius: 30px;
      font-size: 13px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      background: #E8F1F2;
      color: #19535F;
      margin-bottom: 16px;
    }}
    .service-card {{
      background: #FFFFFF;
      border-radius: 20px;
      padding: 30px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.04);
      transition: all 0.3s ease;
    }}
    .service-card:hover {{
      transform: translateY(-5px);
      box-shadow: 0 12px 30px rgba(25, 83, 95, 0.12);
    }}
    .faq-accordion {{
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 14px;
      margin-bottom: 14px;
      overflow: hidden;
      transition: all 0.2s ease;
    }}
    .faq-question {{
      padding: 20px 24px;
      font-weight: 700;
      font-size: 17px;
      color: #19535F;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .faq-answer {{
      padding: 0 24px 20px 24px;
      font-size: 15px;
      line-height: 1.7;
      color: #4A5568;
      display: block;
    }}
    .checker-option {{
      border: 2px solid #E2E8F0;
      border-radius: 12px;
      padding: 14px 18px;
      margin-bottom: 10px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 12px;
      transition: all 0.2s ease;
    }}
    .checker-option:hover, .checker-option.selected {{
      border-color: #19535F;
      background: #E8F1F2;
    }}
  </style>
</head>
<body>"""

def get_nav(depth_prefix, active_page):
    asset_prefix = f"{depth_prefix}assets/" if depth_prefix else "assets/"
    home_active = "w--current" if active_page == "home" else ""
    about_active = "w--current" if active_page == "about" else ""
    pricing_active = "w--current" if active_page == "pricing" else ""
    faq_active = "w--current" if active_page == "faq" else ""
    checker_active = "w--current" if active_page == "checker" else ""
    
    return f"""  <header>
    <div data-animation="default" data-collapse="medium" data-duration="400" data-easing="ease" data-easing2="ease" role="banner" class="navbar w-nav">
      <div class="container container--navbar w-container" style="display:flex; justify-content:space-between; align-items:center;">
        
        <a href="{depth_prefix or './'}" title="Rajan's Physiotherapy &amp; Pain Relief Centre" class="brand w-nav-brand" style="text-decoration:none; display:flex; align-items:center; gap:12px;">
          <div style="width:44px; height:44px; border-radius:50%; background:#19535F; color:#FBF5E9; display:flex; align-items:center; justify-content:center; font-family:'Recoleta',serif; font-size:24px; font-weight:700; box-shadow:0 3px 8px rgba(25,83,95,0.25);">R</div>
          <div style="display:flex; flex-direction:column;">
            <span style="font-family:'Recoleta',serif; font-size:20px; font-weight:700; color:#19535F; line-height:1.15;">Rajan's Physiotherapy</span>
            <span style="font-size:11px; letter-spacing:0.8px; color:#5A6E72; text-transform:uppercase; font-weight:600;">&amp; Pain Relief Centre &bull; Since 2009</span>
          </div>
        </a>

        <nav role="navigation" class="nav-menu w-nav-menu" style="display:flex; align-items:center;">
          <a href="{depth_prefix or './'}" class="nav__link w-nav-link {home_active}">Home</a>
          <a href="{depth_prefix}about.html" class="nav__link w-nav-link {about_active}">About Us</a>
          <a href="{depth_prefix}pricing.html" class="nav__link w-nav-link {pricing_active}">Pricing &amp; Fees</a>
          <a href="{depth_prefix}faq.html" class="nav__link w-nav-link {faq_active}">FAQ</a>
          <a href="{depth_prefix}free-assessment.html" class="nav__link w-nav-link {checker_active}">Pain Checker</a>
          <a href="tel:9042612895" class="button w-button" style="margin-left:16px; background:#19535F; padding:10px 22px; font-size:14px;">Call: 90426 12895</a>
        </nav>

        <div class="menu-button w-nav-button">
          <div class="icon w-icon-nav-menu"></div>
        </div>
      </div>
    </div>
  </header>"""

def get_footer(depth_prefix):
    return f"""  <footer class="footer" style="padding:60px 0 30px 0; background:#FFFFFF; border-top:1px solid #E2E8F0;">
      <div class="container w-container">
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap:40px; margin-bottom:50px;">
          <div>
            <h4 style="font-family:'Recoleta',serif; font-size:22px; color:#19535F; margin-bottom:12px;">Rajan's Physiotherapy &amp; Pain Relief Centre</h4>
            <p style="font-size:14px; line-height:1.6; color:#4A5568; margin-bottom:16px;">
              Evidence-informed, patient-centred physiotherapy and rehabilitation since 2009. Specializing in sports rehabilitation, Dorn method spinal therapy, advanced laser &amp; shockwave treatment.
            </p>
            <p style="font-size:13px; font-weight:600; color:#19535F;">Lead by Dr. Prabhu Rajan, PT (17 Yrs Exp &bull; MIAP L-27944)</p>
          </div>
          <div>
            <h5 style="font-size:16px; font-weight:700; color:#19535F; margin-bottom:14px;">Clinic Timings</h5>
            <p style="font-size:14px; line-height:1.6; color:#4A5568; margin-bottom:6px;">
              <strong>Monday &ndash; Friday:</strong><br>9:30 AM &ndash; 2:00 PM &bull; 4:00 PM &ndash; 8:30 PM
            </p>
            <p style="font-size:14px; line-height:1.6; color:#4A5568; margin-bottom:6px;">
              <strong>Saturday:</strong> 9:00 AM &ndash; 5:00 PM
            </p>
            <p style="font-size:14px; line-height:1.6; color:#E53E3E;">
              <strong>Sunday:</strong> Holiday (Emergency by Appointment)
            </p>
          </div>
          <div>
            <h5 style="font-size:16px; font-weight:700; color:#19535F; margin-bottom:14px;">Contact &amp; Location</h5>
            <p style="font-size:14px; line-height:1.6; color:#4A5568; margin-bottom:8px;">
              📍 No. 9 / 29C, 1st Cross Street, Nagappa Nagar / New Colony, Chromepet, Chennai &ndash; 600044<br>
              <em style="font-size:12px; color:#718096;">(Behind Chromepet Police Station / Shastri Colony)</em>
            </p>
            <p style="font-size:14px; line-height:1.6; color:#4A5568; margin-bottom:8px;">
              📞 <strong>Phone:</strong> <a href="tel:9042612895" style="color:#19535F; font-weight:600;">+91 90426 12895</a> / <a href="tel:9840512895" style="color:#19535F;">98405 12895</a>
            </p>
            <p style="font-size:14px; line-height:1.6; color:#4A5568; margin-bottom:8px;">
              💬 <strong>WhatsApp:</strong> <a href="https://wa.me/919042612895?text=Hello%20Dr.%20Prabhu%2C%20I%20would%20like%20to%20consult%20regarding%20physiotherapy" target="_blank" style="color:#25D366; font-weight:600;">+91 90426 12895</a>
            </p>
            <p style="font-size:14px; line-height:1.6; color:#4A5568;">
              ✉️ <strong>Email:</strong> <a href="mailto:rajansphysio2009@gmail.com" style="color:#19535F;">rajansphysio2009@gmail.com</a>
            </p>
          </div>
          <div>
            <h5 style="font-size:16px; font-weight:700; color:#19535F; margin-bottom:14px;">Quick Links</h5>
            <ul style="list-style:none; padding:0; margin:0; line-height:2.2; font-size:14px;">
              <li><a href="{depth_prefix}about.html" style="color:#4A5568; text-decoration:none;">About Dr. Prabhu Rajan</a></li>
              <li><a href="{depth_prefix}pricing.html" style="color:#4A5568; text-decoration:none;">Consultation &amp; Pricing</a></li>
              <li><a href="{depth_prefix}faq.html" style="color:#4A5568; text-decoration:none;">Frequently Asked Questions</a></li>
              <li><a href="{depth_prefix}free-assessment.html" style="color:#4A5568; text-decoration:none;">Free Pain Assessment</a></li>
              <li><a href="https://share.google/tpyR96H2jyHYaLHxz" target="_blank" style="color:#19535F; font-weight:600;">Google Maps Directions ↗</a></li>
            </ul>
          </div>
        </div>
        <div style="border-top:1px solid #E2E8F0; padding-top:24px; display:flex; justify-content:space-between; flex-wrap:wrap; gap:16px; font-size:13px; color:#718096;">
          <p>&copy; 2009 &ndash; 2026 Rajan's Physiotherapy &amp; Pain Relief Centre. All rights reserved.</p>
          <p>Chromepet, Chennai &bull; Practo 99% Recommended (513+ Ratings) &bull; Justdial 4.9★ (730+ Reviews)</p>
        </div>
      </div>
    </footer>
    <script src="{depth_prefix}assets/js/jquery.min.js" type="text/javascript"></script>
    <script src="{depth_prefix}assets/js/webflow.js" type="text/javascript"></script>
    <script>
      if (window.location.protocol === 'file:') {{
        document.addEventListener('DOMContentLoaded', function() {{
          var depth = '{depth_prefix}';
          document.querySelectorAll('a[href^="/"]').forEach(function(a) {{
            var h = a.getAttribute('href');
            if (h === '/') {{
              a.setAttribute('href', depth + 'index.html');
            }} else if (!h.startsWith('mailto:') && !h.startsWith('tel:') && !h.startsWith('#')) {{
              var path = h.substring(1).replace(/\\/$/, '');
              a.setAttribute('href', depth + path + '.html');
            }}
          }});
        }});
      }}
    </script>
</body>
</html>"""

# ----------------- ABOUT PAGE -----------------
def generate_about_html(depth_prefix):
    asset_prefix = f"{depth_prefix}assets/" if depth_prefix else "assets/"
    return f"""{get_head("About Dr. Prabhu Rajan, PT | Rajan's Physiotherapy Chromepet", "Learn about Dr. Prabhu Rajan, PT (17 Yrs Exp, MPT Sports, MIAP) and Rajan's Physiotherapy & Pain Relief Centre, established in 2009 in Chromepet, Chennai.", asset_prefix)}
  {get_nav(depth_prefix, "about")}
  <main>
    <section class="section" style="padding:80px 0 50px 0; background:#FBF5E9;">
      <div class="container w-container" style="text-align:center; max-width:850px;">
        <span class="clinic-badge">ESTABLISHED 2009 &bull; CHROMEPET, CHENNAI</span>
        <h1 class="heading-1 recoleta blue5" style="font-size:44px; margin-bottom:20px;">
          Restoring pain-free movement <span class="highlight highlight--line">since 2009.</span>
        </h1>
        <p style="font-size:18px; line-height:1.7; color:#4A5568;">
          At Rajan's Physiotherapy and Pain Relief Centre, we are committed to professional, evidence-informed, and patient-centred rehabilitation. Our focus is eliminating pain at the root cause without lifetime painkillers or unnecessary surgery.
        </p>
      </div>
    </section>

    <!-- MEET THE DOCTOR SECTION -->
    <section class="section" style="padding:70px 0;">
      <div class="container w-container">
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:50px; align-items:center;">
          <div>
            <img src="{asset_prefix}images/dr_prabhu_rajan_profile.jpg" alt="Dr. Prabhu Rajan PT" style="width:100%; border-radius:24px; box-shadow:0 15px 35px rgba(25,83,95,0.15);"/>
          </div>
          <div>
            <span class="clinic-badge">CHIEF PHYSIOTHERAPIST</span>
            <h2 class="heading-2 recoleta" style="font-size:36px; margin-bottom:12px; color:#19535F;">Dr. Prabhu Rajan, PT</h2>
            <p style="font-size:16px; font-weight:700; color:#19535F; margin-bottom:16px;">
              Senior Physiotherapist &bull; Sports &amp; Musculoskeletal Rehabilitation Specialist (MIAP L-27944)
            </p>
            <p style="font-size:15px; line-height:1.7; color:#4A5568; margin-bottom:16px;">
              With over 17 years of dedicated clinical practice, Dr. Prabhu Rajan completed his Bachelor of Physiotherapy (BPT) in 2009 and Master's in Sports Physiotherapy (MPT) in 2013 from The Tamil Nadu Dr. M.G.R. Medical University. He earned his Doctorate in Acupuncture (D.Ac) from the University of Colombo in 2012.
            </p>
            <p style="font-size:15px; line-height:1.7; color:#4A5568; margin-bottom:20px;">
              Dr. Prabhu serves as the <strong>Vice Chairman of the All India Dorn Therapy Association (AIDTA)</strong> and holds international certifications in Manual Chiropractic, Dry Needling (CDNT USA), Osteopathy, Varma Therapy, and Kinesio Taping (CKT).
            </p>
            
            <div style="background:#FAF6EE; border-radius:16px; padding:20px; margin-bottom:24px;">
              <h4 style="font-size:15px; font-weight:700; color:#19535F; margin-bottom:8px;">Qualifications &amp; Certifications</h4>
              <p style="font-size:13px; color:#4A5568; margin:0; line-height:1.6;">
                BPT &bull; MPT (Sports) &bull; Dr.Acu (Colombo) &bull; MIAP L-27944 &bull; Dip. Osteo &bull; Dip. Mcp &bull; Dip. Varma &bull; Dip. EAcu &bull; CDNT (USA) &bull; CEMT &bull; CEOMT &bull; CKT &bull; Certified Dorn Specialist
              </p>
            </div>

            <a class="button w-button" href="https://wa.me/919042612895?text=Hello%20Dr.%20Prabhu%2C%20I%20would%20like%20to%20consult%20regarding%20physiotherapy" target="_blank" style="background:#25D366; font-size:15px; padding:12px 26px;">
              💬 Book Consultation on WhatsApp
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- CLINIC FACILITIES TOUR -->
    <section class="section" style="padding:70px 0; background:#FAF6EE;">
      <div class="container w-container">
        <div style="text-align:center; max-width:760px; margin:0 auto 50px auto;">
          <p class="uppercase blue4" style="font-weight:700; letter-spacing:1px;">CLINIC TOUR</p>
          <h3 class="heading-3 recoleta" style="font-size:36px;">Modern facilities designed for your comfort</h3>
          <p style="color:#4A5568; font-size:16px;">Located conveniently behind Chromepet Police Station on 1st Cross Street, Nagappa Nagar.</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:24px;">
          <div style="border-radius:18px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.05); background:#FFF;">
            <img src="{asset_prefix}images/clinic_photo_banner_1.jpg" alt="Clinic Exterior" style="width:100%; height:200px; object-fit:cover;"/>
            <div style="padding:16px;"><strong style="color:#19535F;">Clinic Exterior</strong><p style="font-size:13px; color:#718096; margin:4px 0 0 0;">Spacious clinic with clear signage</p></div>
          </div>
          <div style="border-radius:18px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.05); background:#FFF;">
            <img src="{asset_prefix}images/clinic_entrance.jpg" alt="Clinic Entrance" style="width:100%; height:200px; object-fit:cover;"/>
            <div style="padding:16px;"><strong style="color:#19535F;">Entrance Gate &amp; Parking</strong><p style="font-size:13px; color:#718096; margin:4px 0 0 0;">Dedicated 29C entrance</p></div>
          </div>
          <div style="border-radius:18px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.05); background:#FFF;">
            <img src="{asset_prefix}images/clinic_treatment_room_1.jpg" alt="Consultation Desk" style="width:100%; height:200px; object-fit:cover;"/>
            <div style="padding:16px;"><strong style="color:#19535F;">Consultation Room</strong><p style="font-size:13px; color:#718096; margin:4px 0 0 0;">Spine anatomy model &amp; diagnostic desk</p></div>
          </div>
          <div style="border-radius:18px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.05); background:#FFF;">
            <img src="{asset_prefix}images/clinic_interior_reception.jpg" alt="Patient Lounge" style="width:100%; height:200px; object-fit:cover;"/>
            <div style="padding:16px;"><strong style="color:#19535F;">Patient Reception &amp; Lounge</strong><p style="font-size:13px; color:#718096; margin:4px 0 0 0;">Comfortable waiting seating</p></div>
          </div>
        </div>
      </div>
    </section>
  </main>
  {get_footer(depth_prefix)}"""

# ----------------- PRICING PAGE -----------------
def generate_pricing_html(depth_prefix):
    asset_prefix = f"{depth_prefix}assets/" if depth_prefix else "assets/"
    return f"""{get_head("Consultation Fees & Pricing | Rajan's Physiotherapy Chromepet", "Transparent physiotherapy fees at Rajan's Physiotherapy & Pain Relief Centre. Initial consultation ₹600. Cash & GPay accepted.", asset_prefix)}
  {get_nav(depth_prefix, "pricing")}
  <main>
    <section class="section" style="padding:80px 0 50px 0; background:#FBF5E9;">
      <div class="container w-container" style="text-align:center; max-width:850px;">
        <span class="clinic-badge">TRANSPARENT &bull; NO HIDDEN CHARGES</span>
        <h1 class="heading-1 recoleta blue5" style="font-size:44px; margin-bottom:20px;">
          Affordable care for <span class="highlight highlight--line">everyone.</span>
        </h1>
        <p style="font-size:18px; line-height:1.7; color:#4A5568;">
          Rest and mobility are rights everyone should be able to afford. Rajan's Physiotherapy offers transparent, highly affordable treatment fees tailored to your personal condition.
        </p>
      </div>
    </section>

    <!-- PRICING TIERS -->
    <section class="section" style="padding:70px 0;">
      <div class="container w-container">
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:32px;">
          
          <!-- INITIAL CONSULTATION -->
          <div style="background:#FFFFFF; border:2px solid #19535F; border-radius:24px; padding:36px; box-shadow:0 10px 30px rgba(25,83,95,0.08); display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="background:#19535F; color:#FBF5E9; display:inline-block; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:700; margin-bottom:16px;">FIRST VISIT</div>
              <h3 style="font-family:'Recoleta',serif; font-size:26px; color:#19535F; margin-bottom:8px;">Initial Consultation</h3>
              <div style="font-family:'Recoleta',serif; font-size:46px; font-weight:700; color:#19535F; margin:14px 0;">₹600</div>
              <p style="font-size:14px; color:#718096; margin-bottom:20px;">One-time comprehensive clinical physical assessment</p>
              
              <ul style="list-style:none; padding:0; margin:0 0 30px 0; line-height:2.2; font-size:14px; color:#4A5568;">
                <li>✓ Full physical palpation &amp; mobility examination</li>
                <li>✓ Spine, joint, and posture alignment assessment</li>
                <li>✓ Root-cause diagnosis (No unnecessary scans)</li>
                <li>✓ Explanation of diagnosis in plain language</li>
                <li>✓ Personalized recovery roadmap &amp; exercise advice</li>
              </ul>
            </div>
            <a class="button w-button" href="https://wa.me/919042612895?text=Hello%20Dr.%20Prabhu%2C%20I%20would%20like%20to%20book%20an%20initial%20consultation" target="_blank" style="background:#19535F; text-align:center; padding:14px; font-size:15px;">Book Consultation</a>
          </div>

          <!-- FOLLOW UP SESSIONS -->
          <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:24px; padding:36px; box-shadow:0 4px 20px rgba(0,0,0,0.04); display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="background:#E8F1F2; color:#19535F; display:inline-block; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:700; margin-bottom:16px;">FOLLOW-UP CARE</div>
              <h3 style="font-family:'Recoleta',serif; font-size:26px; color:#19535F; margin-bottom:8px;">Treatment Sessions</h3>
              <div style="font-family:'Recoleta',serif; font-size:36px; font-weight:700; color:#19535F; margin:14px 0;">Customized</div>
              <p style="font-size:14px; color:#718096; margin-bottom:20px;">Fee based on specific treatment modalities needed</p>
              
              <ul style="list-style:none; padding:0; margin:0 0 30px 0; line-height:2.2; font-size:14px; color:#4A5568;">
                <li>✓ Dorn Method vertebrae alignment &amp; mobilization</li>
                <li>✓ Advanced Scanning Laser &amp; Radial Shockwave</li>
                <li>✓ Clinical Dry Needling (CDNT USA) &amp; Cupping</li>
                <li>✓ IFT, Ultrasonic Therapy (UST), EMS, SWD</li>
                <li>✓ Ongoing progress evaluation every session</li>
              </ul>
            </div>
            <a class="button w-button" href="tel:9042612895" style="background:#19535F; text-align:center; padding:14px; font-size:15px;">Enquire Details</a>
          </div>

          <!-- HOME VISITS -->
          <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:24px; padding:36px; box-shadow:0 4px 20px rgba(0,0,0,0.04); display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="background:#E8F1F2; color:#19535F; display:inline-block; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:700; margin-bottom:16px;">AT YOUR DOORSTEP</div>
              <h3 style="font-family:'Recoleta',serif; font-size:26px; color:#19535F; margin-bottom:8px;">Home Physiotherapy</h3>
              <div style="font-family:'Recoleta',serif; font-size:36px; font-weight:700; color:#19535F; margin:14px 0;">Distance Based</div>
              <p style="font-size:14px; color:#718096; margin-bottom:20px;">For post-operative, elderly, or severely immobile patients</p>
              
              <ul style="list-style:none; padding:0; margin:0 0 30px 0; line-height:2.2; font-size:14px; color:#4A5568;">
                <li>✓ Complete physiotherapy at your residence</li>
                <li>✓ Post-joint replacement (Knee / Hip) rehabilitation</li>
                <li>✓ Post-fracture &amp; stroke mobility restoration</li>
                <li>✓ Gait training, balance &amp; fall prevention</li>
                <li>✓ Coverage across Chromepet &amp; nearby areas</li>
              </ul>
            </div>
            <a class="button w-button" href="https://wa.me/919042612895?text=Hello%20Dr.%20Prabhu%2C%20I%20would%20like%20to%20enquire%20about%20home%20physiotherapy" target="_blank" style="background:#25D366; text-align:center; padding:14px; font-size:15px;">Book Home Visit</a>
          </div>

        </div>
      </div>
    </section>
  </main>
  {get_footer(depth_prefix)}"""

# ----------------- FAQ PAGE -----------------
def generate_faq_html(depth_prefix):
    asset_prefix = f"{depth_prefix}assets/" if depth_prefix else "assets/"
    return f"""{get_head("FAQ | Rajan's Physiotherapy & Pain Relief Centre Chromepet", "Frequently asked questions about physiotherapy, Dr. Prabhu Rajan, Dorn method, fees, timings, and location in Chromepet.", asset_prefix)}
  {get_nav(depth_prefix, "faq")}
  <main>
    <section class="section" style="padding:80px 0 50px 0; background:#FBF5E9;">
      <div class="container w-container" style="text-align:center; max-width:850px;">
        <span class="clinic-badge">HELP &bull; POPULAR QUESTIONS</span>
        <h1 class="heading-1 recoleta blue5" style="font-size:44px; margin-bottom:20px;">
          Frequently Asked <span class="highlight highlight--line">Questions</span>
        </h1>
        <p style="font-size:18px; line-height:1.7; color:#4A5568;">
          Find answers regarding our treatments, Dr. Prabhu Rajan's credentials, Dorn method spinal alignment, appointments, and fees.
        </p>
      </div>
    </section>

    <section class="section" style="padding:60px 0;">
      <div class="container container--small w-container">
        
        <div class="faq-accordion">
          <div class="faq-question">Where is the clinic located? <span>+</span></div>
          <div class="faq-answer">Rajan's Physiotherapy &amp; Pain Relief Centre is located at <strong>No. 9 / 29C, 1st Cross Street, Nagappa Nagar / New Colony, Chromepet, Chennai - 600044</strong>, right behind the Chromepet Police Station and Shastri Colony.</div>
        </div>

        <div class="faq-accordion">
          <div class="faq-question">What are the clinic working hours? <span>+</span></div>
          <div class="faq-answer"><strong>Monday &ndash; Friday:</strong> 9:30 AM &ndash; 2:00 PM and 4:00 PM &ndash; 8:30 PM.<br><strong>Saturday:</strong> 9:00 AM &ndash; 5:00 PM.<br><strong>Sunday:</strong> Closed (Holiday / Emergency by appointment).</div>
        </div>

        <div class="faq-accordion">
          <div class="faq-question">What is the consultation fee? <span>+</span></div>
          <div class="faq-answer">The initial detailed consultation fee is <strong>₹600</strong>, which includes a comprehensive physical examination, spinal alignment review, and customized treatment planning. Subsequent session fees depend on the specific therapy modalities chosen.</div>
        </div>

        <div class="faq-accordion">
          <div class="faq-question">What is the Dorn Method and is it safe? <span>+</span></div>
          <div class="faq-answer">The Dorn Method is a gentle, dynamic vertebrae realignment technique originating in Germany. Unlike traditional aggressive chiropractic cracking, Dorn therapy uses natural patient movement to guide vertebrae and joints back into their natural alignment safely. It is 100% surgery-free and gentle. Dr. Prabhu Rajan is the Vice Chairman of the All India Dorn Therapy Association (AIDTA).</div>
        </div>

        <div class="faq-accordion">
          <div class="faq-question">Do I need an X-ray or MRI before consulting? <span>+</span></div>
          <div class="faq-answer">No, an MRI or X-ray is not mandatory before your first visit. Dr. Prabhu Rajan performs detailed physical palpation and orthopedic tests to identify the root cause. If you already have previous scans, please bring them along.</div>
        </div>

        <div class="faq-accordion">
          <div class="faq-question">Are home physiotherapy visits available? <span>+</span></div>
          <div class="faq-answer">Yes, we provide dedicated home physiotherapy services across Chromepet, Pallavaram, Tambaram, Chitlapakkam, and surrounding localities for post-operative, elderly, or severely immobile patients.</div>
        </div>

        <div class="faq-accordion">
          <div class="faq-question">What payment methods are accepted? <span>+</span></div>
          <div class="faq-answer">We accept Cash, Google Pay (GPay), PhonePe, and all standard UPI apps. Receipts are provided for medical insurance reimbursement documentation.</div>
        </div>

      </div>
    </section>
  </main>
  {get_footer(depth_prefix)}"""

# ----------------- PAIN CHECKER PAGE -----------------
def generate_checker_html(depth_prefix):
    asset_prefix = f"{depth_prefix}assets/" if depth_prefix else "assets/"
    return f"""{get_head("Free Pain Assessment & Symptom Checker | Rajan's Physiotherapy", "Answer 4 simple questions about your pain and get a personalized consultation recommendation with Dr. Prabhu Rajan on WhatsApp.", asset_prefix)}
  {get_nav(depth_prefix, "checker")}
  <main>
    <section class="section" style="padding:60px 0 40px 0; background:#FBF5E9;">
      <div class="container w-container" style="text-align:center; max-width:800px;">
        <span class="clinic-badge">PHYSIOTHERAPY SYMPTOM CHECKER</span>
        <h1 class="heading-1 recoleta blue5" style="font-size:40px; margin-bottom:16px;">
          Find the root cause of your <span class="highlight highlight--line">pain.</span>
        </h1>
        <p style="font-size:17px; line-height:1.6; color:#4A5568;">
          Select your symptoms below to get an instant clinical assessment and send your details directly to Dr. Prabhu Rajan on WhatsApp for immediate guidance.
        </p>
      </div>
    </section>

    <section class="section" style="padding:40px 0 80px 0;">
      <div class="container container--small w-container">
        <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:24px; padding:36px; box-shadow:0 8px 30px rgba(0,0,0,0.05);">
          
          <form id="painAssessmentForm">
            <!-- QUESTION 1 -->
            <div style="margin-bottom:30px;">
              <h3 style="font-family:'Recoleta',serif; font-size:20px; color:#19535F; margin-bottom:12px;">1. Where is your pain located?</h3>
              <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px;">
                <label class="checker-option"><input type="radio" name="pain_location" value="Lower Back / Sciatica" checked> <span>Lower Back / Sciatica</span></label>
                <label class="checker-option"><input type="radio" name="pain_location" value="Neck / Cervical Spondylitis"> <span>Neck / Cervical Pain</span></label>
                <label class="checker-option"><input type="radio" name="pain_location" value="Knee Joint / Ligament"> <span>Knee Joint / Ligament</span></label>
                <label class="checker-option"><input type="radio" name="pain_location" value="Shoulder / Frozen Shoulder"> <span>Frozen Shoulder / Arm</span></label>
                <label class="checker-option"><input type="radio" name="pain_location" value="Heel / Plantar Fasciitis"> <span>Heel / Plantar Fasciitis</span></label>
                <label class="checker-option"><input type="radio" name="pain_location" value="Sports Injury / Other"> <span>Sports Injury / Other</span></label>
              </div>
            </div>

            <!-- QUESTION 2 -->
            <div style="margin-bottom:30px;">
              <h3 style="font-family:'Recoleta',serif; font-size:20px; color:#19535F; margin-bottom:12px;">2. How long have you experienced this pain?</h3>
              <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:10px;">
                <label class="checker-option"><input type="radio" name="pain_duration" value="Less than 2 weeks" checked> <span>Less than 2 weeks</span></label>
                <label class="checker-option"><input type="radio" name="pain_duration" value="1 to 6 months"> <span>1 &ndash; 6 months</span></label>
                <label class="checker-option"><input type="radio" name="pain_duration" value="Over 1 year"> <span>Over 1 year</span></label>
                <label class="checker-option"><input type="radio" name="pain_duration" value="Chronic (Multiple years)"> <span>Chronic (Several years)</span></label>
              </div>
            </div>

            <!-- QUESTION 3 -->
            <div style="margin-bottom:30px;">
              <h3 style="font-family:'Recoleta',serif; font-size:20px; color:#19535F; margin-bottom:12px;">3. Your Name &amp; Contact Number</h3>
              <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
                <input type="text" id="patientName" placeholder="Your Name" required style="width:100%; padding:14px; border:1px solid #CBD5E0; border-radius:10px; font-size:15px;"/>
                <input type="tel" id="patientPhone" placeholder="Mobile Number" required style="width:100%; padding:14px; border:1px solid #CBD5E0; border-radius:10px; font-size:15px;"/>
              </div>
            </div>

            <button type="button" onclick="submitAssessment()" class="button w-button" style="width:100%; background:#25D366; border:none; padding:16px; font-size:17px; font-weight:700; display:flex; align-items:center; justify-content:center; gap:10px;">
              <span>💬 Send to Dr. Prabhu on WhatsApp &rarr;</span>
            </button>
          </form>

        </div>
      </div>
    </section>
  </main>
  
  <script>
    function submitAssessment() {{
      var loc = document.querySelector('input[name="pain_location"]:checked').value;
      var dur = document.querySelector('input[name="pain_duration"]:checked').value;
      var name = document.getElementById('patientName').value.trim() || 'Patient';
      var phone = document.getElementById('patientPhone').value.trim() || 'Not provided';
      
      var msg = "Hello Dr. Prabhu Rajan,%0A%0AI completed the online pain assessment:%0A" +
                "👤 Name: " + encodeURIComponent(name) + "%0A" +
                "📞 Phone: " + encodeURIComponent(phone) + "%0A" +
                "📍 Pain Location: " + encodeURIComponent(loc) + "%0A" +
                "⏱️ Duration: " + encodeURIComponent(dur) + "%0A%0A" +
                "I would like to book a consultation at Rajan's Physiotherapy Centre.";
      
      window.open("https://wa.me/919042612895?text=" + msg, "_blank");
    }}
  </script>
  {get_footer(depth_prefix)}"""

# Generate and write all files
pages = {
    'about': generate_about_html,
    'pricing': generate_pricing_html,
    'faq': generate_faq_html,
    'free-assessment': generate_checker_html
}

for page_name, generator in pages.items():
    # 1. Root page, e.g. about.html
    root_file = os.path.join(ROOT_DIR, f"{page_name}.html")
    with open(root_file, 'w', encoding='utf-8') as f:
        f.write(generator(''))
    print(f"Generated {page_name}.html")

    # 2. Subfolder page, e.g. about/index.html
    sub_dir = os.path.join(ROOT_DIR, page_name)
    os.makedirs(sub_dir, exist_ok=True)
    sub_file = os.path.join(sub_dir, 'index.html')
    with open(sub_file, 'w', encoding='utf-8') as f:
        f.write(generator('../'))
    print(f"Generated {page_name}/index.html")

print("All primary pages updated successfully.")
