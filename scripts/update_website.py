import os
import re
import json
from bs4 import BeautifulSoup

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

with open(os.path.join(ROOT_DIR, 'extracted_data', 'clinic_data.json'), 'r', encoding='utf-8') as f:
    clinic_data = json.load(f)

# Helper function to create the clinic logo HTML
def get_brand_html(depth_prefix):
    return f"""<a href="{depth_prefix or './'}" title="Rajan's Physiotherapy &amp; Pain Relief Centre" class="brand w-nav-brand" style="text-decoration:none; display:flex; align-items:center; gap:12px;">
      <div style="width:42px; height:42px; border-radius:50%; background:#19535F; color:#FBF5E9; display:flex; align-items:center; justify-content:center; font-family:'Recoleta',serif; font-size:22px; font-weight:700; box-shadow:0 2px 6px rgba(25,83,95,0.2);">R</div>
      <div style="display:flex; flex-direction:column;">
        <span style="font-family:'Recoleta',serif; font-size:18px; font-weight:700; color:#19535F; line-height:1.15;">Rajan's Physiotherapy</span>
        <span style="font-size:11px; letter-spacing:0.5px; color:#5A6E72; text-transform:uppercase; font-weight:500;">&amp; Pain Relief Centre &bull; Since 2009</span>
      </div>
    </a>"""

# Helper function to create standard footer HTML
def get_footer_html(depth_prefix):
    return f"""<footer class="footer">
      <div class="container w-container">
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap:40px; margin-bottom:50px;">
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

print("Helper functions ready.")
