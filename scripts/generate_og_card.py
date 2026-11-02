import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
img = Image.new('RGB', (W, H), color='#FAF6EE')
draw = ImageDraw.Draw(img)

# Top accent bar (Navy & Magenta)
draw.rectangle([0, 0, 720, 8], fill='#233E85')
draw.rectangle([720, 0, W, 8], fill='#ED1D7F')

# Load fonts
font_bold_path = os.path.join('assets', 'fonts', 'WorkSans-Bold.ttf')
font_reg_path = os.path.join('assets', 'fonts', 'WorkSans-Regular.ttf')

font_h1 = ImageFont.truetype(font_bold_path, 48)
font_h2 = ImageFont.truetype(font_bold_path, 36)
font_sub = ImageFont.truetype(font_reg_path, 22)
font_badge = ImageFont.truetype(font_bold_path, 15)
font_sm = ImageFont.truetype(font_reg_path, 17)
font_sm_bold = ImageFont.truetype(font_bold_path, 18)

# Logo
logo_path = os.path.join('assets', 'images', 'clinic_logo.png')
if os.path.exists(logo_path):
    logo = Image.open(logo_path).convert('RGBA')
    logo = logo.resize((260, 260), Image.Resampling.LANCZOS)
    
    # White rounded container for logo on left
    card_bg = Image.new('RGBA', (300, 300), (255, 255, 255, 255))
    draw_card = ImageDraw.Draw(card_bg)
    draw_card.rounded_rectangle([0, 0, 300, 300], radius=24, fill='#FFFFFF', outline='#DCE5F5', width=2)
    card_bg.paste(logo, (20, 20), logo)
    img.paste(card_bg, (70, 65))

# Draw eyebrow pill on right
eyebrow_text = "EST. 2009  •  17 YEARS CLINICAL EXCELLENCE"
pill_box = [420, 65, 870, 105]
draw.rounded_rectangle(pill_box, radius=20, fill='#FFF0F6', outline='#FFD6E7', width=1)
draw.text((440, 75), eyebrow_text, fill='#ED1D7F', font=font_badge)

# Main Title
draw.text((420, 125), "Rajan's Physiotherapy", fill='#233E85', font=font_h1)
draw.text((420, 185), "& Pain Relief Centre", fill='#ED1D7F', font=font_h2)

# Subtitle / Tagline
draw.text((420, 245), "Evidence-informed rehabilitation in Chromepet, Chennai", fill='#2D3748', font=font_sub)
draw.text((420, 280), "Over 15,000+ patients healed without surgery", fill='#4A5568', font=font_sub)

# Modality badges
modalities = ["Dorn Spinal Therapy", "Laser Therapy", "Shockwave ESWT", "Sports Rehab", "Home Visits"]
mx = 420
my = 330
for m in modalities:
    bbox = draw.textbbox((0, 0), m, font=font_badge)
    tw = bbox[2] - bbox[0]
    draw.rounded_rectangle([mx, my, mx + tw + 24, my + 34], radius=17, fill='#EEF3FA', outline='#DCE5F5', width=1)
    draw.text((mx + 12, my + 8), m, fill='#233E85', font=font_badge)
    mx += tw + 14
    if mx > 1120:
        break

# Doctor card under logo on left
doc_box = [70, 385, 370, 565]
draw.rounded_rectangle(doc_box, radius=18, fill='#FFFFFF', outline='#DCE5F5', width=1)
draw.text((90, 402), "Lead Consultant:", fill='#718096', font=font_sm)
draw.text((90, 426), "Dr. Prabhu Rajan, PT", fill='#233E85', font=font_sm_bold)
draw.text((90, 456), "17+ Yrs Exp  •  MPT Sports", fill='#ED1D7F', font=font_badge)
draw.text((90, 482), "MIAP L-27944  •  Vice Chairman AIDTA", fill='#4A5568', font=font_sm)
draw.text((90, 520), "📞 +91 90426 12895", fill='#233E85', font=font_sm_bold)

# Trust & Address box on right
trust_box = [420, 385, 1130, 565]
draw.rounded_rectangle(trust_box, radius=18, fill='#FFFFFF', outline='#DCE5F5', width=1)
draw.text((450, 405), "Practo 99% Recommended (513+ Ratings)  •  Justdial 4.9 Stars (730+ Reviews)", fill='#233E85', font=font_sm_bold)
draw.text((450, 445), "Location: No. 9 / 29C, 1st Cross St, Nagappa Nagar, Chromepet, Chennai - 600044", fill='#4A5568', font=font_sm)
draw.text((450, 480), "Landmark: Behind Chromepet Police Station / Near Shastri Colony", fill='#718096', font=font_sm)
draw.text((450, 520), "🌐 rajans-physio.vercel.app  •  Mon-Sat: 9:30 AM - 8:30 PM", fill='#233E85', font=font_sm_bold)

out_jpg = os.path.join('assets', 'images', 'og-share-card.jpg')
out_png = os.path.join('assets', 'images', 'og-share-card.png')
img.save(out_jpg, 'JPEG', quality=92, optimize=True)
img.save(out_png, 'PNG', optimize=True)
print(f"Generated: {out_jpg} ({os.path.getsize(out_jpg)} bytes)")
print(f"Generated: {out_png} ({os.path.getsize(out_png)} bytes)")
