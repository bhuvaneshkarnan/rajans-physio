import os
import json
from build_full_website import (
    get_global_head, get_global_nav, get_global_footer, get_cta_section,
    SVG_CHECK, SVG_PHONE, SVG_WHATSAPP, SVG_STAR, SVG_MAP_PIN, SVG_MAIL,
    SVG_SHIELD, SVG_SPINE, SVG_ACTIVITY, SVG_LASER, SVG_CROSSHAIR, SVG_HOME,
    SVG_HEART, SVG_CALENDAR, SVG_CHEVRON, SVG_ARROW_RIGHT, SVG_AWARD, SVG_CLOCK,
    SVG_WAVE, SVG_ZAP, SVG_NEEDLE, SVG_LAYERS
)
from build_all_service_pages import SERVICES_DATA, render_service_page, render_contact_page

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

with open(os.path.join(ROOT_DIR, 'extracted_data', 'clinic_data.json'), 'r', encoding='utf-8') as f:
    clinic_data = json.load(f)

# -------------------------------------------------------------
# 1. HOMEPAGE GENERATOR (Tight line-spacing, clean typography, 0 emojis)
# -------------------------------------------------------------
def render_homepage():
    asset_prefix = "assets/"
    
    html = f"""{get_global_head(
        "Rajan's Physiotherapy & Pain Relief Centre | Chromepet, Chennai (Since 2009)",
        "Rajan's Physiotherapy & Pain Relief Centre in Chromepet, Chennai. Established 2009. Led by Dr. Prabhu Rajan, PT (17 Yrs Exp, MPT Sports, MIAP, AIDTA). Dorn method spinal alignment, scanning laser, shockwave & dry needling.",
        asset_prefix
    )}
{get_global_nav("", "home")}

  <main>
    <!-- HERO SECTION -->
    <section class="section section--hero" style="background:#FAF6EE; padding:60px 0 72px 0;">
      <div class="container w-container">
        <div class="hero-grid">
          <div>
            <div class="clinic-badge">
              {SVG_SHIELD} 17 Years of Clinical Excellence &bull; Est. 2009
            </div>
            <h1 class="heading-1 hero-title" style="font-size:clamp(36px, 4.8vw, 54px); line-height:1.14 !important; font-weight:800 !important; margin-bottom:18px;">
              Pain-free living starts <span class="highlight highlight--line" style="display:inline; line-height:inherit;">here.</span>
            </h1>
            <p class="text-lead" style="margin-bottom:24px;">
              Over 15,000 patients successfully treated without surgery. We diagnose the biomechanical root cause of your pain &mdash; restoring mobility, freedom, and strength.
            </p>

            <div class="hero-ratings-group" style="display:flex; flex-wrap:wrap; gap:16px; margin-bottom:28px;">
              <div style="display:flex; align-items:center; gap:8px; font-size:14px; font-weight:600; color:#233E85;">
                {SVG_CHECK} Practo 99% Recommended (513+ Ratings)
              </div>
              <div style="display:flex; align-items:center; gap:8px; font-size:14px; font-weight:600; color:#233E85;">
                {SVG_CHECK} Justdial 4.9 Stars (730+ Reviews)
              </div>
            </div>

            <div class="hero-cta-group" style="display:flex; flex-wrap:wrap; gap:14px; margin-bottom:32px;">
              <a href="https://wa.me/919042612895?text=Hello%20Dr.%20Prabhu%2C%20I%20would%20like%20to%20book%20a%20consultation" target="_blank" class="btn-whatsapp">
                {SVG_WHATSAPP} Book via WhatsApp
              </a>
              <a href="tel:9042612895" class="btn-secondary">
                {SVG_PHONE} Call +91 90426 12895
              </a>
            </div>

            <div class="hero-stats-grid" style="display:grid; grid-template-columns: repeat(3, 1fr); gap:16px; padding-top:20px; border-top:1px solid #E2E8F0;">
              <div>
                <div data-counter="17" data-suffix="+" style="font-family:'Recoleta',Georgia,serif; font-size:26px; font-weight:700; color:#233E85; line-height:1.1;">17+</div>
                <div class="hero-stat-label" style="font-size:12px; color:#536B88; font-weight:600; text-transform:uppercase;">Years Experience</div>
              </div>
              <div>
                <div data-counter="15000" data-suffix="+" style="font-family:'Recoleta',Georgia,serif; font-size:26px; font-weight:700; color:#233E85; line-height:1.1;">15,000+</div>
                <div class="hero-stat-label" style="font-size:12px; color:#536B88; font-weight:600; text-transform:uppercase;">Patients Healed</div>
              </div>
              <div>
                <div data-counter="99" data-suffix="%" style="font-family:'Recoleta',Georgia,serif; font-size:26px; font-weight:700; color:#233E85; line-height:1.1;">99%</div>
                <div class="hero-stat-label" style="font-size:12px; color:#536B88; font-weight:600; text-transform:uppercase;">Practo Score</div>
              </div>
            </div>
          </div>

          <div style="position:relative;">
            <div class="photo-card reveal-blur" style="">
              <img src="assets/images/dr_prabhu_rajan_profile.jpg" alt="Dr. Prabhu Rajan, PT" class="hero-doctor-img" loading="eager"/>
            </div>
            
            <div class="reveal-blur hero-doctor-badge" style="position:absolute; bottom:20px; left:20px; right:20px; background:rgba(255,255,255,0.95); backdrop-filter:blur(8px); border-radius:14px; padding:16px 20px;  border:1px solid #EEF2F4;">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <div>
                  <div style="font-family:'Recoleta',Georgia,serif; font-size:18px; font-weight:700; color:#233E85; line-height:1.2;">Dr. Prabhu Rajan, PT</div>
                  <div style="font-size:12.5px; color:#536B88;">Chief Physiotherapist &bull; MIAP L-27944</div>
                </div>
                <div style="display:flex; align-items:center; gap:4px; background:#FEFCBF; padding:4px 10px; border-radius:20px; font-size:12.5px; font-weight:700; color:#744210;">
                  {SVG_STAR} <span data-counter="4.9" data-suffix=" / 5.0">4.9 / 5.0</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 1: CONDITIONS & CLINICAL SPECIALTIES -->
    <section id="specialties" class="section" style="background:#FFFFFF; padding:72px 0;">
      <div class="container w-container">
        <div style="text-align:center; max-width:720px; margin:0 auto 48px auto;">
          <div class="section-kicker">CONDITIONS WE TREAT</div>
          <h2 class="heading-2" style="font-size:clamp(30px, 3.8vw, 44px); line-height:1.2 !important; margin:0 0 16px 0;">
            Targeted relief for <span class="highlight highlight--line" style="display:inline; line-height:inherit;">complex conditions.</span>
          </h2>
          <p class="section-subtitle">
            From severe acute disc herniations and sciatica to stubborn sports injuries, we treat the biomechanical origin of your pain.
          </p>
        </div>

        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap:24px;">
          <!-- CARD 1 -->
          <a href="dorn-spinal-therapy.html" style="text-decoration:none; color:inherit;">
            <div class="service-card reveal-blur stagger-1">
              <div>
                <div style="width:48px; height:48px; border-radius:12px; background:#EEF3FA; display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
                  {SVG_SPINE}
                </div>
                <h3 style="font-family:'Recoleta',Georgia,serif; font-size:20px; line-height:1.26 !important; color:#233E85 !important; margin-bottom:10px;">
                  Spine, Neck &amp; Disc Care
                </h3>
                <p style="font-size:14px; line-height:1.6 !important; color:#4A5568 !important; margin:0 0 16px 0;">
                  Slip disc, sciatica, cervical spondylosis, lumbar radiculopathy, and scoliosis. Gentle non-surgical correction.
                </p>
              </div>
              <div style="display:flex; align-items:center; justify-content:space-between; padding-top:14px; border-top:1px solid #EEF2F4; font-size:13px; font-weight:600; color:#233E85;">
                <span>Dorn Spinal Alignment</span>
                {SVG_ARROW_RIGHT}
              </div>
            </div>
          </a>

          <!-- CARD 2 -->
          <a href="laser-therapy.html" style="text-decoration:none; color:inherit;">
            <div class="service-card reveal-blur stagger-2">
              <div>
                <div style="width:48px; height:48px; border-radius:12px; background:#EEF3FA; display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
                  {SVG_ACTIVITY}
                </div>
                <h3 style="font-family:'Recoleta',Georgia,serif; font-size:20px; line-height:1.26 !important; color:#233E85 !important; margin-bottom:10px;">
                  Joint &amp; Shoulder Pain
                </h3>
                <p style="font-size:14px; line-height:1.6 !important; color:#4A5568 !important; margin:0 0 16px 0;">
                  Frozen shoulder, rotator cuff tears, bursitis, arthritis, and tennis elbow. Deep tissue photobiomodulation.
                </p>
              </div>
              <div style="display:flex; align-items:center; justify-content:space-between; padding-top:14px; border-top:1px solid #EEF2F4; font-size:13px; font-weight:600; color:#233E85;">
                <span>Laser Therapy</span>
                {SVG_ARROW_RIGHT}
              </div>
            </div>
          </a>

          <!-- CARD 3 -->
          <a href="shockwave-therapy.html" style="text-decoration:none; color:inherit;">
            <div class="service-card reveal-blur stagger-3">
              <div>
                <div style="width:48px; height:48px; border-radius:12px; background:#EEF3FA; display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
                  {SVG_WAVE}
                </div>
                <h3 style="font-family:'Recoleta',Georgia,serif; font-size:20px; line-height:1.26 !important; color:#233E85 !important; margin-bottom:10px;">
                  Knee, Foot &amp; Heel Pain
                </h3>
                <p style="font-size:14px; line-height:1.6 !important; color:#4A5568 !important; margin:0 0 16px 0;">
                  Plantar fasciitis, calcaneal heel spurs, knee osteoarthritis, and Achilles tendinitis resolved with acoustic shockwaves.
                </p>
              </div>
              <div style="display:flex; align-items:center; justify-content:space-between; padding-top:14px; border-top:1px solid #EEF2F4; font-size:13px; font-weight:600; color:#233E85;">
                <span>Shockwave ESWT</span>
                {SVG_ARROW_RIGHT}
              </div>
            </div>
          </a>

          <!-- CARD 4 -->
          <a href="sports-rehabilitation.html" style="text-decoration:none; color:inherit;">
            <div class="service-card reveal-blur stagger-4">
              <div>
                <div style="width:48px; height:48px; border-radius:12px; background:#EEF3FA; display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
                  {SVG_AWARD}
                </div>
                <h3 style="font-family:'Recoleta',Georgia,serif; font-size:20px; line-height:1.26 !important; color:#233E85 !important; margin-bottom:10px;">
                  Sports &amp; Post-Surgical
                </h3>
                <p style="font-size:14px; line-height:1.6 !important; color:#4A5568 !important; margin:0 0 16px 0;">
                  ACL rehabilitation, meniscus recovery, ligament sprains, total knee/hip replacement rehab, and athletic conditioning.
                </p>
              </div>
              <div style="display:flex; align-items:center; justify-content:space-between; padding-top:14px; border-top:1px solid #EEF2F4; font-size:13px; font-weight:600; color:#233E85;">
                <span>Sports Rehabilitation</span>
                {SVG_ARROW_RIGHT}
              </div>
            </div>
          </a>
        </div>
      </div>
    </section>

    <!-- SECTION 2: COMPLETE TREATMENT MODALITIES ARSENAL -->
    <section id="modalities" class="section" style="background:#FAF6EE; padding:72px 0;">
      <div class="container w-container">
        <div style="text-align:center; max-width:720px; margin:0 auto 48px auto;">
          <div class="section-kicker">TREATMENT MODALITIES</div>
          <h2 class="heading-2" style="font-size:clamp(30px, 3.8vw, 44px); line-height:1.2 !important; margin:0 0 16px 0;">
            Evidence-informed therapies for <span class="highlight highlight--line" style="display:inline; line-height:inherit;">rapid healing.</span>
          </h2>
          <p class="section-subtitle">
            Combining European manual techniques with precision physical modalities for deep tissue cellular repair.
          </p>
        </div>

        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:24px;">
          <!-- M1 -->
          <a href="laser-therapy.html" style="text-decoration:none; color:inherit;">
            <div class="bento-card reveal-blur stagger-1">
              <div style="display:flex; align-items:center; gap:12px; margin-bottom:12px;">
                <div style="width:40px; height:40px; border-radius:10px; background:#EEF3FA; display:flex; align-items:center; justify-content:center;">
                  {SVG_LASER}
                </div>
                <h3 style="font-family:'Recoleta',Georgia,serif; font-size:20px; line-height:1.26 !important; color:#233E85 !important; margin:0;">
                  LASERSTIM Scanning Laser
                </h3>
              </div>
              <p style="font-size:14px; line-height:1.6 !important; color:#4A5568 !important; margin-bottom:14px;">
                Deep tissue photobiomodulation stimulates mitochondrial ATP synthesis, eliminating acute inflammation and accelerating cellular repair.
              </p>
              <div style="font-size:12.5px; font-weight:600; color:#233E85; display:flex; align-items:center; gap:6px;">
                <span>Explore Laser Therapy</span> {SVG_ARROW_RIGHT}
              </div>
            </div>
          </a>

          <!-- M2 -->
          <a href="shockwave-therapy.html" style="text-decoration:none; color:inherit;">
            <div class="bento-card reveal-blur stagger-2">
              <div style="display:flex; align-items:center; gap:12px; margin-bottom:12px;">
                <div style="width:40px; height:40px; border-radius:10px; background:#EEF3FA; display:flex; align-items:center; justify-content:center;">
                  {SVG_WAVE}
                </div>
                <h3 style="font-family:'Recoleta',Georgia,serif; font-size:20px; line-height:1.26 !important; color:#233E85 !important; margin:0;">
                  Radial Shockwave Therapy
                </h3>
              </div>
              <p style="font-size:14px; line-height:1.6 !important; color:#4A5568 !important; margin-bottom:14px;">
                Acoustic pressure waves break down stubborn calcifications, dissolve bone spurs, and restart dormant tissue healing cascades.
              </p>
              <div style="font-size:12.5px; font-weight:600; color:#233E85; display:flex; align-items:center; gap:6px;">
                <span>Explore Shockwave Therapy</span> {SVG_ARROW_RIGHT}
              </div>
            </div>
          </a>

          <!-- M3 -->
          <a href="dorn-spinal-therapy.html" style="text-decoration:none; color:inherit;">
            <div class="bento-card reveal-blur stagger-3">
              <div style="display:flex; align-items:center; gap:12px; margin-bottom:12px;">
                <div style="width:40px; height:40px; border-radius:10px; background:#EEF3FA; display:flex; align-items:center; justify-content:center;">
                  {SVG_SPINE}
                </div>
                <h3 style="font-family:'Recoleta',Georgia,serif; font-size:20px; line-height:1.26 !important; color:#233E85 !important; margin:0;">
                  Dorn Spinal Alignment
                </h3>
              </div>
              <p style="font-size:14px; line-height:1.6 !important; color:#4A5568 !important; margin-bottom:14px;">
                Gentle, active-dynamic manual therapy to realign vertebrae and pelvic joints without aggressive thrusts or violent cracking.
              </p>
              <div style="font-size:12.5px; font-weight:600; color:#233E85; display:flex; align-items:center; gap:6px;">
                <span>Explore Dorn Therapy</span> {SVG_ARROW_RIGHT}
              </div>
            </div>
          </a>

          <!-- M4 -->
          <a href="dry-needling.html" style="text-decoration:none; color:inherit;">
            <div class="bento-card reveal-blur stagger-4">
              <div style="display:flex; align-items:center; gap:12px; margin-bottom:12px;">
                <div style="width:40px; height:40px; border-radius:10px; background:#EEF3FA; display:flex; align-items:center; justify-content:center;">
                  {SVG_NEEDLE}
                </div>
                <h3 style="font-family:'Recoleta',Georgia,serif; font-size:20px; line-height:1.26 !important; color:#233E85 !important; margin:0;">
                  Clinical Dry Needling (CDNT)
                </h3>
              </div>
              <p style="font-size:14px; line-height:1.6 !important; color:#4A5568 !important; margin-bottom:14px;">
                Precision intramuscular trigger point deactivation resets contracted motor endplates, releasing chronic neck, back &amp; hip knots.
              </p>
              <div style="font-size:12.5px; font-weight:600; color:#233E85; display:flex; align-items:center; gap:6px;">
                <span>Explore Dry Needling</span> {SVG_ARROW_RIGHT}
              </div>
            </div>
          </a>

          <!-- M5 -->
          <a href="tecar-therapy.html" style="text-decoration:none; color:inherit;">
            <div class="bento-card reveal-blur stagger-5">
              <div style="display:flex; align-items:center; gap:12px; margin-bottom:12px;">
                <div style="width:40px; height:40px; border-radius:10px; background:#EEF3FA; display:flex; align-items:center; justify-content:center;">
                  {SVG_ZAP}
                </div>
                <h3 style="font-family:'Recoleta',Georgia,serif; font-size:20px; line-height:1.26 !important; color:#233E85 !important; margin:0;">
                  TECAR Radiofrequency
                </h3>
              </div>
              <p style="font-size:14px; line-height:1.6 !important; color:#4A5568 !important; margin-bottom:14px;">
                Capacitive and resistive diathermy generates endogenous thermal biostimulation, dramatically speeding knee arthritis recovery.
              </p>
              <div style="font-size:12.5px; font-weight:600; color:#233E85; display:flex; align-items:center; gap:6px;">
                <span>Explore TECAR Therapy</span> {SVG_ARROW_RIGHT}
              </div>
            </div>
          </a>

          <!-- M6 -->
          <a href="cupping-iastm.html" style="text-decoration:none; color:inherit;">
            <div class="bento-card reveal-blur stagger-6">
              <div style="display:flex; align-items:center; gap:12px; margin-bottom:12px;">
                <div style="width:40px; height:40px; border-radius:10px; background:#EEF3FA; display:flex; align-items:center; justify-content:center;">
                  {SVG_LAYERS}
                </div>
                <h3 style="font-family:'Recoleta',Georgia,serif; font-size:20px; line-height:1.26 !important; color:#233E85 !important; margin:0;">
                  Kinesio Cupping &amp; IASTM
                </h3>
              </div>
              <p style="font-size:14px; line-height:1.6 !important; color:#4A5568 !important; margin-bottom:14px;">
                Negative pressure myofascial decompression and stainless-steel instruments release stubborn scar tissue and fascial restrictions.
              </p>
              <div style="font-size:12.5px; font-weight:600; color:#233E85; display:flex; align-items:center; gap:6px;">
                <span>Explore Cupping &amp; IASTM</span> {SVG_ARROW_RIGHT}
              </div>
            </div>
          </a>
        </div>
      </div>
    </section>

    <!-- 4-STEP CLINICAL PROTOCOL SECTION -->
    <section class="section" style="background:#FAF9F6; padding:72px 0;">
      <div class="container w-container">
        <div style="text-align:center; max-width:680px; margin:0 auto 48px auto;">
          <div class="section-kicker">OUR CLINICAL PROTOCOL</div>
          <h2 class="heading-2" style="font-size:clamp(30px, 3.8vw, 44px); line-height:1.2 !important; margin-bottom:16px;">
            Say goodbye to pain.<br/>Only <span class="highlight highlight--yellow-line">4 steps</span> to active recovery.
          </h2>
          <p class="section-subtitle">
            From initial musculoskeletal palpation to long-term ergonomic stabilization, Dr. Prabhu Rajan ensures your recovery is structured, measurable, and permanent.
          </p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr)); gap:24px;">
          
          <div class="bento-card reveal-blur stagger-1" style="background:#FFFFFF; padding:28px; border-radius:18px; border:1px solid #DCE5F5;">
            <div style="font-family:'Recoleta',serif; font-size:32px; font-weight:700; color:#ED1D7F; margin-bottom:12px;">01</div>
            <h3 style="font-size:18px; font-weight:700; margin-bottom:8px; color:#233E85;">Physical Palpation</h3>
            <p style="font-size:14.5px; line-height:1.6; color:#4A5568; margin-bottom:0;">
              Comprehensive tactile assessment of musculoskeletal dysfunction, joint range of motion, and spinal alignment discrepancies.
            </p>
          </div>

          <div class="bento-card reveal-blur stagger-2" style="background:#FFFFFF; padding:28px; border-radius:18px; border:1px solid #DCE5F5;">
            <div style="font-family:'Recoleta',serif; font-size:32px; font-weight:700; color:#233E85; margin-bottom:12px;">02</div>
            <h3 style="font-size:18px; font-weight:700; margin-bottom:8px; color:#233E85;">Laser &amp; Manual Therapy</h3>
            <p style="font-size:14.5px; line-height:1.6; color:#4A5568; margin-bottom:0;">
              High-power scanning laser stim, radial shockwave, or gentle Dorn joint realignment to eliminate acute cellular inflammation and nerve compression.
            </p>
          </div>

          <div class="bento-card reveal-blur stagger-3" style="background:#FFFFFF; padding:28px; border-radius:18px; border:1px solid #DCE5F5;">
            <div style="font-family:'Recoleta',serif; font-size:32px; font-weight:700; color:#ED1D7F; margin-bottom:12px;">03</div>
            <h3 style="font-size:18px; font-weight:700; margin-bottom:8px; color:#233E85;">Rehabilitation Exercises</h3>
            <p style="font-size:14.5px; line-height:1.6; color:#4A5568; margin-bottom:0;">
              Targeted progressive resistance, core proprioceptive stabilization, and myofascial release to restore functional kinetic movement.
            </p>
          </div>

          <div class="bento-card reveal-blur stagger-4" style="background:#FFFFFF; padding:28px; border-radius:18px; border:1px solid #DCE5F5;">
            <div style="font-family:'Recoleta',serif; font-size:32px; font-weight:700; color:#233E85; margin-bottom:12px;">04</div>
            <h3 style="font-size:18px; font-weight:700; margin-bottom:8px; color:#233E85;">Long-term Stabilization</h3>
            <p style="font-size:14.5px; line-height:1.6; color:#4A5568; margin-bottom:0;">
              Customized ergonomic coaching, home maintenance routines, and posture re-education to prevent recurrent pain episodes.
            </p>
          </div>

        </div>
      </div>
    </section>

    <!-- SECTION 3: THE RAJAN'S DIFFERENCE (ROOT-CAUSE VS CONVENTIONAL) - FIXED TIGHT LINE SPACING -->
    <section class="section" style="background:#FAF6EE; padding:72px 0;">
      <div class="container w-container">
        <div style="text-align:center; max-width:760px; margin:0 auto 42px auto;">
          <div class="section-kicker">THE RAJAN'S DIFFERENCE</div>
          <h2 class="heading-2" style="font-size:clamp(30px, 3.8vw, 44px); line-height:1.2 !important; margin:0 0 16px 0;">
            Root-cause healing vs. <span class="highlight highlight--line" style="display:inline; line-height:inherit;">temporary masking.</span>
          </h2>
          <p class="section-subtitle">
            Here is why over 15,000 patients have trusted Dr. Prabhu Rajan since 2009 instead of living on endless medication or undergoing unnecessary surgery.
          </p>
        </div>

        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:28px;">
          <!-- CONVENTIONAL -->
          <div class="reveal-blur stagger-1" style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:20px; padding:32px; ">
            <div style="color:#C53030; font-weight:700; text-transform:uppercase; font-size:12px; letter-spacing:1px; margin-bottom:12px;">Standard Conventional Care</div>
            <h3 style="font-family:'Recoleta',Georgia,serif; font-size:22px; line-height:1.28 !important; color:#2D3748 !important; margin-bottom:18px;">Temporary Masking</h3>
            <ul style="list-style:none; padding:0; margin:0; line-height:2.1; font-size:14.5px; color:#718096;">
              <li style="display:flex; align-items:flex-start; gap:10px; margin-bottom:8px;">
                <span style="color:#C53030; font-weight:700;">&times;</span>
                <span>Painkillers and anti-inflammatory pills that only numb symptoms temporarily</span>
              </li>
              <li style="display:flex; align-items:flex-start; gap:10px; margin-bottom:8px;">
                <span style="color:#C53030; font-weight:700;">&times;</span>
                <span>Advice to wear lifelong neck collars or lumbar belts that weaken muscles</span>
              </li>
              <li style="display:flex; align-items:flex-start; gap:10px; margin-bottom:8px;">
                <span style="color:#C53030; font-weight:700;">&times;</span>
                <span>Premature surgical recommendations for common disc bulges</span>
              </li>
              <li style="display:flex; align-items:flex-start; gap:10px;">
                <span style="color:#C53030; font-weight:700;">&times;</span>
                <span>Pain recurs as soon as medication wears off</span>
              </li>
            </ul>
          </div>

          <!-- RAJAN'S -->
          <div class="reveal-blur stagger-2" style="background:#233E85; color:#FBF5E9; border-radius:20px; padding:32px; ">
            <div style="color:#FEFCBF; font-weight:700; text-transform:uppercase; font-size:12px; letter-spacing:1px; margin-bottom:12px;">Rajan's Clinical Protocol</div>
            <h3 style="font-family:'Recoleta',Georgia,serif; font-size:22px; line-height:1.28 !important; color:#FBF5E9 !important; margin-bottom:18px;">Permanent Root-Cause Recovery</h3>
            <ul style="list-style:none; padding:0; margin:0; line-height:2.1; font-size:14.5px; color:#EEF3FA;">
              <li style="display:flex; align-items:flex-start; gap:10px; margin-bottom:8px;">
                <span style="color:#FEFCBF;">{SVG_CHECK}</span>
                <span>Thorough biomechanical and postural evaluation by Dr. Prabhu Rajan</span>
              </li>
              <li style="display:flex; align-items:flex-start; gap:10px; margin-bottom:8px;">
                <span style="color:#FEFCBF;">{SVG_CHECK}</span>
                <span>Gentle Dorn spinal alignment and targeted laser/shockwave therapy</span>
              </li>
              <li style="display:flex; align-items:flex-start; gap:10px; margin-bottom:8px;">
                <span style="color:#FEFCBF;">{SVG_CHECK}</span>
                <span>Active muscle retraining and ergonomic coaching to prevent recurrence</span>
              </li>
              <li style="display:flex; align-items:flex-start; gap:10px;">
                <span style="color:#FEFCBF;">{SVG_CHECK}</span>
                <span>Lasting mobility and freedom without reliance on pharmaceuticals</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 4: HOME PHYSIOTHERAPY VISITS PROGRAM -->
    <section class="section" style="background:#FFFFFF; padding:72px 0;">
      <div class="container w-container">
        <div class="doorstep-card reveal-blur">
          <div>
            <div class="section-kicker">IN-HOME REHABILITATION</div>
            <h2 class="heading-2" style="font-size:clamp(28px, 3.6vw, 42px); line-height:1.2 !important; color:#233E85 !important; margin:0 0 16px 0;">
              Expert physiotherapy delivered directly to your doorstep.
            </h2>
            <p style="font-size:15.5px; line-height:1.65 !important; color:#4A5568 !important; margin-bottom:22px;">
              For post-surgical patients, elderly family members, stroke survivors, or acute bedridden cases unable to travel to our clinic. Our visiting therapists bring portable ultrasound, electrotherapy, and exercises directly to your bedside.
            </p>
            <div class="doorstep-locations">
              <div class="doorstep-loc-item">{SVG_CHECK} <span>Chromepet</span></div>
              <div class="doorstep-loc-item">{SVG_CHECK} <span>Pallavaram</span></div>
              <div class="doorstep-loc-item">{SVG_CHECK} <span>Tambaram</span></div>
              <div class="doorstep-loc-item">{SVG_CHECK} <span>Chitlapakkam</span></div>
              <div class="doorstep-loc-item">{SVG_CHECK} <span>Hasthinapuram</span></div>
              <div class="doorstep-loc-item">{SVG_CHECK} <span>Radha Nagar</span></div>
            </div>
            <a href="home-physiotherapy.html" class="btn-primary" style="display:inline-flex; align-items:center; gap:8px;">
              <span>Learn About Home Visits</span>
              {SVG_ARROW_RIGHT}
            </a>
          </div>

          <div>
            <div class="photo-card" style="border-radius:18px; overflow:hidden; border:1px solid #EEF2F4; background:#FFFFFF;">
              <img src="assets/images/clinic_entrance.jpg" alt="Home Visit Care Program" class="doorstep-img"/>
              <div style="padding:16px 20px; background:#FFFFFF;">
                <div style="font-size:14px; font-weight:700; color:#233E85; margin-bottom:4px;">Direct Residence Coverage</div>
                <p style="font-size:12.5px; color:#536B88; margin:0; line-height:1.5;">
                  Serving Chromepet, Pallavaram, Tambaram &amp; nearby South Chennai neighborhoods.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 5: CLINIC PHOTO TOUR & ENVIRONMENT -->
    <section class="section" style="background:#FAF6EE; padding:72px 0;">
      <div class="container w-container">
        <div style="text-align:center; max-width:720px; margin:0 auto 42px auto;">
          <div class="section-kicker">OUR CLINICAL FACILITY</div>
          <h2 class="heading-2" style="font-size:clamp(30px, 3.8vw, 44px); line-height:1.2 !important; margin:0 0 16px 0;">
            Take a look inside our <span class="highlight highlight--line" style="display:inline; line-height:inherit;">healing center.</span>
          </h2>
          <p class="section-subtitle">
            Clean, fully equipped, sanitized clinical environment in Chromepet with advanced imported therapeutic consoles.
          </p>
        </div>

        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:20px;">
          <div class="photo-card reveal-blur stagger-1">
            <img src="assets/images/clinic_interior_reception.jpg" alt="Reception & Consultation Desk" style="width:100%; height:220px; object-fit:cover; display:block;"/>
            <div style="padding:14px 18px; font-size:13px; font-weight:600; color:#233E85;">Reception &amp; Consultation Desk</div>
          </div>
          <div class="photo-card reveal-blur stagger-2">
            <img src="assets/images/clinic_treatment_beds.jpg" alt="Scanning Laser Suite" style="width:100%; height:220px; object-fit:cover; display:block;"/>
            <div style="padding:14px 18px; font-size:13px; font-weight:600; color:#233E85;">Scanning Laser &amp; Therapy Suites</div>
          </div>
          <div class="photo-card reveal-blur stagger-3">
            <img src="assets/images/clinic_therapy_equipment.jpg" alt="Electroson 608 Electrotherapy" style="width:100%; height:220px; object-fit:cover; display:block;"/>
            <div style="padding:14px 18px; font-size:13px; font-weight:600; color:#233E85;">Electroson 608 &amp; Shockwave Console</div>
          </div>
          <div class="photo-card reveal-blur stagger-4">
            <img src="assets/images/clinic_consultation_area.jpg" alt="Dorn Spinal Wall Graphics" style="width:100%; height:220px; object-fit:cover; display:block;"/>
            <div style="padding:14px 18px; font-size:13px; font-weight:600; color:#233E85;">Dorn Method Spine Alignment Station</div>
          </div>
        </div>

        <div style="text-align:center; margin-top:32px;">
          <a href="contact.html" class="btn-secondary">
            View Clinic Location &amp; Directions &rarr;
          </a>
        </div>
      </div>
    </section>

    <!-- TESTIMONIALS SECTION -->
    <section class="section" style="background:#233E85; color:#FBF5E9; padding:72px 0;">
      <div class="container w-container">
        <div style="text-align:center; max-width:720px; margin:0 auto 48px auto;">
          <div style="display:inline-flex; align-items:center; gap:6px; color:#FEFCBF; margin-bottom:10px;">
            {SVG_STAR}{SVG_STAR}{SVG_STAR}{SVG_STAR}{SVG_STAR}
          </div>
          <h2 class="heading-2" style="color:#FBF5E9 !important; font-size:clamp(30px, 3.8vw, 44px); line-height:1.2 !important; margin:0 0 16px 0;">
            What our patients say
          </h2>
          <p style="font-size:15.5px; line-height:1.6 !important; color:#EEF3FA !important; margin:0;">
            Real recovery stories from verified Google, Practo, and Justdial reviews.
          </p>
        </div>

        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:24px;">
          <!-- T1 -->
          <div class="testimonial-card reveal-blur stagger-1" style="background:rgba(255,255,255,0.12); border-radius:18px; padding:28px; border:1px solid rgba(255,255,255,0.22); ">
            <div style="display:flex; align-items:center; gap:4px; margin-bottom:14px;">
              {SVG_STAR}{SVG_STAR}{SVG_STAR}{SVG_STAR}{SVG_STAR}
            </div>
            <p class="testimonial-quote" style="font-size:15px; line-height:1.68 !important; color:#FFFFFF !important; margin-bottom:18px; font-style:italic;">
              &ldquo;I suffered from severe lower back pain and sciatica for over 8 months. After just 5 sessions with Dr. Prabhu Rajan using Dorn alignment and laser, I am completely pain-free and back to my daily morning walks.&rdquo;
            </p>
            <div class="testimonial-author" style="font-size:14px; font-weight:700; color:#FEFCBF !important; margin-bottom:4px;">Devi S.P.</div>
            <div class="testimonial-meta" style="font-size:12.5px; color:#E2E8F0 !important;">Verified Practo Review &bull; Sciatica Recovery</div>
          </div>

          <!-- T2 -->
          <div class="testimonial-card reveal-blur stagger-2" style="background:rgba(255,255,255,0.12); border-radius:18px; padding:28px; border:1px solid rgba(255,255,255,0.22); ">
            <div style="display:flex; align-items:center; gap:4px; margin-bottom:14px;">
              {SVG_STAR}{SVG_STAR}{SVG_STAR}{SVG_STAR}{SVG_STAR}
            </div>
            <p class="testimonial-quote" style="font-size:15px; line-height:1.68 !important; color:#FFFFFF !important; margin-bottom:18px; font-style:italic;">
              &ldquo;Dr. Prabhu's clinic is exceptional. He treated my frozen shoulder when other clinics suggested surgery. His patience, manual mobilization skills, and home exercises restored 100% of my arm movement.&rdquo;
            </p>
            <div class="testimonial-author" style="font-size:14px; font-weight:700; color:#FEFCBF !important; margin-bottom:4px;">Mrs. Hema Raman</div>
            <div class="testimonial-meta" style="font-size:12.5px; color:#E2E8F0 !important;">Verified Google Review &bull; Frozen Shoulder</div>
          </div>

          <!-- T3 -->
          <div class="testimonial-card reveal-blur stagger-3" style="background:rgba(255,255,255,0.12); border-radius:18px; padding:28px; border:1px solid rgba(255,255,255,0.22); ">
            <div style="display:flex; align-items:center; gap:4px; margin-bottom:14px;">
              {SVG_STAR}{SVG_STAR}{SVG_STAR}{SVG_STAR}{SVG_STAR}
            </div>
            <p class="testimonial-quote" style="font-size:15px; line-height:1.68 !important; color:#FFFFFF !important; margin-bottom:18px; font-style:italic;">
              &ldquo;Extremely professional care. As a badminton player, my ankle sprain was treated with dry needling and laser therapy. I was back on the court in 2 weeks without any pain or instability.&rdquo;
            </p>
            <div class="testimonial-author" style="font-size:14px; font-weight:700; color:#FEFCBF !important; margin-bottom:4px;">Viswapriya K.</div>
            <div class="testimonial-meta" style="font-size:12.5px; color:#E2E8F0 !important;">Verified Justdial Review &bull; Sports Injury</div>
          </div>
        </div>
      </div>
    </section>

{get_cta_section("")}
  </main>

{get_global_footer("")}"""
    return html


