import glob
from datetime import datetime

base = "https://rajans-physio.vercel.app"
htmls = [f for f in glob.glob("*.html") if not f.startswith("404")]
lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

today = datetime.now().strftime("%Y-%m-%d")
for h in sorted(htmls):
    url = f"{base}/{h}" if h != "index.html" else f"{base}/"
    prio = "1.0" if h == "index.html" else ("0.8" if "therapy" in h or "rehabilitation" in h else "0.6")
    lines.append(f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>{prio}</priority>\n  </url>")

lines.append("</urlset>")
with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"Created sitemap.xml with {len(htmls)} URLs")
