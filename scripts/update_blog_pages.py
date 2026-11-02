import os
import re
import glob
from build_full_website import get_global_head, get_global_nav, get_global_footer

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def update_blog_file(filepath, depth_prefix):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    title_m = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
    title = title_m.group(1) if title_m else "Clinical Articles & Health Guides | Rajan's Physiotherapy"
    
    desc_m = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]*)"', html, re.IGNORECASE)
    desc = desc_m.group(1) if desc_m else "Evidence-informed physiotherapy, spinal rehabilitation, and pain management guides from Dr. Prabhu Rajan, PT."

    # Find content between header and footer
    nav_end = html.find('</header>')
    if nav_end != -1:
        nav_end += 9
    else:
        nav_end = html.find('<main')
        if nav_end == -1: nav_end = 0

    footer_start = html.find('<footer')
    if footer_start == -1:
        footer_start = len(html) - 200

    content_inner = html[nav_end:footer_start].strip()
    
    # Replace old teal
    content_inner = content_inner.replace('#19535F', '#233E85').replace('#19535f', '#233E85')
    content_inner = content_inner.replace('#133E47', '#172A5C').replace('#E8F1F2', '#EEF3FA')
    
    asset_prefix = f"{depth_prefix}assets/" if depth_prefix else "assets/"
    if depth_prefix:
        content_inner = re.sub(r'src="assets/', f'src="{depth_prefix}assets/', content_inner)
        content_inner = re.sub(r'href="assets/', f'href="{depth_prefix}assets/', content_inner)

    new_html = f"""{get_global_head(title, desc, asset_prefix)}
{get_global_nav(depth_prefix, "")}
{content_inner}
{get_global_footer(depth_prefix)}"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Updated blog page: {filepath}")

# Update root blog.html
update_blog_file(os.path.join(ROOT_DIR, 'blog.html'), "")
# Update blog/index.html
if os.path.exists(os.path.join(ROOT_DIR, 'blog', 'index.html')):
    update_blog_file(os.path.join(ROOT_DIR, 'blog', 'index.html'), "../")

# Update any blog subposts
for post in glob.glob(os.path.join(ROOT_DIR, 'blog', '*.html')):
    if not post.endswith('index.html'):
        update_blog_file(post, "../")

print("Blog pages updated!")