# -------------------------------------------------------------
# 2. CORE PAGES BUILDER (About, Pricing, FAQ, Free Assessment)
# -------------------------------------------------------------
def build_core_pages():
    print("Building updated core pages (About, Pricing, FAQ, Free Assessment)...")
    
    # 1. ABOUT US
    def render_about(depth_prefix):
        asset_prefix = f"{depth_prefix}assets/" if depth_prefix else "assets/"
        home_link = depth_prefix if depth_prefix else "./"
        if not home_link.endswith(('/', 'index.html')):
            home_link = home_link + "index.html" if home_link else "./index.html"
            
        return f"""{get_global_head(
            "About Dr. Prabhu Rajan, PT & Rajan's Physiotherapy Centre | Chromepet Chennai",
            "Learn about Dr. Prabhu Rajan, PT (17 Yrs Exp, MPT Sports, MIAP, Dr.Acu Colombo, Vice Chairman AIDTA) and the history of Rajan's Physiotherapy Centre established in 2009.",
            asset_prefix
        )}
{get_global_nav(depth_prefix, "about")}

  <main>
    <!-- HERO SECTION -->
    <section class="section section--hero" style="background:#FAF6EE; padding:60px 0 72px 0;">
      <div class="container w-container">
        <!-- BREADCRUMB -->
        <div style="font-size:12px; font-weight:600; letter-spacing:0.8px; text-transform:uppercase; margin-bottom:18px; color:#536B88; display:flex; align-items:center; gap:8px;">
          <a href="{home_link}" style="color:#536B88; text-decoration:none;">Home</a>
          <span>/</span>
          <span style="color:#233E85; font-weight:700;">About Dr. Prabhu Rajan &amp; Clinic</span>
        </div>

        <div class="hero-grid">
          <div>
            <div class="clinic-badge">
              {SVG_AWARD} Founder &amp; Chief Physiotherapist
            </div>
            <h1 class="heading-1" style="font-size:clamp(30px, 3.8vw, 44px); line-height:1.18 !important; margin-bottom:16px;">
              Healing through root-cause science, empathy &amp; dedication since 2009.
            </h1>
            <p class="text-lead" style="margin-bottom:20px;">
              Founded by Dr. Prabhu Rajan, PT in Chromepet, Chennai, Rajan's Physiotherapy &amp; Pain Relief Centre was built on a foundational promise: treating the whole human being, not just a pain symptom on a prescription pad.
            </p>
            <p style="font-size:15px; line-height:1.65; color:#4A5568; margin-bottom:24px;">
              Over 17 years of continuous clinical practice, Dr. Prabhu Rajan has spearheaded advanced conservative orthopedic rehabilitation in Chennai—serving as Vice Chairman of the All India Dorn Therapy Association (AIDTA) and pioneering non-surgical spinal realignments.
            </p>
            
            <div style="display:flex; flex-wrap:wrap; gap:14px;">
              <a href="https://wa.me/919042612895?text=Hello%20Dr.%20Prabhu%2C%20I%20would%20like%20to%20consult%20with%20you" target="_blank" class="btn-whatsapp">
                {SVG_WHATSAPP} Consult Dr. Prabhu Rajan
              </a>
              <a href="tel:9042612895" class="btn-secondary">
                {SVG_PHONE} Call Clinic Directly
              </a>
            </div>
          </div>

          <div>
            <div class="photo-card" style="">
              <img src="{asset_prefix}images/dr_prabhu_rajan_profile.jpg" alt="Dr. Prabhu Rajan, PT" style="width:100%; height:440px; object-fit:cover; display:block;" loading="eager"/>
              <div style="padding:18px 22px; background:#FFFFFF; border-top:1px solid #EEF2F4;">
                <h4 style="font-family:'Recoleta',Georgia,serif; font-size:18px; line-height:1.24 !important; color:#233E85 !important; margin:0 0 4px 0;">
                  Dr. Prabhu Rajan, PT (Dr. Prabhu R, PT)
                </h4>
                <p style="font-size:13px; color:#536B88; margin:0;">
                  BPT &bull; MPT (Sports) &bull; Dr.Acu (Colombo) &bull; CDNT (USA) &bull; MIAP L-27944
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CREDENTIALS BENTO -->
    <section class="section" style="background:#FFFFFF; padding:72px 0;">
      <div class="container w-container">
        <div style="text-align:center; max-width:720px; margin:0 auto 48px auto;">
          <div class="section-kicker">CLINICAL EXCELLENCE</div>
          <h2 class="heading-2" style="font-size:clamp(30px, 3.8vw, 44px); line-height:1.2 !important; margin:0 0 16px 0;">
            Qualifications, Honors &amp; Leadership
          </h2>
          <p class="section-subtitle">
            Rigorous international and national training backed by 17 years of patient-first orthopedic experience.
          </p>
        </div>

        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:24px;">
          <div class="bento-card reveal-blur stagger-1">
            <div style="width:40px; height:40px; border-radius:10px; background:#EEF3FA; display:flex; align-items:center; justify-content:center; margin-bottom:14px;">
              {SVG_AWARD}
            </div>
            <h3 style="font-family:'Recoleta',Georgia,serif; font-size:18px; line-height:1.28 !important; color:#233E85 !important; margin-bottom:8px;">
              Vice Chairman, AIDTA
            </h3>
            <p style="font-size:14px; line-height:1.6; color:#4A5568; margin:0;">
              Vice Chairman of the All India Dorn Therapy Association, training physiotherapists across India in gentle dynamic spinal realignment.
            </p>
          </div>

          <div class="bento-card reveal-blur stagger-2">
            <div style="width:40px; height:40px; border-radius:10px; background:#EEF3FA; display:flex; align-items:center; justify-content:center; margin-bottom:14px;">
              {SVG_ACTIVITY}
            </div>
            <h3 style="font-family:'Recoleta',Georgia,serif; font-size:18px; line-height:1.28 !important; color:#233E85 !important; margin-bottom:8px;">
              MPT in Sports Physiotherapy (2013)
            </h3>
            <p style="font-size:14px; line-height:1.6; color:#4A5568; margin:0;">
              Master's degree specializing in athletic injury kinematics, high-speed ligament strain rehabilitation, and return-to-sport protocols.
            </p>
          </div>

          <div class="bento-card reveal-blur stagger-3">
            <div style="width:40px; height:40px; border-radius:10px; background:#EEF3FA; display:flex; align-items:center; justify-content:center; margin-bottom:14px;">
              {SVG_NEEDLE}
            </div>
            <h3 style="font-family:'Recoleta',Georgia,serif; font-size:18px; line-height:1.28 !important; color:#233E85 !important; margin-bottom:8px;">
              Certified Dry Needling (CDNT, USA)
            </h3>
            <p style="font-size:14px; line-height:1.6; color:#4A5568; margin:0;">
              Certified in myofascial trigger point dry needling under US curriculum, precision neuro-muscular release for deep knots.
            </p>
          </div>

          <div class="bento-card reveal-blur stagger-4">
            <div style="width:40px; height:40px; border-radius:10px; background:#EEF3FA; display:flex; align-items:center; justify-content:center; margin-bottom:14px;">
              {SVG_SHIELD}
            </div>
            <h3 style="font-family:'Recoleta',Georgia,serif; font-size:18px; line-height:1.28 !important; color:#233E85 !important; margin-bottom:8px;">
              Doctor of Acupuncture (Dr.Acu, Colombo 2012)
            </h3>
            <p style="font-size:14px; line-height:1.6; color:#4A5568; margin:0;">
              International clinical training in neuro-acupuncture and micro-meridian stimulation from Colombo, Sri Lanka.
            </p>
          </div>

          <div class="bento-card reveal-blur stagger-5">
            <div style="width:40px; height:40px; border-radius:10px; background:#EEF3FA; display:flex; align-items:center; justify-content:center; margin-bottom:14px;">
              {SVG_CHECK}
            </div>
            <h3 style="font-family:'Recoleta',Georgia,serif; font-size:18px; line-height:1.28 !important; color:#233E85 !important; margin-bottom:8px;">
              Life Member, IAP (L-27944)
            </h3>
            <p style="font-size:14px; line-height:1.6; color:#4A5568; margin:0;">
              Registered life member of the Indian Association of Physiotherapists, upholding strict medical ethics and patient safety codes.
            </p>
          </div>

          <div class="bento-card reveal-blur stagger-6">
            <div style="width:40px; height:40px; border-radius:10px; background:#EEF3FA; display:flex; align-items:center; justify-content:center; margin-bottom:14px;">
              {SVG_HOME}
            </div>
            <h3 style="font-family:'Recoleta',Georgia,serif; font-size:18px; line-height:1.28 !important; color:#233E85 !important; margin-bottom:8px;">
              Clinical Team &amp; Home Visits
            </h3>
            <p style="font-size:14px; line-height:1.6; color:#4A5568; margin:0;">
              Co-supported by senior associate therapists including Dr. Ravi, PT (BPT), offering seamless in-clinic and at-home continuity.
            </p>
          </div>
        </div>
      </div>
    </section>

{get_cta_section(depth_prefix)}
  </main>

{get_global_footer(depth_prefix)}"""

    # 2. PRICING & FEES
    def render_pricing(depth_prefix):
        asset_prefix = f"{depth_prefix}assets/" if depth_prefix else "assets/"
        home_link = depth_prefix if depth_prefix else "./"
        if not home_link.endswith(('/', 'index.html')):
            home_link = home_link + "index.html" if home_link else "./index.html"

        return f"""{get_global_head(
            "Transparent Consultation & Treatment Pricing | Rajan's Physio Chromepet",
            "Clear, honest pricing at Rajan's Physiotherapy Centre Chromepet. Initial consultation ₹600, treatment sessions ₹400-₹800, home visits ₹800-₹1,200.",
            asset_prefix
        )}
{get_global_nav(depth_prefix, "pricing")}

  <main>
    <!-- HERO SECTION -->
    <section class="section section--hero" style="background:#FAF6EE; padding:60px 0 64px 0;">
      <div class="container w-container">
        <!-- BREADCRUMB -->
        <div style="font-size:12px; font-weight:600; letter-spacing:0.8px; text-transform:uppercase; margin-bottom:18px; color:#536B88; display:flex; align-items:center; gap:8px;">
          <a href="{home_link}" style="color:#536B88; text-decoration:none;">Home</a>
          <span>/</span>
          <span style="color:#233E85; font-weight:700;">Pricing &amp; Consultation Fees</span>
        </div>

        <div style="text-align:center; max-width:760px; margin:0 auto 48px auto;">
          <div class="clinic-badge">
            {SVG_CHECK} Transparent &bull; No Hidden Charges &bull; Fair Healthcare
          </div>
          <h1 class="heading-1" style="font-size:clamp(32px, 4vw, 44px); line-height:1.18 !important; margin-bottom:16px;">
            Honest, transparent clinical fees.
          </h1>
          <p class="section-subtitle">
            We believe world-class conservative physiotherapy should be accessible and predictable. You will always know what treatment involves and what it costs upfront.
          </p>
        </div>

        <!-- 3 PRICING TIERS -->
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:28px; margin-bottom:48px;">
          <!-- TIER 1 -->
          <div class="service-card reveal-blur stagger-1" style="padding:32px; background:#FFFFFF;">
            <div>
              <div style="font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:1px; color:#536B88; margin-bottom:8px;">FIRST VISIT</div>
              <h3 style="font-family:'Recoleta',Georgia,serif; font-size:24px; line-height:1.24 !important; color:#233E85 !important; margin-bottom:12px;">Initial Assessment</h3>
              <div style="display:flex; align-items:baseline; gap:6px; margin-bottom:16px;">
                <span data-counter="600" data-prefix="₹" style="font-family:'Recoleta',Georgia,serif; font-size:38px; font-weight:700; color:#233E85;">&#8377;600</span>
                <span style="font-size:13px; color:#718096;">/ comprehensive consult</span>
              </div>
              <p style="font-size:14px; line-height:1.6; color:#4A5568; margin-bottom:20px;">
                Complete 45-minute clinical evaluation directly by Dr. Prabhu Rajan, PT. Includes orthopedic tests, spinal posture check &amp; treatment plan.
              </p>
              <ul style="list-style:none; padding:0; margin:0 0 24px 0; font-size:13.5px; line-height:2.1; color:#4A5568;">
                <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Full biomechanical movement test</li>
                <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Spine, pelvic &amp; limb alignment check</li>
                <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Review of X-rays / MRI reports</li>
                <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} First day pain-relief modality</li>
              </ul>
            </div>
            <a href="https://wa.me/919042612895?text=Hello%20Dr.%20Prabhu%2C%20I%20would%20like%20to%20book%20an%20initial%20consultation" target="_blank" class="btn-primary" style="justify-content:center;">
              Book Initial Visit
            </a>
          </div>

          <!-- TIER 2: POPULAR -->
          <div class="service-card reveal-blur stagger-2" style="padding:32px; background:#233E85; color:#FBF5E9; border-color:#233E85; ">
            <div>
              <div style="display:inline-block; background:#FEFCBF; color:#744210; font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:1px; padding:3px 10px; border-radius:20px; margin-bottom:8px;">MOST COMMON</div>
              <h3 style="font-family:'Recoleta',Georgia,serif; font-size:24px; line-height:1.24 !important; color:#FBF5E9 !important; margin-bottom:12px;">Therapy Session</h3>
              <div style="display:flex; align-items:baseline; gap:6px; margin-bottom:16px;">
                <span style="font-family:'Recoleta',Georgia,serif; font-size:38px; font-weight:700; color:#FBF5E9;">&#8377;400 &ndash; &#8377;800</span>
                <span style="font-size:13px; color:#EEF3FA;">/ session</span>
              </div>
              <p style="font-size:14px; line-height:1.6; color:#EEF3FA; margin-bottom:20px;">
                Personalized hands-on therapy session integrating advanced modalities (Laser, Dorn alignment, Shockwave, Dry Needling, IFT).
              </p>
              <ul style="list-style:none; padding:0; margin:0 0 24px 0; font-size:13.5px; line-height:2.1; color:#FBF5E9;">
                <li style="display:flex; align-items:center; gap:8px;"><span style="color:#FEFCBF;">{SVG_CHECK}</span> 40 &ndash; 60 mins 1-on-1 care</li>
                <li style="display:flex; align-items:center; gap:8px;"><span style="color:#FEFCBF;">{SVG_CHECK}</span> Targeted physical modalities included</li>
                <li style="display:flex; align-items:center; gap:8px;"><span style="color:#FEFCBF;">{SVG_CHECK}</span> Dorn spinal mobilization &amp; stretching</li>
                <li style="display:flex; align-items:center; gap:8px;"><span style="color:#FEFCBF;">{SVG_CHECK}</span> Progress tracking every session</li>
              </ul>
            </div>
            <a href="https://wa.me/919042612895?text=Hello%20Dr.%20Prabhu%2C%20I%20would%20like%20to%20schedule%20a%20therapy%20session" target="_blank" class="btn-whatsapp" style="justify-content:center; background:#FEFCBF; color:#233E85 !important;">
              {SVG_WHATSAPP} Schedule Session
            </a>
          </div>

          <!-- TIER 3: HOME VISITS -->
          <div class="service-card reveal-blur stagger-3" style="padding:32px; background:#FFFFFF;">
            <div>
              <div style="font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:1px; color:#536B88; margin-bottom:8px;">DOORSTEP CARE</div>
              <h3 style="font-family:'Recoleta',Georgia,serif; font-size:24px; line-height:1.24 !important; color:#233E85 !important; margin-bottom:12px;">In-Home Visit</h3>
              <div style="display:flex; align-items:baseline; gap:6px; margin-bottom:16px;">
                <span style="font-family:'Recoleta',Georgia,serif; font-size:38px; font-weight:700; color:#233E85;">&#8377;800 &ndash; &#8377;1,200</span>
                <span style="font-size:13px; color:#718096;">/ visit</span>
              </div>
              <p style="font-size:14px; line-height:1.6; color:#4A5568; margin-bottom:20px;">
                Doctor-supervised home physiotherapy for post-surgery, bedridden, stroke, or elderly patients in Chromepet, Pallavaram &amp; Tambaram.
              </p>
              <ul style="list-style:none; padding:0; margin:0 0 24px 0; font-size:13.5px; line-height:2.1; color:#4A5568;">
                <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Bedside clinical rehabilitation</li>
                <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Portable ultrasound &amp; electrotherapy</li>
                <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Gait training &amp; transfer assistance</li>
                <li style="display:flex; align-items:center; gap:8px;">{SVG_CHECK} Family &amp; caregiver coaching</li>
              </ul>
            </div>
            <a href="home-physiotherapy.html" class="btn-secondary" style="justify-content:center;">
              Explore Home Visits
            </a>
          </div>
        </div>
      </div>
    </section>

{get_cta_section(depth_prefix)}
  </main>

{get_global_footer(depth_prefix)}"""

    # 3. FAQ PAGE
    def render_faq(depth_prefix):
        asset_prefix = f"{depth_prefix}assets/" if depth_prefix else "assets/"
        home_link = depth_prefix if depth_prefix else "./"
        if not home_link.endswith(('/', 'index.html')):
            home_link = home_link + "index.html" if home_link else "./index.html"

        return f"""{get_global_head(
            "Frequently Asked Clinical Questions | Rajan's Physio Chromepet",
            "Get detailed answers to common clinical questions about physiotherapy, Dorn spinal alignment, laser therapy, home visits, and appointments at Rajan's Physio.",
            asset_prefix
        )}
{get_global_nav(depth_prefix, "faq")}

  <main>
    <!-- HERO SECTION -->
    <section class="section section--hero" style="background:#FAF6EE; padding:60px 0 64px 0;">
      <div class="container w-container">
        <!-- BREADCRUMB -->
        <div style="font-size:12px; font-weight:600; letter-spacing:0.8px; text-transform:uppercase; margin-bottom:18px; color:#536B88; display:flex; align-items:center; gap:8px;">
          <a href="{home_link}" style="color:#536B88; text-decoration:none;">Home</a>
          <span>/</span>
          <span style="color:#233E85; font-weight:700;">Frequently Asked Questions</span>
        </div>

        <div style="text-align:center; max-width:760px; margin:0 auto 48px auto;">
          <div class="clinic-badge">
            {SVG_SHIELD} Patient Transparency &amp; Medical Guidance
          </div>
          <h1 class="heading-1" style="font-size:clamp(32px, 4vw, 44px); line-height:1.18 !important; margin-bottom:16px;">
            Frequently Asked Questions
          </h1>
          <p class="section-subtitle">
            Clear, honest answers to help you prepare for your consultation and understand our clinical treatment methodologies.
          </p>
        </div>

        <!-- FAQ LIST -->
        <div style="max-width:820px; margin:0 auto;">
          <div class="faq-item reveal-blur">
            <div class="faq-q"><span>Do I need a doctor's referral to visit Rajan's Physiotherapy?</span><span class="faq-icon">+</span></div>
            <div class="faq-a">No referral is required. In India, qualified physiotherapists are primary healthcare practitioners capable of independent musculoskeletal assessment. If you already have doctor notes, X-rays, or MRI scans, please bring them along.</div>
          </div>
          <div class="faq-item reveal-blur">
            <div class="faq-q"><span>How does the Dorn Method differ from chiropractic cracking?</span><span class="faq-icon">+</span></div>
            <div class="faq-a">Chiropractic manipulation typically uses sudden, high-velocity passive thrusts that can cause reflexive muscle guarding. The Dorn Method is gentle, active, and dynamic: Dr. Prabhu Rajan realigns vertebrae with gentle thumb pressure while you actively swing your arm or leg, keeping muscles relaxed and ligaments protected.</div>
          </div>
          <div class="faq-item reveal-blur">
            <div class="faq-q"><span>How many sessions will I need before I see results?</span><span class="faq-icon">+</span></div>
            <div class="faq-a">Many patients experience significant relief after the very first or second session. Acute muscle spasms or recent sprains often resolve in 3 to 5 sessions. Chronic degenerative conditions, such as severe lumbar disc bulges or frozen shoulder, usually require 6 to 10 sessions combined with home exercises.</div>
          </div>
          <div class="faq-item reveal-blur">
            <div class="faq-q"><span>What should I wear for my physiotherapy consultation?</span><span class="faq-icon">+</span></div>
            <div class="faq-a">Wear comfortable, loose-fitting clothing that allows easy movement and access to the affected area (e.g., shorts or track pants for knee/back pain, or a sleeveless shirt for shoulder problems).</div>
          </div>
          <div class="faq-item reveal-blur">
            <div class="faq-q"><span>Can older adults or patients with osteoporosis receive treatment?</span><span class="faq-icon">+</span></div>
            <div class="faq-a">Absolutely. Our treatments are tailored to bone density and medical history. We utilize gentle Dorn alignments without thrusts, soothing therapeutic ultrasound, scanning laser, and gentle joint mobilization that are 100% safe for elderly patients.</div>
          </div>
          <div class="faq-item reveal-blur">
            <div class="faq-q"><span>How do I book an in-home physiotherapy visit?</span><span class="faq-icon">+</span></div>
            <div class="faq-a">Simply message or call us at +91 90426 12895. Provide your address and patient condition. We service Chromepet, Pallavaram, Tambaram, Chitlapakkam, and Hasthinapuram.</div>
          </div>
        </div>
      </div>
    </section>

{get_cta_section(depth_prefix)}
  </main>

{get_global_footer(depth_prefix)}"""

    # 4. FREE PAIN ASSESSMENT / CHECKER
    def render_checker(depth_prefix):
        asset_prefix = f"{depth_prefix}assets/" if depth_prefix else "assets/"
        home_link = depth_prefix if depth_prefix else "./"
        if not home_link.endswith(('/', 'index.html')):
            home_link = home_link + "index.html" if home_link else "./index.html"

        return f"""{get_global_head(
            "Free Online Pain Assessment & Symptom Checker | Rajan's Physio",
            "Take our 2-minute clinical symptom assessment to understand your pain pattern and receive personalized guidance from Dr. Prabhu Rajan on WhatsApp.",
            asset_prefix
        )}
{get_global_nav(depth_prefix, "checker")}

  <main>
    <!-- HERO SECTION -->
    <section class="section section--hero" style="background:#FAF6EE; padding:60px 0 64px 0;">
      <div class="container w-container">
        <!-- BREADCRUMB -->
        <div style="font-size:12px; font-weight:600; letter-spacing:0.8px; text-transform:uppercase; margin-bottom:18px; color:#536B88; display:flex; align-items:center; gap:8px;">
          <a href="{home_link}" style="color:#536B88; text-decoration:none;">Home</a>
          <span>/</span>
          <span style="color:#233E85; font-weight:700;">Free Pain Symptom Checker</span>
        </div>

        <div style="text-align:center; max-width:760px; margin:0 auto 40px auto;">
          <div class="clinic-badge">
            {SVG_CROSSHAIR} 2-Minute Biomechanical Triage
          </div>
          <h1 class="heading-1" style="font-size:clamp(32px, 4vw, 44px); line-height:1.18 !important; margin-bottom:16px;">
            Free Pain Assessment &amp; Symptom Checker
          </h1>
          <p class="section-subtitle">
            Select your pain characteristics below. Our system will summarize your presentation for direct review by Dr. Prabhu Rajan, PT.
          </p>
        </div>

        <!-- INTERACTIVE CHECKER FORM -->
        <div style="max-width:720px; margin:0 auto; background:#FFFFFF; border-radius:22px; padding:36px;  border:1px solid #EEF2F4;">
          <form onsubmit="event.preventDefault(); var a=document.querySelector('input[name=area]:checked')?.value || 'Not selected'; var d=document.querySelector('input[name=duration]:checked')?.value || 'Not selected'; var n=document.getElementById('p_name').value; var msg='Hello Dr. Prabhu, I completed the Pain Checker:%0A- Name: ' + encodeURIComponent(n) + '%0A- Pain Area: ' + encodeURIComponent(a) + '%0A- Duration: ' + encodeURIComponent(d); window.open('https://wa.me/919042612895?text=' + msg, '_blank');">
            
            <div style="margin-bottom:24px;">
              <label style="display:block; font-family:'Recoleta',Georgia,serif; font-size:18px; color:#233E85; margin-bottom:12px; font-weight:700;">
                1. Where is your primary pain located?
              </label>
              <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:10px;">
                <label style="display:flex; align-items:center; gap:10px; padding:12px 16px; border:1px solid #E2E8F0; border-radius:10px; cursor:pointer; font-size:14px;">
                  <input type="radio" name="area" value="Lower Back / Sciatica" required style="accent-color:#233E85;"/> Lower Back / Sciatica
                </label>
                <label style="display:flex; align-items:center; gap:10px; padding:12px 16px; border:1px solid #E2E8F0; border-radius:10px; cursor:pointer; font-size:14px;">
                  <input type="radio" name="area" value="Neck / Cervical / Headaches" style="accent-color:#233E85;"/> Neck / Tech Neck
                </label>
                <label style="display:flex; align-items:center; gap:10px; padding:12px 16px; border:1px solid #E2E8F0; border-radius:10px; cursor:pointer; font-size:14px;">
                  <input type="radio" name="area" value="Shoulder / Frozen Shoulder" style="accent-color:#233E85;"/> Shoulder / Rotator Cuff
                </label>
                <label style="display:flex; align-items:center; gap:10px; padding:12px 16px; border:1px solid #E2E8F0; border-radius:10px; cursor:pointer; font-size:14px;">
                  <input type="radio" name="area" value="Knee / Osteoarthritis" style="accent-color:#233E85;"/> Knee / Cartilage Wear
                </label>
                <label style="display:flex; align-items:center; gap:10px; padding:12px 16px; border:1px solid #E2E8F0; border-radius:10px; cursor:pointer; font-size:14px;">
                  <input type="radio" name="area" value="Heel / Plantar Fasciitis" style="accent-color:#233E85;"/> Heel / Plantar Fasciitis
                </label>
                <label style="display:flex; align-items:center; gap:10px; padding:12px 16px; border:1px solid #E2E8F0; border-radius:10px; cursor:pointer; font-size:14px;">
                  <input type="radio" name="area" value="Sports Injury / Post-Surgery" style="accent-color:#233E85;"/> Sports / Post-Surgery
                </label>
              </div>
            </div>

            <div style="margin-bottom:24px;">
              <label style="display:block; font-family:'Recoleta',Georgia,serif; font-size:18px; color:#233E85; margin-bottom:12px; font-weight:700;">
                2. How long have you experienced this discomfort?
              </label>
              <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:10px;">
                <label style="display:flex; align-items:center; gap:10px; padding:12px 16px; border:1px solid #E2E8F0; border-radius:10px; cursor:pointer; font-size:14px;">
                  <input type="radio" name="duration" value="Less than 2 weeks (Acute)" required style="accent-color:#233E85;"/> Less than 2 weeks
                </label>
                <label style="display:flex; align-items:center; gap:10px; padding:12px 16px; border:1px solid #E2E8F0; border-radius:10px; cursor:pointer; font-size:14px;">
                  <input type="radio" name="duration" value="1 to 3 months (Subacute)" style="accent-color:#233E85;"/> 1 to 3 months
                </label>
                <label style="display:flex; align-items:center; gap:10px; padding:12px 16px; border:1px solid #E2E8F0; border-radius:10px; cursor:pointer; font-size:14px;">
                  <input type="radio" name="duration" value="Over 3 months (Chronic)" style="accent-color:#233E85;"/> Over 3 months (Chronic)
                </label>
              </div>
            </div>

            <div style="margin-bottom:24px;">
              <label style="display:block; font-family:'Recoleta',Georgia,serif; font-size:18px; color:#233E85; margin-bottom:8px; font-weight:700;">
                3. Your Name
              </label>
              <input type="text" id="p_name" required placeholder="e.g. Anand Sharma" style="width:100%; padding:12px 16px; border:1px solid #CBD5E0; border-radius:10px; font-size:14px; outline:none;"/>
            </div>

            <button type="submit" class="btn-whatsapp" style="width:100%; justify-content:center; padding:14px; font-size:15px;">
              {SVG_WHATSAPP} Send Assessment to Dr. Prabhu Rajan via WhatsApp &rarr;
            </button>
          </form>
        </div>
      </div>
    </section>

{get_cta_section(depth_prefix)}
  </main>

{get_global_footer(depth_prefix)}"""

    core_files = [
        ("about.html", render_about("")),
        (os.path.join("about", "index.html"), render_about("../")),
        ("pricing.html", render_pricing("")),
        (os.path.join("pricing", "index.html"), render_pricing("../")),
        ("faq.html", render_faq("")),
        (os.path.join("faq", "index.html"), render_faq("../")),
        ("free-assessment.html", render_checker("")),
        (os.path.join("free-assessment", "index.html"), render_checker("../")),
    ]

    for rel_path, content in core_files:
        full_path = os.path.join(ROOT_DIR, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated core: {rel_path} ({len(content)} bytes)")


# -------------------------------------------------------------
# 3. MASTER EXECUTION
# -------------------------------------------------------------
def build_everything():
    print("=== BUILDING ENTIRE RAJAN'S PHYSIO WEBSITE ===")
    
    # 1. Homepage
    home_html = render_homepage()
    with open(os.path.join(ROOT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(home_html)
    print(f"Generated: index.html ({len(home_html)} bytes)")

    # 2. Core Pages
    build_core_pages()

    # 3. 10 Specialized Clinical & Contact Pages
    print("Generating 10 specialized service & contact pages...")
    for s in SERVICES_DATA:
        slug = s["slug"]
        root_html = render_service_page(s, "")
        sub_html = render_service_page(s, "../")
        with open(os.path.join(ROOT_DIR, f"{slug}.html"), "w", encoding="utf-8") as f:
            f.write(root_html)
        sub_path = os.path.join(ROOT_DIR, slug, "index.html")
        os.makedirs(os.path.dirname(sub_path), exist_ok=True)
        with open(sub_path, "w", encoding="utf-8") as f:
            f.write(sub_html)
        print(f"Generated service: {slug}.html & {slug}/index.html")

    contact_root = render_contact_page("")
    contact_sub = render_contact_page("../")
    with open(os.path.join(ROOT_DIR, "contact.html"), "w", encoding="utf-8") as f:
        f.write(contact_root)
    contact_sub_path = os.path.join(ROOT_DIR, "contact", "index.html")
    os.makedirs(os.path.dirname(contact_sub_path), exist_ok=True)
    with open(contact_sub_path, "w", encoding="utf-8") as f:
        f.write(contact_sub)
    print("Generated contact: contact.html & contact/index.html")

    print("\nALL PAGES SUCCESSFULLY GENERATED!")


if __name__ == "__main__":
    build_everything()