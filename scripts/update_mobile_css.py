import os

css_path = os.path.abspath('assets/css/clinic-custom.css')
with open(css_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos_start = text.find('/* 12. Responsive Adjustments */')
pos_end = text.find('/* ========================================================\n   DYNAMIC ANIMATIONS', pos_start)
if pos_end == -1:
    pos_end = text.find('/* ========================================================\r\n   DYNAMIC ANIMATIONS', pos_start)

assert pos_start != -1 and pos_end != -1, f"Positions not found: {pos_start}, {pos_end}"

mobile_css = """/* 12. Complete Mobile & Tablet Responsive Optimizations */
@media (max-width: 991px) {
  .section {
    padding: 48px 0 !important;
  }
  .section--hero {
    padding: 44px 0 52px 0 !important;
  }
  .footer__grid {
    grid-template-columns: 1fr 1fr !important;
    gap: 36px !important;
  }
}

@media (max-width: 767px) {
  /* Mobile Spacings & Typography */
  .section {
    padding: 38px 0 !important;
  }
  .section--hero {
    padding: 36px 0 44px 0 !important;
  }
  .container {
    padding-left: 16px !important;
    padding-right: 16px !important;
  }
  h1, .heading-1 {
    font-size: clamp(24px, 6.2vw, 32px) !important;
    line-height: 1.2 !important;
    margin-bottom: 12px !important;
  }
  h2, .heading-2 {
    font-size: clamp(20px, 5.2vw, 26px) !important;
    line-height: 1.22 !important;
    margin-bottom: 12px !important;
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
  }

  /* Mobile Navbar & Brand */
  .navbar {
    padding: 8px 0 !important;
  }
  .navbar .brand img {
    height: 38px !important;
    width: 38px !important;
  }
  .navbar .brand span:first-child {
    font-size: 15.5px !important;
  }
  .navbar .brand span:last-child {
    font-size: 9px !important;
  }

  /* Mobile Cards & Bento Grids */
  .service-card, .bento-card, .testimonial-card {
    padding: 20px 18px !important;
    border-radius: 14px !important;
  }
  
  /* Mobile Streamlined Footer (Clean Vertical Flow) */
  .footer__grid {
    grid-template-columns: 1fr !important;
    gap: 28px !important;
  }
  .footer {
    padding: 44px 0 24px 0 !important;
  }
  .footer-subbar {
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    gap: 12px !important;
    padding-top: 18px !important;
  }

  /* Mobile Floating Buttons (No Overlap & Zero Shadows) */
  #floating-whatsapp {
    bottom: 16px !important;
    left: 16px !important;
    padding: 9px 15px !important;
    font-size: 12.5px !important;
    border-radius: 24px !important;
    box-shadow: none !important;
  }
  #back-to-top {
    bottom: 16px !important;
    right: 16px !important;
    width: 38px !important;
    height: 38px !important;
    box-shadow: none !important;
  }

  /* Mobile Touch-Friendly Buttons */
  .btn-primary, .btn-secondary, .btn-whatsapp, .btn-magenta {
    padding: 11px 20px !important;
    font-size: 13.5px !important;
    width: 100% !important;
    justify-content: center !important;
  }

  /* Lightweight Mobile Reveal (Smooth & Battery Friendly) */
  .reveal-blur {
    filter: blur(10px) !important;
    transform: translateY(22px) scale(0.98) !important;
    transition-duration: 0.85s !important;
  }
}

"""

new_text = text[:pos_start] + mobile_css + text[pos_end:]
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updated mobile responsive CSS successfully.")
