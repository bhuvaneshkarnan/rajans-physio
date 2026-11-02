# Rajan's Physiotherapy & Pain Relief Centre

Official website for **Rajan's Physiotherapy & Pain Relief Centre**, located in Chromepet, Chennai. Established in 2009 and led by **Dr. Prabhu Rajan, PT** (17+ years clinical experience, MPT Sports, MIAP L-27944, Vice Chairman of All India Dorn Therapy Association).

Designed and developed by **[Boldlabs](https://goboldlabs.com)**.

---

## Clinical Services & Treatments
1. **Dorn Method Spinal Alignment** &mdash; Gentle, dynamic non-manipulative joint and vertebral realignment.
2. **LASERSTIM Scanning Laser Therapy** &mdash; Deep cellular photobiomodulation for acute inflammation and nerve recovery.
3. **Radial Shockwave Therapy (ESWT)** &mdash; Acoustic shockwaves for chronic calcific tendonitis, heel spurs, and plantar fasciitis.
4. **Clinical Dry Needling (CDNT USA)** &mdash; Deep muscular trigger point release and myofascial pain alleviation.
5. **TECAR Radiofrequency Therapy** &mdash; 448 kHz targeted cellular bio-stimulation for rapid sports injury recovery.
6. **Kinesio Cupping & IASTM** &mdash; Negative-pressure myofascial decompression and stainless-steel instrument-assisted soft tissue mobilization.
7. **Electrotherapy & Clinical Ultrasound** &mdash; Multi-frequency interferential (IFT), TENS, and ultrasonic tissue healing.
8. **Sports Injury Rehabilitation** &mdash; ACL rehabilitation, meniscus recovery, ankle sprain protocols, and athletic re-conditioning.
9. **In-Home Physiotherapy Program** &mdash; Full clinical care delivered to patients' homes across Chromepet, Tambaram, Pallavaram, and Sanatorium.

---

## Architecture & Technology Stack
- **Architecture**: 100% static HTML5, CSS3, and vanilla JavaScript.
- **Dual Routing Compatibility**: Every route is dual-published as both `[page].html` and `[page]/index.html` to guarantee instant compatibility across any static host (GitHub Pages, Vercel, Netlify, Apache, Nginx, or local `file://` opening).
- **Self-Hosted Assets**: 0 external CDN dependencies; all fonts (Work Sans, Recoleta), images, and icons are completely self-hosted in `assets/`.
- **Flat Modern Design**: Strict zero-shadow policy (`box-shadow: none !important; text-shadow: none !important;`).
- **Brand Palette**:
  - Primary Royal Navy: `#233E85`
  - Vibrant Brand Magenta: `#ED1D7F`
  - Warm Organic Heading Underline: `#FACD71`
  - Ice Navy Tint: `#EEF3FA` / Blush Magenta Tint: `#FDF2F7`
  - WhatsApp Action Green: `#25D366`
- **Performance & Animations**:
  - Smooth scroll reveal with gentle unblurring (`assets/js/clinic-dynamic.js`).
  - Staggered card transitions.
  - Number counter animations with cubic ease-out.
  - Interactive FAQ accordion transitions.
  - Sticky navbar with backdrop blur.
  - Persistent, shadow-free floating WhatsApp consultation button.

---

## Directory Structure
```
├── assets/
│   ├── css/
│   │   ├── clinic-custom.css     # Brand tokens, responsive typography, flat styling
│   │   └── dreamlab.webflow.css  # Core layout grid and base reset
│   ├── js/
│   │   ├── clinic-dynamic.js     # Smooth reveal, counters, FAQ, floating WhatsApp
│   │   ├── jquery.min.js
│   │   └── webflow.js
│   └── images/                   # Clinic logo, treatment illustrations, room photos
├── scripts/                      # Python automated generators and verification suite
├── about.html & about/
├── contact.html & contact/
├── pricing.html & pricing/
├── faq.html & faq/
├── free-assessment.html & free-assessment/
├── [service-slug].html & [service-slug]/
└── index.html                    # Homepage with 4-step protocol and clinical bento
```

---

## Author & Attribution
- **Clinic**: Rajan's Physiotherapy & Pain Relief Centre (Est. 2009)
- **Lead Physiotherapist**: Dr. Prabhu Rajan, PT
- **Designed & Developed by**: [Boldlabs](https://goboldlabs.com)
