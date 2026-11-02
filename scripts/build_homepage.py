import os
from bs4 import BeautifulSoup

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def generate_home_html(depth_prefix):
    asset_prefix = f"{depth_prefix}assets/" if depth_prefix else "assets/"
    
    html = f"""<!DOCTYPE html>
<html data-wf-domain="rajansphysio.com" data-wf-page="home" lang="en">
<head>
  <meta charset="utf-8"/>
  <title>Rajan's Physiotherapy &amp; Pain Relief Centre | Chromepet, Chennai (Since 2009)</title>
  <meta content="Rajan's Physiotherapy &amp; Pain Relief Centre in Chromepet, Chennai. Led by Dr. Prabhu Rajan, PT (17 Yrs Exp). Expert manual therapy, Dorn spinal alignment, advanced laser &amp; shockwave therapy." name="description"/>
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
    }}
    .service-card:hover {{
      transform: translateY(-5px);
      box-shadow: 0 12px 30px rgba(25, 83, 95, 0.12);
    }}
    .testimonial-box {{
      background: #FBF5E9;
      border-radius: 20px;
      padding: 32px;
      border-left: 5px solid #19535F;
      margin-bottom: 24px;
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
  </style>
</head>
<body>

  <!-- HEADER -->
  <header>
    <div data-animation="default" data-collapse="medium" data-duration="400" data-easing="ease" data-easing2="ease" role="banner" class="navbar w-nav">
      <div class="container container--navbar w-container" style="display:flex; justify-content:space-between; align-items:center;">
        
        <!-- BRAND LOGO -->
        <a href="{depth_prefix or './'}" title="Rajan's Physiotherapy &amp; Pain Relief Centre" class="brand w-nav-brand w--current" style="text-decoration:none; display:flex; align-items:center; gap:12px;">
          <div style="width:44px; height:44px; border-radius:50%; background:#19535F; color:#FBF5E9; display:flex; align-items:center; justify-content:center; font-family:'Recoleta',serif; font-size:24px; font-weight:700; box-shadow:0 3px 8px rgba(25,83,95,0.25);">R</div>
          <div style="display:flex; flex-direction:column;">
            <span style="font-family:'Recoleta',serif; font-size:20px; font-weight:700; color:#19535F; line-height:1.15;">Rajan's Physiotherapy</span>
            <span style="font-size:11px; letter-spacing:0.8px; color:#5A6E72; text-transform:uppercase; font-weight:600;">&amp; Pain Relief Centre &bull; Since 2009</span>
          </div>
        </a>

        <!-- NAV MENU -->
        <nav role="navigation" class="nav-menu w-nav-menu" style="display:flex; align-items:center;">
          <a href="{depth_prefix or './'}" class="nav__link w-nav-link w--current">Home</a>
          <a href="{depth_prefix}about.html" class="nav__link w-nav-link">About Us</a>
          <a href="{depth_prefix}pricing.html" class="nav__link w-nav-link">Pricing &amp; Fees</a>
          <a href="{depth_prefix}faq.html" class="nav__link w-nav-link">FAQ</a>
          <a href="{depth_prefix}free-assessment.html" class="nav__link w-nav-link">Pain Checker</a>
          <a href="tel:9042612895" class="button w-button" style="margin-left:16px; background:#19535F; padding:10px 22px; font-size:14px;">Call: 90426 12895</a>
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
            <span class="clinic-badge">🏆 17+ Years Experience &bull; Est. 2009</span>
            <h1 class="heading-1 recoleta blue5" style="line-height:1.15; margin-bottom:20px;">
              Pain-free living starts <span class="highlight highlight--line">here.</span>
            </h1>
            <p class="fold__subtitle blue5" style="font-size:18px; line-height:1.6; margin-bottom:28px;">
              Personalized, evidence-informed physiotherapy and rehabilitation in Chromepet, Chennai. Led by <strong>Dr. Prabhu Rajan, PT</strong> (Master in Sports Physio, MIAP L-27944).
            </p>
            
            <ul class="fold_list w-list-unstyled" role="list" style="margin-bottom:32px;">
              <li class="fold__list-item" style="margin-bottom:10px; display:flex; align-items:center; gap:10px;">
                <img alt="Check" loading="lazy" src="{asset_prefix}images/6475b366ed49970529d05c92_icon-check.svg"/>
                <p class="blue5" style="font-size:16px; margin:0;"><strong>Dorn Method Spinal Alignment &amp; Manual Therapy</strong> (No cracking, surgery-free)</p>
              </li>
              <li class="fold__list-item" style="margin-bottom:10px; display:flex; align-items:center; gap:10px;">
                <img alt="Check" loading="lazy" src="{asset_prefix}images/6475b366ed49970529d05c92_icon-check.svg"/>
                <p class="blue5" style="font-size:16px; margin:0;"><strong>Advanced Laser &amp; Radial Shockwave Therapy</strong> for chronic tendinitis &amp; disc issues</p>
              </li>
              <li class="fold__list-item" style="margin-bottom:10px; display:flex; align-items:center; gap:10px;">
                <img alt="Check" loading="lazy" src="{asset_prefix}images/6475b366ed49970529d05c92_icon-check.svg"/>
                <p class="blue5" style="font-size:16px; margin:0;"><strong>99% Recommendation Rate</strong> on Practo &bull; 4.9★ on Justdial (730+ reviews)</p>
              </li>
              <li class="fold__list-item" style="display:flex; align-items:center; gap:10px;">
                <img alt="Check" loading="lazy" src="{asset_prefix}images/6475b366ed49970529d05c92_icon-check.svg"/>
                <p class="blue5" style="font-size:16px; margin:0;"><strong>Dedicated Home Physiotherapy Visits</strong> available in Chromepet &amp; nearby areas</p>
              </li>
            </ul>

            <div style="display:flex; flex-wrap:wrap; gap:16px; align-items:center;">
              <a class="button w-button" href="https://wa.me/919042612895?text=Hello%20Dr.%20Prabhu%2C%20I%20would%20like%20to%20book%20a%20physiotherapy%20consultation" target="_blank" style="background:#25D366; border:none; padding:14px 28px; font-size:16px; font-weight:600; display:flex; align-items:center; gap:8px;">
                <span>💬 Book on WhatsApp</span>
              </a>
              <a class="button button--secondary w-button" href="tel:9042612895" style="padding:14px 24px; font-size:16px;">
                <span>📞 Call: 90426 12895</span>
              </a>
            </div>
          </div>

          <div class="fold__images" style="position:relative;">
            <div style="position:relative; width:100%; max-width:440px; margin:0 auto;">
              <img alt="Dr. Prabhu Rajan PT - Chief Physiotherapist" src="{asset_prefix}images/dr_prabhu_rajan_profile.jpg" style="width:100%; height:auto; border-radius:24px; box-shadow:0 20px 40px rgba(25, 83, 95, 0.2); object-fit:cover; aspect-ratio:4/5;"/>
              
              <!-- Floating Trust Badge -->
              <div class="hero-doctor-badge">
                <div style="background:#25D366; width:12px; height:12px; border-radius:50%;"></div>
                <div>
                  <h4 style="font-size:14px; font-weight:700; color:#19535F; margin:0;">Dr. Prabhu Rajan, PT</h4>
                  <p style="font-size:12px; color:#4A5568; margin:0;">BPT, MPT (Sports), Dr.Acu, MIAP L-27944</p>
                  <p style="font-size:11px; color:#D69E2E; font-weight:700; margin:0;">★★★★★ 99% Recommended (513+ Patients)</p>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>

    <!-- STATS / TRUST BANNER -->
    <section class="section section--blue4 section--less-top-margin" style="padding:40px 0;">
      <div class="container w-container">
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:24px; text-align:center;">
          <div>
            <div style="font-family:'Recoleta',serif; font-size:42px; font-weight:700; color:#FBF5E9;">17+</div>
            <p style="color:#FBF5E9; opacity:0.85; font-size:15px; margin:0;">Years Clinical Excellence</p>
          </div>
          <div>
            <div style="font-family:'Recoleta',serif; font-size:42px; font-weight:700; color:#FBF5E9;">15,000+</div>
            <p style="color:#FBF5E9; opacity:0.85; font-size:15px; margin:0;">Patients Treated</p>
          </div>
          <div>
            <div style="font-family:'Recoleta',serif; font-size:42px; font-weight:700; color:#FBF5E9;">99%</div>
            <p style="color:#FBF5E9; opacity:0.85; font-size:15px; margin:0;">Practo Positive Score</p>
          </div>
          <div>
            <div style="font-family:'Recoleta',serif; font-size:42px; font-weight:700; color:#FBF5E9;">₹600</div>
            <p style="color:#FBF5E9; opacity:0.85; font-size:15px; margin:0;">Consultation Fee</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 1: WHY CHOOSE US -->
    <section class="section" style="padding:80px 0;">
      <div class="container w-container">
        <div class="section__header" style="text-align:center; max-width:760px; margin:0 auto 60px auto;">
          <p class="uppercase blue4" style="letter-spacing:1px; font-weight:700;">WHY RAJAN'S PHYSIOTHERAPY</p>
          <h2 class="heading-2 recoleta" style="font-size:38px;">
            Targeted hands-on care.<br/>Personalized for <span class="highlight highlight--circle">lasting relief.</span>
          </h2>
          <p style="font-size:17px; line-height:1.6; color:#4A5568; margin-top:16px;">
            We don't believe in temporary pain-killers or lifetime braces. We identify the true root cause of your pain through precise palpation, joint assessment, and customized therapeutic protocols.
          </p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:32px;">
          
          <div class="service-card">
            <div>
              <div style="width:52px; height:52px; border-radius:12px; background:#E8F1F2; display:flex; align-items:center; justify-content:center; font-size:24px; margin-bottom:20px;">🦴</div>
              <h3 style="font-family:'Recoleta',serif; font-size:22px; margin-bottom:12px; color:#19535F;">Dorn Spinal Alignment</h3>
              <p style="color:#4A5568; line-height:1.6; font-size:15px;">
                A gentle, non-invasive vertebrae alignment technique without cracking or surgery. Highly effective for cervical spondylitis, lumbar disc bulge (L4-L5, L5-S1), and sciatica.
              </p>
            </div>
            <p style="font-size:13px; font-weight:600; color:#19535F; margin-top:16px;">Vice Chairman AIDTA Certified &rarr;</p>
          </div>

          <div class="service-card">
            <div>
              <div style="width:52px; height:52px; border-radius:12px; background:#E8F1F2; display:flex; align-items:center; justify-content:center; font-size:24px; margin-bottom:20px;">⚡</div>
              <h3 style="font-family:'Recoleta',serif; font-size:22px; margin-bottom:12px; color:#19535F;">Advanced Laser &amp; Shockwave</h3>
              <p style="color:#4A5568; line-height:1.6; font-size:15px;">
                High-intensity scanning laser therapy and radial extracorporeal shockwave therapy (ESWT) to dissolve calcifications, stimulate deep cellular healing, and heal chronic tendinopathies.
              </p>
            </div>
            <p style="font-size:13px; font-weight:600; color:#19535F; margin-top:16px;">Technomed LaserStim &amp; ESWT &rarr;</p>
          </div>

          <div class="service-card">
            <div>
              <div style="width:52px; height:52px; border-radius:12px; background:#E8F1F2; display:flex; align-items:center; justify-content:center; font-size:24px; margin-bottom:20px;">🎯</div>
              <h3 style="font-family:'Recoleta',serif; font-size:22px; margin-bottom:12px; color:#19535F;">Dry Needling &amp; Myofascial Release</h3>
              <p style="color:#4A5568; line-height:1.6; font-size:15px;">
                Certified Dry Needling Therapist (USA) utilizing precision filament needles and deep trigger-point release to deactivate stubborn muscular knots and referred nerve pain in seconds.
              </p>
            </div>
            <p style="font-size:13px; font-weight:600; color:#19535F; margin-top:16px;">CDNT (USA) Certified &rarr;</p>
          </div>

        </div>
      </div>
    </section>

    <!-- SECTION 2: 4-STEP RECOVERY PROCESS -->
    <section class="section section--steps" style="padding:80px 0; background:#FAF6EE;">
      <div class="container w-container">
        <div class="section__header" style="text-align:center; max-width:700px; margin:0 auto 50px auto;">
          <h3 class="heading-3 recoleta" style="font-size:36px;">
            Say goodbye to pain.<br/>Only <span class="highlight highlight--yellow-line">4 steps</span> to active recovery.
          </h3>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr)); gap:24px;">
          
          <div style="background:#FFF; padding:28px; border-radius:18px; box-shadow:0 4px 15px rgba(0,0,0,0.03);">
            <div style="font-family:'Recoleta',serif; font-size:32px; font-weight:700; color:#19535F; margin-bottom:12px;">01</div>
            <h4 style="font-size:18px; font-weight:700; margin-bottom:8px; color:#19535F;">Physical Palpation</h4>
            <p style="font-size:14px; line-height:1.6; color:#4A5568;">Comprehensive tactile assessment of musculoskeletal dysfunction, joint range, and neural tension.</p>
          </div>

          <div style="background:#FFF; padding:28px; border-radius:18px; box-shadow:0 4px 15px rgba(0,0,0,0.03);">
            <div style="font-family:'Recoleta',serif; font-size:32px; font-weight:700; color:#19535F; margin-bottom:12px;">02</div>
            <h4 style="font-size:18px; font-weight:700; margin-bottom:8px; color:#19535F;">Tailored Care Plan</h4>
            <p style="font-size:14px; line-height:1.6; color:#4A5568;">Individualized treatment program combining manual therapy, spinal alignment, and electro-modalities.</p>
          </div>

          <div style="background:#FFF; padding:28px; border-radius:18px; box-shadow:0 4px 15px rgba(0,0,0,0.03);">
            <div style="font-family:'Recoleta',serif; font-size:32px; font-weight:700; color:#19535F; margin-bottom:12px;">03</div>
            <h4 style="font-size:18px; font-weight:700; margin-bottom:8px; color:#19535F;">Hands-on Therapy</h4>
            <p style="font-size:14px; line-height:1.6; color:#4A5568;">Focused manual realignment, laser/shockwave healing, and immediate muscular knot release.</p>
          </div>

          <div style="background:#FFF; padding:28px; border-radius:18px; box-shadow:0 4px 15px rgba(0,0,0,0.03);">
            <div style="font-family:'Recoleta',serif; font-size:32px; font-weight:700; color:#19535F; margin-bottom:12px;">04</div>
            <h4 style="font-size:18px; font-weight:700; margin-bottom:8px; color:#19535F;">Active Prevention</h4>
            <p style="font-size:14px; line-height:1.6; color:#4A5568;">Custom corrective exercise prescription to strengthen deep core muscles and prevent recurrence.</p>
          </div>

        </div>
      </div>
    </section>

    <!-- SECTION 3: ADVANCED CLINICAL MODALITIES SHOWCASE -->
    <section class="section" style="padding:80px 0;">
      <div class="container w-container">
        <div class="section__header" style="text-align:center; max-width:760px; margin:0 auto 60px auto;">
          <p class="uppercase blue4" style="letter-spacing:1px; font-weight:700;">OUR CLINIC &amp; TECHNOLOGY</p>
          <h3 class="heading-3 recoleta" style="font-size:36px;">Advanced healing equipment &amp; comfortable facilities</h3>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:32px;">
          
          <div style="background:#FFFFFF; border-radius:20px; overflow:hidden; box-shadow:0 4px 20px rgba(0,0,0,0.05);">
            <img src="{asset_prefix}images/clinic_treatment_beds.jpg" alt="LASERSTIM Laser Therapy" style="width:100%; height:240px; object-fit:cover;"/>
            <div style="padding:24px;">
              <h4 style="font-family:'Recoleta',serif; font-size:20px; color:#19535F; margin-bottom:8px;">LASERSTIM &amp; Scanning Laser</h4>
              <p style="font-size:14px; line-height:1.6; color:#4A5568;">Non-invasive laser therapy targeting deep tendon injuries, ligament sprains, knee osteoarthritis, and acute inflammatory conditions.</p>
            </div>
          </div>

          <div style="background:#FFFFFF; border-radius:20px; overflow:hidden; box-shadow:0 4px 20px rgba(0,0,0,0.05);">
            <img src="{asset_prefix}images/clinic_therapy_equipment.jpg" alt="Electroson 608 Ultrasound" style="width:100%; height:240px; object-fit:cover;"/>
            <div style="padding:24px;">
              <h4 style="font-family:'Recoleta',serif; font-size:20px; color:#19535F; margin-bottom:8px;">Electrotherapy &amp; Ultrasound (IFT/UST)</h4>
              <p style="font-size:14px; line-height:1.6; color:#4A5568;">Electroson 608 clinical workstation for deep tissue heating, neuromuscular re-education, edema reduction, and nerve stimulation.</p>
            </div>
          </div>

          <div style="background:#FFFFFF; border-radius:20px; overflow:hidden; box-shadow:0 4px 20px rgba(0,0,0,0.05);">
            <img src="{asset_prefix}images/clinic_interior_reception.jpg" alt="Reception &amp; Waiting Lounge" style="width:100%; height:240px; object-fit:cover;"/>
            <div style="padding:24px;">
              <h4 style="font-family:'Recoleta',serif; font-size:20px; color:#19535F; margin-bottom:8px;">Patient Reception &amp; Lounge</h4>
              <p style="font-size:14px; line-height:1.6; color:#4A5568;">Hygienic, comfortable, and well-equipped treatment cubicles ensuring patient privacy, personal dignity, and sterile clinical standards.</p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- SECTION 4: REAL PATIENT REVIEWS -->
    <section class="section section--blue2" style="padding:80px 0; background:#19535F; color:#FBF5E9;">
      <div class="container w-container">
        <div class="section__header" style="text-align:center; max-width:760px; margin:0 auto 60px auto;">
          <p class="uppercase" style="letter-spacing:1px; color:#FBF5E9; opacity:0.8; font-weight:700;">VERIFIED PATIENT STORIES</p>
          <h3 class="heading-3 recoleta" style="color:#FBF5E9; font-size:38px;">What our patients say</h3>
          <p style="color:#FBF5E9; opacity:0.9; font-size:16px;">Real feedback from patients treated at Rajan's Physiotherapy &amp; Pain Relief Centre</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:28px;">
          
          <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.15); border-radius:20px; padding:32px; backdrop-filter:blur(10px);">
            <div style="color:#F6E05E; font-size:18px; margin-bottom:12px;">★★★★★</div>
            <p style="font-size:15px; line-height:1.7; opacity:0.95; margin-bottom:20px; font-style:italic;">
              "When I met the Doctor, I was not able to walk properly and while sitting too had severe pain from an old ligament tear. He never asked me to take scans. Just by touching he found out the problem! During the second sitting, I found enormous improvement. Now I am able to climb stairs normally, which I couldn't do for 10 long years!"
            </p>
            <div style="font-weight:700; font-size:15px;">&mdash; Devi.S.P</div>
            <div style="font-size:13px; opacity:0.75;">Knee Ligament Tear &bull; Practo Verified</div>
          </div>

          <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.15); border-radius:20px; padding:32px; backdrop-filter:blur(10px);">
            <div style="color:#F6E05E; font-size:18px; margin-bottom:12px;">★★★★★</div>
            <p style="font-size:15px; line-height:1.7; opacity:0.95; margin-bottom:20px; font-style:italic;">
              "I have been suffering from L3-L4 disc bulge and cervical spondylitis for 15 years. I consulted orthos, tried ayurveda, but within the first 10 sessions of manual therapy and basic exercises with Dr. Prabhu, my pain subsided completely without any medicines! Highly recommend before wearing back belts for life."
            </p>
            <div style="font-weight:700; font-size:15px;">&mdash; Mrs. Hema</div>
            <div style="font-size:13px; opacity:0.75;">15-Year Disc Bulge &bull; Practo Verified</div>
          </div>

          <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.15); border-radius:20px; padding:32px; backdrop-filter:blur(10px);">
            <div style="color:#F6E05E; font-size:18px; margin-bottom:12px;">★★★★★</div>
            <p style="font-size:15px; line-height:1.7; opacity:0.95; margin-bottom:20px; font-style:italic;">
              "Dr. Prabhu listened patiently, analysed to identify the root cause, and taught several strengthening exercises which cut the problem at its root. I am deeply thankful that I have had no recurrence of knee pain since!"
            </p>
            <div style="font-weight:700; font-size:15px;">&mdash; Viswapriya</div>
            <div style="font-size:13px; opacity:0.75;">Knee Rehabilitation &bull; Practo Verified</div>
          </div>

        </div>
      </div>
    </section>

    <!-- SECTION 5: DOCTOR QUOTE & COMMITMENT -->
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

    <!-- SECTION 6: CTA / APPOINTMENT BOOKING -->
    <section class="section" style="padding:60px 0; background:#FAF6EE;">
      <div class="container w-container">
        <div style="background:#19535F; border-radius:28px; padding:50px; text-align:center; color:#FBF5E9; box-shadow:0 15px 35px rgba(25, 83, 95, 0.2);">
          <h3 style="font-family:'Recoleta',serif; font-size:36px; margin-bottom:14px; color:#FBF5E9;">Ready to start your recovery?</h3>
          <p style="font-size:18px; max-width:600px; margin:0 auto 30px auto; opacity:0.9;">
            Book an appointment today with Dr. Prabhu Rajan at our Chromepet clinic or enquire about home physiotherapy visits.
          </p>
          <div style="display:flex; justify-content:center; flex-wrap:wrap; gap:16px;">
            <a class="button w-button" href="https://wa.me/919042612895?text=Hello%20Dr.%20Prabhu%2C%20I%20would%20like%20to%20book%20an%20appointment" target="_blank" style="background:#25D366; font-size:16px; padding:14px 32px; font-weight:600;">
              💬 Book on WhatsApp: 90426 12895
            </a>
            <a class="button w-button" href="tel:9042612895" style="background:#FFFFFF; color:#19535F; font-size:16px; padding:14px 28px; font-weight:600;">
              📞 Call: +91 90426 12895
            </a>
            <a class="button w-button" href="{depth_prefix}free-assessment.html" style="background:transparent; border:2px solid #FBF5E9; color:#FBF5E9; font-size:16px; padding:12px 24px;">
              📋 Free Pain Assessment
            </a>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- FOOTER -->
  {get_footer_html(depth_prefix)}

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

# Helper for footer
def get_footer_html(depth_prefix):
    return f"""<footer class="footer" style="padding:60px 0 30px 0; background:#FFFFFF; border-top:1px solid #E2E8F0;">
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
    </footer>"""

if __name__ == '__main__':
    home_html = generate_home_html('')
    with open(os.path.join(ROOT_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(home_html)
    print("Updated index.html successfully.")
