import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Clean inline SVGs (no emojis)
SVG_CHECK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#19535F" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><polyline points="20 6 9 17 4 12"></polyline></svg>'
SVG_PHONE = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>'
SVG_WHATSAPP = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="flex-shrink:0;"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19.01L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67M9.53 7.32C9.36 7.32 9.09 7.38 8.86 7.63C8.63 7.88 7.98 8.49 7.98 9.73C7.98 10.97 8.88 12.17 9.01 12.34C9.14 12.51 10.77 15.02 13.27 16.1C13.86 16.36 14.33 16.51 14.68 16.62C15.28 16.82 15.82 16.79 16.26 16.72C16.75 16.65 17.76 16.11 17.97 15.52C18.18 14.93 18.18 14.43 18.11 14.32C18.05 14.21 17.88 14.15 17.62 14.02C17.37 13.89 16.13 13.28 15.9 13.2C15.68 13.11 15.51 13.07 15.34 13.32C15.17 13.57 14.69 14.15 14.55 14.32C14.4 14.48 14.26 14.51 14.01 14.38C13.75 14.25 12.93 13.99 11.96 13.12C11.2 12.44 10.69 11.61 10.54 11.36C10.4 11.11 10.53 10.97 10.66 10.84C10.77 10.73 10.91 10.54 11.05 10.38C11.19 10.21 11.23 10.09 11.32 9.92C11.41 9.75 11.36 9.61 11.3 9.48C11.23 9.36 10.72 8.1 10.51 7.59C10.3 7.09 10.09 7.16 9.93 7.15C9.79 7.14 9.62 7.32 9.53 7.32Z"/></svg>'
SVG_STAR = '<svg width="15" height="15" viewBox="0 0 24 24" fill="#D69E2E" style="flex-shrink:0;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>'
SVG_MAP_PIN = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#19535F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>'
SVG_MAIL = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#19535F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>'
SVG_SHIELD = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#19535F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path><polyline points="9 12 11 14 15 10"></polyline></svg>'
SVG_SPINE = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#19535F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><circle cx="12" cy="4" r="2"></circle><circle cx="12" cy="9" r="2"></circle><circle cx="12" cy="14" r="2"></circle><circle cx="12" cy="19" r="2"></circle><path d="M8 9h8M7 14h10M9 19h6"></path></svg>'
SVG_ACTIVITY = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#19535F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>'
SVG_LASER = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#19535F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>'
SVG_CROSSHAIR = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#19535F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><circle cx="12" cy="12" r="10"></circle><line x1="22" y1="12" x2="18" y2="12"></line><line x1="6" y1="12" x2="2" y2="12"></line><line x1="12" y1="6" x2="12" y2="2"></line><line x1="12" y1="22" x2="12" y2="18"></line></svg>'
SVG_HOME = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#19535F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>'
SVG_HEART = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#19535F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>'
SVG_CALENDAR = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>'

