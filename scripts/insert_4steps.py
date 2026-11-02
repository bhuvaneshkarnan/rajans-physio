import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
master_path = os.path.join(ROOT_DIR, 'scripts', 'build_full_website_master.py')

with open(master_path, 'r', encoding='utf-8') as f:
    text = f.read()

marker = '<span>Explore Cupping &amp; IASTM</span> {SVG_ARROW_RIGHT}'
pos = text.find(marker)
assert pos != -1, "Marker not found!"

end_section = text.find('</section>', pos)
assert end_section != -1, "End of section not found!"
end_section += len('</section>')

section_html = """

    <!-- 4-STEP CLINICAL PROTOCOL SECTION -->
    <section class="section" style="background:#FAF9F6; padding:72px 0;">
      <div class="container w-container">
        <div style="text-align:center; max-width:680px; margin:0 auto 48px auto;">
          <div class="section-kicker">OUR CLINICAL PROTOCOL</div>
          <h2 class="heading-2" style="font-size:clamp(26px, 3.4vw, 38px); line-height:1.22 !important; margin-bottom:14px;">
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
    </section>"""

new_text = text[:end_section] + section_html + text[end_section:]
with open(master_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Successfully inserted 4-step protocol section into build_full_website_master.py!")