def generate_homepage_html(depth_prefix=''):
    asset_prefix = f"{depth_prefix}assets/" if depth_prefix else "assets/"

    stars_html = "".join([SVG_STAR for _ in range(5)])

    html = f"""<!DOCTYPE html>
<html data-wf-domain="rajansphysio.com" data-wf-page="home" lang="en">
<head>
  <meta charset="utf-8"/>
  <title>Rajan's Physiotherapy &amp; Pain Relief Centre | Chromepet, Chennai (Since 2009)</title>
  <meta content="Rajan's Physiotherapy &amp; Pain Relief Centre in Chromepet, Chennai. Established 2009. Led by Dr. Prabhu Rajan, PT (17 Yrs Exp, MPT Sports, MIAP). Dorn method spinal alignment, advanced laser &amp; shockwave therapy." name="description"/>
  <meta content="Rajan's Physiotherapy &amp; Pain Relief Centre | Chromepet, Chennai" property="og:title"/>
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
    .hero-doctor-badge {{
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(8px);
      box-shadow: 0 10px 25px -5px rgba(25, 83, 95, 0.15);
      border-radius: 16px;
      padding: 14px 20px;
      position: absolute;
      bottom: 24px;
      left: -20px;
      display: flex;
      align-items: center;
      gap: 12px;
      z-index: 10;
    }}
    .service-card {{
      background: #FFFFFF;
      border-radius: 20px;
      padding: 30px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.04);
      transition: all 0.3s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border: 1px solid #EEF2F4;
    }}
    .service-card:hover {{
      transform: translateY(-5px);
      box-shadow: 0 14px 32px rgba(25, 83, 95, 0.12);
      border-color: #19535F;
    }}
    .clinic-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 16px;
      border-radius: 30px;
      font-size: 13px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      background: #E8F1F2;
      color: #19535F;
      margin-bottom: 16px;
    }}
    .bento-card {{
      background: #FFFFFF;
      border-radius: 20px;
      padding: 32px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.04);
      border: 1px solid #EEF2F4;
      transition: all 0.3s ease;
    }}
    .bento-card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 12px 28px rgba(25,83,95,0.1);
    }}
    .photo-card {{
      border-radius: 18px;
      overflow: hidden;
      box-shadow: 0 4px 18px rgba(0,0,0,0.06);
      background: #FFFFFF;
      transition: transform 0.3s ease;
    }}
    .photo-card:hover {{
      transform: translateY(-4px);
    }}
    .vs-card {{
      border-radius: 20px;
      padding: 36px;
      height: 100%;
    }}
    .nav-btn {{
      transition: all 0.2s ease;
    }}
    .nav-btn:hover {{
      opacity: 0.92;
      transform: translateY(-1px);
    }}
  </style>
</head>
<body>

  <!-- HEADER -->
  <header>
    <div data-animation="default" data-collapse="medium" data-duration="400" data-easing="ease" data-easing2="ease" role="banner" class="navbar w-nav">
      <div class="container container--navbar w-container" style="display:flex; justify-content:space-between; align-items:center;">
        
        <!-- LOGO -->
        <a href="{depth_prefix or './'}" title="Rajan's Physiotherapy &amp; Pain Relief Centre" class="brand w-nav-brand w--current" style="text-decoration:none; display:flex; align-items:center; gap:12px;">
          <div style="width:44px; height:44px; border-radius:50%; background:#19535F; color:#FBF5E9; display:flex; align-items:center; justify-content:center; font-family:'Recoleta',serif; font-size:24px; font-weight:700; box-shadow:0 3px 8px rgba(25,83,95,0.25);">R</div>
          <div style="display:flex; flex-direction:column;">
            <span style="font-family:'Recoleta',serif; font-size:20px; font-weight:700; color:#19535F; line-height:1.15;">Rajan's Physiotherapy</span>
            <span style="font-size:11px; letter-spacing:0.8px; color:#5A6E72; text-transform:uppercase; font-weight:600;">&amp; Pain Relief Centre &bull; Since 2009</span>
          </div>
        </a>

        <!-- NAV LINKS -->
        <nav role="navigation" class="nav-menu w-nav-menu" style="display:flex; align-items:center;">
          <a href="{depth_prefix or './'}" class="nav__link w-nav-link w--current">Home</a>
          <a href="{depth_prefix}about.html" class="nav__link w-nav-link">About Us</a>
          <a href="#specialties" class="nav__link w-nav-link">Specialties</a>
          <a href="#modalities" class="nav__link w-nav-link">Treatments</a>
          <a href="{depth_prefix}pricing.html" class="nav__link w-nav-link">Pricing &amp; Fees</a>
          <a href="{depth_prefix}faq.html" class="nav__link w-nav-link">FAQ</a>
          <a href="{depth_prefix}free-assessment.html" class="nav__link w-nav-link">Pain Checker</a>
          <a href="tel:9042612895" class="button w-button nav-btn" style="margin-left:14px; background:#19535F; padding:10px 20px; font-size:14px; display:inline-flex; align-items:center; gap:8px;">
            {SVG_PHONE} <span>90426 12895</span>
          </a>
        </nav>

        <div class="menu-button w-nav-button">
          <div class="icon w-icon-nav-menu"></div>
        </div>
      </div>
    </div>
  </header>

  <main>
    <!-- HERO SECTION -->
    <div class="fold-home">
      <div class="container w-container">
        <div class="flex-fold" style="align-items:center;">
          
          <div class="fold__content">
            <span class="clinic-badge">
              {SVG_SHIELD}
              <span>17+ Years Experience &bull; Est. 2009 &bull; Chromepet, Chennai</span>
            </span>
            <h1 class="heading-1 recoleta blue5" style="line-height:1.15; margin-bottom:20px;">
              Pain-free living starts <span class="highlight highlight--line">here.</span>
            </h1>
            <p class="fold__subtitle blue5" style="font-size:18px; line-height:1.6; margin-bottom:28px;">
              Personalized, evidence-informed physiotherapy and rehabilitation in Chromepet, Chennai. Led by <strong>Dr. Prabhu Rajan, PT</strong> (Master in Sports Physio, MIAP L-27944).
            </p>
            
            <ul class="fold_list w-list-unstyled" role="list" style="margin-bottom:32px;">
              <li class="fold__list-item" style="margin-bottom:12px; display:flex; align-items:center; gap:12px;">
                {SVG_CHECK}
                <p class="blue5" style="font-size:16px; margin:0;"><strong>Dorn Method Spinal Alignment &amp; Manual Therapy</strong> (Gentle, non-invasive, no cracking)</p>
              </li>
              <li class="fold__list-item" style="margin-bottom:12px; display:flex; align-items:center; gap:12px;">
                {SVG_CHECK}
                <p class="blue5" style="font-size:16px; margin:0;"><strong>Advanced Scanning Laser &amp; Radial Shockwave</strong> for chronic tendinitis &amp; disc issues</p>
              </li>
              <li class="fold__list-item" style="margin-bottom:12px; display:flex; align-items:center; gap:12px;">
                {SVG_CHECK}
                <p class="blue5" style="font-size:16px; margin:0;"><strong>99% Recommendation Score</strong> on Practo &bull; 4.9 out of 5 Stars on Justdial (730+ reviews)</p>
              </li>
              <li class="fold__list-item" style="display:flex; align-items:center; gap:12px;">
                {SVG_CHECK}
                <p class="blue5" style="font-size:16px; margin:0;"><strong>Dedicated Home Physiotherapy Visits</strong> available across Chromepet &amp; suburbs</p>
              </li>
            </ul>

            <div style="display:flex; flex-wrap:wrap; gap:16px; align-items:center;">
              <a class="button w-button nav-btn" href="https://wa.me/919042612895?text=Hello%20Dr.%20Prabhu%2C%20I%20would%20like%20to%20book%20a%20physiotherapy%20consultation" target="_blank" style="background:#25D366; border:none; padding:14px 28px; font-size:16px; font-weight:600; display:inline-flex; align-items:center; gap:10px;">
                {SVG_WHATSAPP}
                <span>Book on WhatsApp</span>
              </a>
              <a class="button button--secondary w-button nav-btn" href="tel:9042612895" style="padding:14px 24px; font-size:16px; display:inline-flex; align-items:center; gap:10px;">
                {SVG_PHONE}
                <span>Call: 90426 12895</span>
              </a>
            </div>
          </div>

          <div class="fold__images" style="position:relative;">
            <div style="position:relative; width:100%; max-width:440px; margin:0 auto;">
              <img alt="Dr. Prabhu Rajan PT - Chief Physiotherapist" src="{asset_prefix}images/dr_prabhu_rajan_profile.jpg" style="width:100%; height:auto; border-radius:24px; box-shadow:0 20px 40px rgba(25, 83, 95, 0.2); object-fit:cover; aspect-ratio:4/5;"/>
              
              <div class="hero-doctor-badge">
                <div style="background:#25D366; width:12px; height:12px; border-radius:50%; flex-shrink:0;"></div>
                <div>
                  <h4 style="font-size:14px; font-weight:700; color:#19535F; margin:0;">Dr. Prabhu Rajan, PT</h4>
                  <p style="font-size:12px; color:#4A5568; margin:0;">BPT, MPT (Sports), Dr.Acu, MIAP L-27944</p>
                  <div style="display:flex; align-items:center; gap:4px; margin-top:2px;">
                    {stars_html}
                    <span style="font-size:11px; color:#D69E2E; font-weight:700; margin-left:4px;">99% Recommended (513+ Reviews)</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>

    <!-- STATS BANNER -->
    <section class="section section--blue4 section--less-top-margin" style="padding:40px 0;">
      <div class="container w-container">
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:24px; text-align:center;">
          <div>
            <div style="font-family:'Recoleta',serif; font-size:42px; font-weight:700; color:#FBF5E9;">17+</div>
            <p style="color:#FBF5E9; opacity:0.85; font-size:15px; margin:0;">Years Clinical Excellence</p>
          </div>
          <div>
            <div style="font-family:'Recoleta',serif; font-size:42px; font-weight:700; color:#FBF5E9;">15,000+</div>
            <p style="color:#FBF5E9; opacity:0.85; font-size:15px; margin:0;">Successful Treatments</p>
          </div>
          <div>
            <div style="font-family:'Recoleta',serif; font-size:42px; font-weight:700; color:#FBF5E9;">99%</div>
            <p style="color:#FBF5E9; opacity:0.85; font-size:15px; margin:0;">Practo Positive Score</p>
          </div>
          <div>
            <div style="font-family:'Recoleta',serif; font-size:42px; font-weight:700; color:#FBF5E9;">₹600</div>
            <p style="color:#FBF5E9; opacity:0.85; font-size:15px; margin:0;">Initial Consultation Fee</p>
          </div>
        </div>
      </div>
    </section>

    <!-- NEW SECTION 1: CONDITIONS & CLINICAL SPECIALTIES -->
    <section id="specialties" class="section" style="padding:80px 0; background:#FAF6EE;">
      <div class="container w-container">
        <div class="section__header" style="text-align:center; max-width:760px; margin:0 auto 60px auto;">
          <p class="uppercase blue4" style="letter-spacing:1px; font-weight:700;">CONDITIONS WE TREAT</p>
          <h2 class="heading-2 recoleta" style="font-size:38px;">
            Targeted relief for complex <span class="highlight highlight--circle">conditions.</span>
          </h2>
          <p style="font-size:17px; line-height:1.6; color:#4A5568; margin-top:16px;">
            We diagnose and treat the precise neuromuscular and skeletal origins of your discomfort through advanced manual therapy and cutting-edge modalities.
          </p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(270px, 1fr)); gap:24px;">
          
          <!-- BENTO 1: SPINE & BACK -->
          <div class="bento-card">
            <div style="width:48px; height:48px; border-radius:12px; background:#E8F1F2; display:flex; align-items:center; justify-content:center; margin-bottom:20px;">
              {SVG_SPINE}
            </div>
            <h3 style="font-family:'Recoleta',serif; font-size:22px; color:#19535F; margin-bottom:12px;">Spine, Neck &amp; Disc Care</h3>
            <ul style="list-style:none; padding:0; margin:0; line-height:2; font-size:14px; color:#4A5568;">
              <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Cervical Spondylitis &amp; Neck Pain</li>
              <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} L3-L4 / L4-L5 / L5-S1 Disc Bulge</li>
              <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Sciatica &amp; Radiating Leg Pain</li>
              <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Postural Scoliosis &amp; Kyphosis</li>
            </ul>
          </div>

          <!-- BENTO 2: JOINTS & SHOULDERS -->
          <div class="bento-card">
            <div style="width:48px; height:48px; border-radius:12px; background:#E8F1F2; display:flex; align-items:center; justify-content:center; margin-bottom:20px;">
              {SVG_ACTIVITY}
            </div>
            <h3 style="font-family:'Recoleta',serif; font-size:22px; color:#19535F; margin-bottom:12px;">Joint &amp; Shoulder Pain</h3>
            <ul style="list-style:none; padding:0; margin:0; line-height:2; font-size:14px; color:#4A5568;">
              <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Frozen Shoulder (Adhesive Capsulitis)</li>
              <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Rotator Cuff Tendon Strain</li>
              <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Tennis Elbow &amp; Golfer's Elbow</li>
              <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Carpal Tunnel &amp; Wrist Pain</li>
            </ul>
          </div>

          <!-- BENTO 3: KNEE & FOOT -->
          <div class="bento-card">
            <div style="width:48px; height:48px; border-radius:12px; background:#E8F1F2; display:flex; align-items:center; justify-content:center; margin-bottom:20px;">
              {SVG_CROSSHAIR}
            </div>
            <h3 style="font-family:'Recoleta',serif; font-size:22px; color:#19535F; margin-bottom:12px;">Knee, Foot &amp; Heel Pain</h3>
            <ul style="list-style:none; padding:0; margin:0; line-height:2; font-size:14px; color:#4A5568;">
              <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Knee Osteoarthritis (Grade 1 to 4)</li>
              <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} ACL, PCL &amp; Meniscus Ligament Tears</li>
              <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Plantar Fasciitis &amp; Calcaneal Spurs</li>
              <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Recurrent Ankle Sprains</li>
            </ul>
          </div>

          <!-- BENTO 4: REHAB & SURGERY RECOVERY -->
          <div class="bento-card">
            <div style="width:48px; height:48px; border-radius:12px; background:#E8F1F2; display:flex; align-items:center; justify-content:center; margin-bottom:20px;">
              {SVG_HEART}
            </div>
            <h3 style="font-family:'Recoleta',serif; font-size:22px; color:#19535F; margin-bottom:12px;">Sports &amp; Post-Surgical</h3>
            <ul style="list-style:none; padding:0; margin:0; line-height:2; font-size:14px; color:#4A5568;">
              <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Knee Replacement (TKR) Rehabilitation</li>
              <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Hip Replacement (THR) Recovery</li>
              <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Post-Fracture Joint Stiffness</li>
              <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Athletic Muscle Tears &amp; Sprains</li>
            </ul>
          </div>

        </div>
      </div>
    </section>

    <!-- NEW SECTION 2: COMPLETE TREATMENT MODALITIES ARSENAL -->
    <section id="modalities" class="section" style="padding:80px 0;">
      <div class="container w-container">
        <div class="section__header" style="text-align:center; max-width:760px; margin:0 auto 60px auto;">
          <p class="uppercase blue4" style="letter-spacing:1px; font-weight:700;">ADVANCED TREATMENT ARSENAL</p>
          <h2 class="heading-2 recoleta" style="font-size:38px;">
            Evidence-informed therapies for <span class="highlight highlight--line">rapid healing.</span>
          </h2>
          <p style="font-size:17px; line-height:1.6; color:#4A5568; margin-top:16px;">
            Our treatment approach integrates hands-on therapeutic expertise with specialized radiofrequency, acoustic shockwave, and scanning laser technology.
          </p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:32px;">
          
          <div class="service-card">
            <div>
              <div style="width:48px; height:48px; border-radius:12px; background:#E8F1F2; display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
                {SVG_LASER}
              </div>
              <h3 style="font-family:'Recoleta',serif; font-size:22px; color:#19535F; margin-bottom:10px;">LASERSTIM Scanning Laser</h3>
              <p style="color:#4A5568; line-height:1.6; font-size:15px;">
                High-intensity therapeutic laser that delivers photons deep into damaged soft tissues, accelerating ATP cellular repair, clearing inflammatory cytokines, and relieving stubborn chronic pain.
              </p>
            </div>
            <div style="margin-top:20px; padding-top:14px; border-top:1px solid #EEF2F4; font-size:13px; font-weight:600; color:#19535F;">
              Best for: Tendinitis, Ligaments, Disc Bulge
            </div>
          </div>

          <div class="service-card">
            <div>
              <div style="width:48px; height:48px; border-radius:12px; background:#E8F1F2; display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
                {SVG_ACTIVITY}
              </div>
              <h3 style="font-family:'Recoleta',serif; font-size:22px; color:#19535F; margin-bottom:10px;">Radial Shockwave Therapy</h3>
              <p style="color:#4A5568; line-height:1.6; font-size:15px;">
                Extracorporeal acoustic pressure waves that dissolve calcifications in soft tissues, stimulate neo-vascularization, and release deep fibrotic adhesions in chronic musculoskeletal conditions.
              </p>
            </div>
            <div style="margin-top:20px; padding-top:14px; border-top:1px solid #EEF2F4; font-size:13px; font-weight:600; color:#19535F;">
              Best for: Heel Spurs, Plantar Fasciitis, Tennis Elbow
            </div>
          </div>

          <div class="service-card">
            <div>
              <div style="width:48px; height:48px; border-radius:12px; background:#E8F1F2; display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
                {SVG_SPINE}
              </div>
              <h3 style="font-family:'Recoleta',serif; font-size:22px; color:#19535F; margin-bottom:10px;">Dorn Spinal Alignment</h3>
              <p style="color:#4A5568; line-height:1.6; font-size:15px;">
                A gentle, non-invasive German vertebral realignment technique. Utilizes active patient movement to safely guide vertebrae back into position without forceful cracking or surgery.
              </p>
            </div>
            <div style="margin-top:20px; padding-top:14px; border-top:1px solid #EEF2F4; font-size:13px; font-weight:600; color:#19535F;">
              Led by: Vice Chairman AIDTA Certified
            </div>
          </div>

          <div class="service-card">
            <div>
              <div style="width:48px; height:48px; border-radius:12px; background:#E8F1F2; display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
                {SVG_CROSSHAIR}
              </div>
              <h3 style="font-family:'Recoleta',serif; font-size:22px; color:#19535F; margin-bottom:10px;">Clinical Dry Needling (CDNT USA)</h3>
              <p style="color:#4A5568; line-height:1.6; font-size:15px;">
                Fine filament needles target taut neuromuscular trigger points to stimulate immediate muscular release, restore normal biochemical balance, and eliminate referred nerve symptoms.
              </p>
            </div>
            <div style="margin-top:20px; padding-top:14px; border-top:1px solid #EEF2F4; font-size:13px; font-weight:600; color:#19535F;">
              Certified: American CDNT Trained
            </div>
          </div>

          <div class="service-card">
            <div>
              <div style="width:48px; height:48px; border-radius:12px; background:#E8F1F2; display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
                {SVG_HEART}
              </div>
              <h3 style="font-family:'Recoleta',serif; font-size:22px; color:#19535F; margin-bottom:10px;">TECAR Radiofrequency Therapy</h3>
              <p style="color:#4A5568; line-height:1.6; font-size:15px;">
                Capacitive and resistive radiofrequency diathermy that delivers deep cellular thermal energy, relaxes severe muscle spasms, and dramatically increases microcirculation for faster healing.
              </p>
            </div>
            <div style="margin-top:20px; padding-top:14px; border-top:1px solid #EEF2F4; font-size:13px; font-weight:600; color:#19535F;">
              Best for: Muscle Tears, Spasms, Sports Injuries
            </div>
          </div>

          <div class="service-card">
            <div>
              <div style="width:48px; height:48px; border-radius:12px; background:#E8F1F2; display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
                {SVG_SHIELD}
              </div>
              <h3 style="font-family:'Recoleta',serif; font-size:22px; color:#19535F; margin-bottom:10px;">Kinesio Cupping &amp; IASTM</h3>
              <p style="color:#4A5568; line-height:1.6; font-size:15px;">
                Decompressive negative-pressure myofascial cupping paired with Instrument-Assisted Soft Tissue Mobilization (IASTM) to break down restrictive scar tissue and improve lymphatic flow.
              </p>
            </div>
            <div style="margin-top:20px; padding-top:14px; border-top:1px solid #EEF2F4; font-size:13px; font-weight:600; color:#19535F;">
              Best for: Fascial Restrictions &amp; Chronic Tightness
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- NEW SECTION 3: THE RAJAN'S DIFFERENCE (ROOT-CAUSE VS CONVENTIONAL) -->
    <section class="section" style="padding:80px 0; background:#FAF6EE;">
      <div class="container w-container">
        <div class="section__header" style="text-align:center; max-width:760px; margin:0 auto 60px auto;">
          <p class="uppercase blue4" style="letter-spacing:1px; font-weight:700;">THE RAJAN'S DIFFERENCE</p>
          <h2 class="heading-2 recoleta" style="font-size:38px;">
            Root-cause healing vs. <span class="highlight highlight--line">temporary symptom masking.</span>
          </h2>
          <p style="font-size:17px; line-height:1.6; color:#4A5568; margin-top:16px;">
            Here is why over 15,000 patients have trusted Dr. Prabhu Rajan since 2009 instead of living on endless medication or undergoing unnecessary surgery.
          </p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:32px;">
          
          <!-- CONVENTIONAL -->
          <div class="vs-card" style="background:#FFFFFF; border:1px solid #E2E8F0; box-shadow:0 4px 20px rgba(0,0,0,0.03);">
            <div style="color:#E53E3E; font-weight:700; text-transform:uppercase; font-size:13px; letter-spacing:0.8px; margin-bottom:12px;">Standard Conventional Care</div>
            <h3 style="font-family:'Recoleta',serif; font-size:24px; color:#2D3748; margin-bottom:20px;">Temporary Masking</h3>
            <ul style="list-style:none; padding:0; margin:0; line-height:2.2; font-size:15px; color:#718096;">
              <li style="display:flex; align-items:flex-start; gap:10px;">
                <span style="color:#E53E3E; font-weight:700;">&times;</span>
                <span>Painkillers and anti-inflammatory pills that only numb symptoms temporarily</span>
              </li>
              <li style="display:flex; align-items:flex-start; gap:10px;">
                <span style="color:#E53E3E; font-weight:700;">&times;</span>
                <span>Advice to wear lifelong neck collars or lumbar belts that weaken muscles</span>
              </li>
              <li style="display:flex; align-items:flex-start; gap:10px;">
                <span style="color:#E53E3E; font-weight:700;">&times;</span>
                <span>Premature surgical recommendations for common disc bulges</span>
              </li>
              <li style="display:flex; align-items:flex-start; gap:10px;">
                <span style="color:#E53E3E; font-weight:700;">&times;</span>
                <span>Pain recurs as soon as medication wears off</span>
              </li>
            </ul>
          </div>

          <!-- RAJAN'S -->
          <div class="vs-card" style="background:#19535F; color:#FBF5E9; border:2px solid #19535F; box-shadow:0 12px 32px rgba(25,83,95,0.2);">
            <div style="color:#9AE6B4; font-weight:700; text-transform:uppercase; font-size:13px; letter-spacing:0.8px; margin-bottom:12px;">Rajan's Physiotherapy Protocol</div>
            <h3 style="font-family:'Recoleta',serif; font-size:24px; color:#FBF5E9; margin-bottom:20px;">Permanent Root-Cause Recovery</h3>
            <ul style="list-style:none; padding:0; margin:0; line-height:2.2; font-size:15px; color:#FBF5E9; opacity:0.95;">
              <li style="display:flex; align-items:flex-start; gap:10px;">
                <span style="color:#9AE6B4; font-weight:700;">&check;</span>
                <span>Tactile physical assessment identifying exact joint subluxation and muscle knots</span>
              </li>
              <li style="display:flex; align-items:flex-start; gap:10px;">
                <span style="color:#9AE6B4; font-weight:700;">&check;</span>
                <span>Gentle Dorn Method vertebrae realignment without cracking or surgery</span>
              </li>
              <li style="display:flex; align-items:flex-start; gap:10px;">
                <span style="color:#9AE6B4; font-weight:700;">&check;</span>
                <span>Scanning laser &amp; radial shockwave stimulating biological tissue repair</span>
              </li>
              <li style="display:flex; align-items:flex-start; gap:10px;">
                <span style="color:#9AE6B4; font-weight:700;">&check;</span>
                <span>Targeted active strengthening exercises preventing future pain recurrence</span>
              </li>
            </ul>
          </div>

        </div>
      </div>
    </section>

    <!-- NEW SECTION 4: HOME PHYSIOTHERAPY VISITS PROGRAM -->
    <section class="section" style="padding:80px 0;">
      <div class="container w-container">
        <div style="background:#E8F1F2; border-radius:28px; padding:50px 40px; display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:40px; align-items:center;">
          <div>
            <span class="clinic-badge" style="background:#FFF;">
              {SVG_HOME}
              <span>HOME VISIT PROGRAM &bull; CHROMEPET &amp; SURROUNDING AREAS</span>
            </span>
            <h3 class="heading-3 recoleta" style="font-size:36px; color:#19535F; margin:14px 0 16px 0;">
              Expert physiotherapy delivered directly to your doorstep.
            </h3>
            <p style="font-size:16px; line-height:1.7; color:#4A5568; margin-bottom:24px;">
              For elderly family members, patients recovering from recent joint replacements, stroke, fractures, or severe back spasms who cannot travel to the clinic, we provide comprehensive in-home rehabilitation.
            </p>
            
            <ul style="list-style:none; padding:0; margin:0 0 28px 0; line-height:2.2; font-size:15px; color:#19535F;">
              <li style="display:flex; align-items:center; gap:10px;">{SVG_CHECK} Post-Knee Replacement (TKR) &amp; Hip Surgery Rehabilitation</li>
              <li style="display:flex; align-items:center; gap:10px;">{SVG_CHECK} Stroke Mobility Recovery, Balance &amp; Gait Retraining</li>
              <li style="display:flex; align-items:center; gap:10px;">{SVG_CHECK} Post-Fracture Joint Mobilization &amp; Fall Prevention for Seniors</li>
              <li style="display:flex; align-items:center; gap:10px;">{SVG_CHECK} Servicing Chromepet, Pallavaram, Tambaram, Chitlapakkam &amp; suburbs</li>
            </ul>

            <div style="display:flex; flex-wrap:wrap; gap:14px;">
              <a class="button w-button nav-btn" href="https://wa.me/919042612895?text=Hello%20Dr.%20Prabhu%2C%20I%20would%20like%20to%20enquire%20about%20Home%20Physiotherapy%20visits" target="_blank" style="background:#25D366; font-size:15px; padding:12px 24px; font-weight:600; display:inline-flex; align-items:center; gap:8px;">
                {SVG_WHATSAPP}
                <span>Enquire Home Visit on WhatsApp</span>
              </a>
              <a class="button button--secondary w-button nav-btn" href="tel:9042612895" style="font-size:15px; padding:12px 20px; display:inline-flex; align-items:center; gap:8px;">
                {SVG_PHONE}
                <span>Call: 90426 12895</span>
              </a>
            </div>
          </div>

          <div style="text-align:center;">
            <img src="{asset_prefix}images/clinic_entrance.jpg" alt="Rajan's Clinic Entrance" style="width:100%; max-width:440px; border-radius:20px; box-shadow:0 12px 28px rgba(25,83,95,0.15); margin:0 auto;"/>
            <p style="font-size:13px; color:#5A6E72; margin-top:10px;">Clinic Base: No. 9 / 29C, 1st Cross St, Nagappa Nagar, Chromepet</p>
          </div>
        </div>
      </div>
    </section>

    <!-- NEW SECTION 5: CLINIC PHOTO TOUR & ENVIRONMENT -->
    <section class="section" style="padding:80px 0; background:#FAF6EE;">
      <div class="container w-container">
        <div class="section__header" style="text-align:center; max-width:760px; margin:0 auto 50px auto;">
          <p class="uppercase blue4" style="letter-spacing:1px; font-weight:700;">OUR CLINICAL ENVIRONMENT</p>
          <h2 class="heading-2 recoleta" style="font-size:38px;">
            Take a look inside our <span class="highlight highlight--line">healing center.</span>
          </h2>
          <p style="font-size:17px; line-height:1.6; color:#4A5568; margin-top:14px;">
            A dedicated, hygienic, and fully equipped physiotherapy facility designed for patient comfort, personal privacy, and comprehensive recovery.
          </p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:24px;">
          
          <div class="photo-card">
            <img src="{asset_prefix}images/clinic_photo_banner_1.jpg" alt="Clinic Exterior Street View" style="width:100%; height:230px; object-fit:cover;"/>
            <div style="padding:20px;">
              <h4 style="font-family:'Recoleta',serif; font-size:18px; color:#19535F; margin:0 0 6px 0;">Exterior Street View &amp; Signboard</h4>
              <p style="font-size:13px; color:#718096; margin:0; line-height:1.5;">Main building facade with prominent clinic signage behind Chromepet Police Station.</p>
            </div>
          </div>

          <div class="photo-card">
            <img src="{asset_prefix}images/clinic_treatment_room_1.jpg" alt="Consultation Room &amp; Spine Model" style="width:100%; height:230px; object-fit:cover;"/>
            <div style="padding:20px;">
              <h4 style="font-family:'Recoleta',serif; font-size:18px; color:#19535F; margin:0 0 6px 0;">Doctor Consultation Room</h4>
              <p style="font-size:13px; color:#718096; margin:0; line-height:1.5;">Spinal anatomy model and diagnostic desk where Dr. Prabhu Rajan conducts initial physical assessments.</p>
            </div>
          </div>

          <div class="photo-card">
            <img src="{asset_prefix}images/clinic_treatment_beds.jpg" alt="LASERSTIM Laser Console" style="width:100%; height:230px; object-fit:cover;"/>
            <div style="padding:20px;">
              <h4 style="font-family:'Recoleta',serif; font-size:18px; color:#19535F; margin:0 0 6px 0;">LASERSTIM Scanning Laser Console</h4>
              <p style="font-size:13px; color:#718096; margin:0; line-height:1.5;">Deep photon absorption laser therapy unit for acute and chronic soft-tissue tendinitis and disc healing.</p>
            </div>
          </div>

          <div class="photo-card">
            <img src="{asset_prefix}images/clinic_therapy_equipment.jpg" alt="Electroson 608 Ultrasound Workstation" style="width:100%; height:230px; object-fit:cover;"/>
            <div style="padding:20px;">
              <h4 style="font-family:'Recoleta',serif; font-size:18px; color:#19535F; margin:0 0 6px 0;">Electrotherapy &amp; Ultrasound Unit</h4>
              <p style="font-size:13px; color:#718096; margin:0; line-height:1.5;">Electroson 608 clinical cart offering Interferential Therapy (IFT), ultrasound, and muscle stimulation.</p>
            </div>
          </div>

          <div class="photo-card">
            <img src="{asset_prefix}images/clinic_interior_reception.jpg" alt="Patient Waiting Lounge" style="width:100%; height:230px; object-fit:cover;"/>
            <div style="padding:20px;">
              <h4 style="font-family:'Recoleta',serif; font-size:18px; color:#19535F; margin:0 0 6px 0;">Patient Reception &amp; Lounge</h4>
              <p style="font-size:13px; color:#718096; margin:0; line-height:1.5;">Comfortable, sanitized waiting area with informative Dorn spinal therapy visual charts.</p>
            </div>
          </div>

          <div class="photo-card">
            <img src="{asset_prefix}images/clinic_consultation_area.jpg" alt="Wall Graphics &amp; Treatment Bays" style="width:100%; height:230px; object-fit:cover;"/>
            <div style="padding:20px;">
              <h4 style="font-family:'Recoleta',serif; font-size:18px; color:#19535F; margin:0 0 6px 0;">Dorn Method Wall Display</h4>
              <p style="font-size:13px; color:#718096; margin:0; line-height:1.5;">Educational displays explaining gentle spinal correction techniques and therapeutic protocols.</p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- REAL PATIENT REVIEWS -->
    <section class="section section--blue2" style="padding:80px 0; background:#19535F; color:#FBF5E9;">
      <div class="container w-container">
        <div class="section__header" style="text-align:center; max-width:760px; margin:0 auto 60px auto;">
          <p class="uppercase" style="letter-spacing:1px; color:#FBF5E9; opacity:0.8; font-weight:700;">VERIFIED PATIENT STORIES</p>
          <h2 class="heading-2 recoleta" style="color:#FBF5E9; font-size:38px;">What our patients say</h2>
          <p style="color:#FBF5E9; opacity:0.9; font-size:16px;">Verified feedback from patients treated at Rajan's Physiotherapy &amp; Pain Relief Centre</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:28px;">
          
          <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.15); border-radius:20px; padding:32px; backdrop-filter:blur(10px);">
            <div style="display:flex; gap:3px; margin-bottom:12px;">{stars_html}</div>
            <p style="font-size:15px; line-height:1.7; opacity:0.95; margin-bottom:20px; font-style:italic;">
              "When I met the Doctor, I was not able to walk properly and while sitting too had severe pain from an old ligament tear. He never asked me to take scans. Just by touching he found out the problem! During the second sitting, I found enormous improvement. Now I am able to climb stairs normally, which I couldn't do for 10 long years!"
            </p>
            <div style="font-weight:700; font-size:15px;">&mdash; Devi.S.P</div>
            <div style="font-size:13px; opacity:0.75;">Knee Ligament Tear &bull; Practo Verified Story</div>
          </div>

          <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.15); border-radius:20px; padding:32px; backdrop-filter:blur(10px);">
            <div style="display:flex; gap:3px; margin-bottom:12px;">{stars_html}</div>
            <p style="font-size:15px; line-height:1.7; opacity:0.95; margin-bottom:20px; font-style:italic;">
              "I have been suffering from L3-L4 disc bulge and cervical spondylitis for 15 years. I consulted orthos, tried ayurveda, but within the first 10 sessions of manual therapy and basic exercises with Dr. Prabhu, my pain subsided completely without any medicines! Highly recommend before wearing back belts for life."
            </p>
            <div style="font-weight:700; font-size:15px;">&mdash; Mrs. Hema</div>
            <div style="font-size:13px; opacity:0.75;">15-Year Disc Bulge &bull; Practo Verified Story</div>
          </div>

          <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.15); border-radius:20px; padding:32px; backdrop-filter:blur(10px);">
            <div style="display:flex; gap:3px; margin-bottom:12px;">{stars_html}</div>
            <p style="font-size:15px; line-height:1.7; opacity:0.95; margin-bottom:20px; font-style:italic;">
              "Dr. Prabhu listened patiently, analysed to identify the root cause, and taught several strengthening exercises which cut the problem at its root. I am deeply thankful that I have had no recurrence of knee pain since!"
            </p>
            <div style="font-weight:700; font-size:15px;">&mdash; Viswapriya</div>
            <div style="font-size:13px; opacity:0.75;">Knee Rehabilitation &bull; Practo Verified Story</div>
          </div>

        </div>
      </div>
    </section>

    <!-- DOCTOR QUOTE & COMMITMENT -->
    <section class="section section--quote" style="padding:80px 0;">
      <div class="container container--medium w-container">
        <div style="display:flex; flex-direction:column; align-items:center; text-align:center;">
          <img src="{asset_prefix}images/dr_prabhu_rajan_avatar.jpg" alt="Dr. Prabhu Rajan" style="width:90px; height:90px; border-radius:50%; border:3px solid #19535F; margin-bottom:20px;"/>
          <h3 class="h3--big recoleta" style="font-size:32px; color:#19535F; max-width:800px; line-height:1.3; margin-bottom:20px;">
            "Our philosophy since 2009 has remained unwavering: treat the person, not just the symptom. Every patient deserves patient, evidence-informed care that restores their joy of pain-free movement."
          </h3>
          <p style="font-size:16px; font-weight:700; color:#19535F; margin:0;">Dr. Prabhu Rajan, PT</p>
          <p style="font-size:14px; color:#4A5568; margin-top:4px;">Master in Sports Physiotherapy &bull; Vice Chairman AIDTA &bull; MIAP L-27944</p>
        </div>
      </div>
    </section>

    <!-- FINAL CTA / APPOINTMENT BOOKING -->
    <section class="section" style="padding:60px 0 90px 0; background:#FAF6EE;">
      <div class="container w-container">
        <div style="background:#19535F; border-radius:28px; padding:50px 30px; text-align:center; color:#FBF5E9; box-shadow:0 15px 35px rgba(25, 83, 95, 0.2);">
          <h3 style="font-family:'Recoleta',serif; font-size:36px; margin-bottom:14px; color:#FBF5E9;">Ready to start your recovery?</h3>
          <p style="font-size:18px; max-width:620px; margin:0 auto 30px auto; opacity:0.9;">
            Book an appointment today with Dr. Prabhu Rajan at our Chromepet clinic or enquire about home physiotherapy visits.
          </p>
          <div style="display:flex; justify-content:center; flex-wrap:wrap; gap:16px;">
            <a class="button w-button nav-btn" href="https://wa.me/919042612895?text=Hello%20Dr.%20Prabhu%2C%20I%20would%20like%20to%20book%20an%20appointment" target="_blank" style="background:#25D366; font-size:16px; padding:14px 30px; font-weight:600; display:inline-flex; align-items:center; gap:10px;">
              {SVG_WHATSAPP}
              <span>Book on WhatsApp: 90426 12895</span>
            </a>
            <a class="button w-button nav-btn" href="tel:9042612895" style="background:#FFFFFF; color:#19535F; font-size:16px; padding:14px 28px; font-weight:600; display:inline-flex; align-items:center; gap:10px;">
              {SVG_PHONE}
              <span>Call: +91 90426 12895</span>
            </a>
            <a class="button w-button nav-btn" href="{depth_prefix}free-assessment.html" style="background:transparent; border:2px solid #FBF5E9; color:#FBF5E9; font-size:16px; padding:12px 24px; display:inline-flex; align-items:center; gap:10px;">
              {SVG_CALENDAR}
              <span>Free Pain Assessment</span>
            </a>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- FOOTER -->
  <footer class="footer" style="padding:60px 0 30px 0; background:#FFFFFF; border-top:1px solid #E2E8F0;">
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
          <p style="font-size:14px; line-height:1.6; color:#4A5568; margin-bottom:8px; display:flex; gap:8px;">
            {SVG_MAP_PIN}
            <span>No. 9 / 29C, 1st Cross Street, Nagappa Nagar / New Colony, Chromepet, Chennai &ndash; 600044<br><em style="font-size:12px; color:#718096;">(Behind Chromepet Police Station / Shastri Colony)</em></span>
          </p>
          <p style="font-size:14px; line-height:1.6; color:#4A5568; margin-bottom:8px; display:flex; align-items:center; gap:8px;">
            {SVG_PHONE}
            <span><strong>Phone:</strong> <a href="tel:9042612895" style="color:#19535F; font-weight:600;">+91 90426 12895</a> / <a href="tel:9840512895" style="color:#19535F;">98405 12895</a></span>
          </p>
          <p style="font-size:14px; line-height:1.6; color:#4A5568; margin-bottom:8px; display:flex; align-items:center; gap:8px;">
            <span style="color:#25D366;">{SVG_WHATSAPP}</span>
            <span><strong>WhatsApp:</strong> <a href="https://wa.me/919042612895?text=Hello%20Dr.%20Prabhu%2C%20I%20would%20like%20to%20consult%20regarding%20physiotherapy" target="_blank" style="color:#25D366; font-weight:600;">+91 90426 12895</a></span>
          </p>
          <p style="font-size:14px; line-height:1.6; color:#4A5568; display:flex; align-items:center; gap:8px;">
            {SVG_MAIL}
            <span><strong>Email:</strong> <a href="mailto:rajansphysio2009@gmail.com" style="color:#19535F;">rajansphysio2009@gmail.com</a></span>
          </p>
        </div>
        <div>
          <h5 style="font-size:16px; font-weight:700; color:#19535F; margin-bottom:14px;">Quick Links</h5>
          <ul style="list-style:none; padding:0; margin:0; line-height:2.2; font-size:14px;">
            <li><a href="{depth_prefix}about.html" style="color:#4A5568; text-decoration:none;">About Dr. Prabhu Rajan</a></li>
            <li><a href="{depth_prefix}pricing.html" style="color:#4A5568; text-decoration:none;">Consultation &amp; Pricing</a></li>
            <li><a href="{depth_prefix}faq.html" style="color:#4A5568; text-decoration:none;">Frequently Asked Questions</a></li>
            <li><a href="{depth_prefix}free-assessment.html" style="color:#4A5568; text-decoration:none;">Free Pain Assessment</a></li>
            <li><a href="https://share.google/tpyR96H2jyHYaLHxz" target="_blank" style="color:#19535F; font-weight:600;">Google Maps Directions &rarr;</a></li>
          </ul>
        </div>
      </div>
      <div style="border-top:1px solid #E2E8F0; padding-top:24px; display:flex; justify-content:space-between; flex-wrap:wrap; gap:16px; font-size:13px; color:#718096;">
        <p>&copy; 2009 &ndash; 2026 Rajan's Physiotherapy &amp; Pain Relief Centre. All rights reserved.</p>
        <p>Chromepet, Chennai &bull; Practo 99% Recommended (513+ Ratings) &bull; Justdial 4.9 Stars (730+ Reviews)</p>
      </div>
    </div>
  </footer>

  <script src="{asset_prefix}js/jquery.min.js" type="text/javascript"></script>
  <script src="{asset_prefix}js/webflow.js" type="text/javascript"></script>
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
    return html

if __name__ == '__main__':
    content = generate_homepage_html('')
    with open(os.path.join(ROOT_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html with 5 additional sections and clean vector icons (zero emojis).")
