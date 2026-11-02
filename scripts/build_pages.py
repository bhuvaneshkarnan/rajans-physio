import os
import re
import json
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote

PAGES = [
    '/',
    '/about',
    '/blog',
    '/blog/10-things-nobody-told-you-about-being-a-web-designer',
    '/blog/10-web-design-blogs-you-cant-miss',
    '/blog/7-must-have-tools-for-web-designers',
    '/blog/7-of-the-best-examples-of-beautiful-blog-design',
    '/faq',
    '/free-assessment',
    '/medical-terms',
    '/membership-terms',
    '/non-discrimination',
    '/pricing',
    '/privacy-policy',
    '/privacy-practices'
]

BASE_URL = 'https://dreamlab-website-e0f709d63d04003d95aaea.webflow.io'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch_html(path):
    url = BASE_URL + path
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode('utf-8', errors='ignore')

def match_url(url, url_map):
    if not url:
        return None
    url = url.strip()
    if url in url_map:
        return url_map[url]
    unq_url = unquote(url)
    if unq_url in url_map:
        return url_map[unq_url]
    parsed = urlparse(url)
    no_query = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    if no_query in url_map:
        return url_map[no_query]
    no_scheme = f"//{parsed.netloc}{parsed.path}"
    if no_scheme in url_map:
        return url_map[no_scheme]
    if parsed.path in url_map:
        return url_map[parsed.path]
    if unquote(parsed.path) in url_map:
        return url_map[unquote(parsed.path)]
    base_name = os.path.basename(parsed.path)
    clean_base = re.sub(r'[\s%]+', '_', unquote(base_name))
    clean_base = re.sub(r'[\\/*?:"<>|()]', '_', clean_base)
    clean_base = re.sub(r'_+', '_', clean_base)
    if clean_base in url_map:
        return url_map[clean_base]
    for k, v in url_map.items():
        if v == clean_base:
            return v
    return None

def process_page_html(raw_html, depth_prefix, asset_prefix, url_map):
    soup = BeautifulSoup(raw_html, 'html.parser')
    
    # 1. Update Stylesheets
    for link in soup.find_all('link', rel='stylesheet'):
        href = link.get('href', '')
        if 'webflow' in href or 'dreamlab' in href:
            link['href'] = f"{asset_prefix}css/dreamlab.webflow.css"
            
    # 2. Update Scripts
    for s in soup.find_all('script', src=True):
        src = s['src']
        if 'jquery' in src:
            s['src'] = f"{asset_prefix}js/jquery.min.js"
        elif 'webflow' in src:
            s['src'] = f"{asset_prefix}js/webflow.js"
        elif 'webfont' in src:
            s['src'] = f"{asset_prefix}js/webfont.js"
        elif 'scrolldisable' in src:
            s['src'] = f"{asset_prefix}js/scrolldisable.js"
            
    # 3. Update Favicon / Touch Icons
    for link in soup.find_all('link', rel=lambda r: r and any(x in r for x in ['icon', 'apple-touch-icon'])):
        href = link.get('href', '')
        fname = match_url(href, url_map)
        if fname:
            link['href'] = f"{asset_prefix}images/{fname}"

    # 4. Update Images & Srcset
    for img in soup.find_all('img'):
        src = img.get('src', '')
        fname = match_url(src, url_map)
        if fname:
            img['src'] = f"{asset_prefix}images/{fname}"
            
        srcset = img.get('srcset', '')
        if srcset:
            new_parts = []
            candidates = [c.strip() for c in re.split(r',\s*(?=[^,\s]+(?:\s+[0-9.]+[wx])?)', srcset) if c.strip()]
            for cand in candidates:
                tokens = cand.split()
                if not tokens:
                    continue
                u = tokens[0]
                desc = tokens[1] if len(tokens) > 1 else ''
                matched = match_url(u, url_map)
                if matched:
                    new_u = f"{asset_prefix}images/{matched}"
                    new_parts.append(f"{new_u} {desc}".strip())
                else:
                    new_parts.append(cand)
            img['srcset'] = ', '.join(new_parts)

    # 5. Inline styles with background-image: url(...)
    for el in soup.find_all(style=True):
        style = el['style']
        def replace_bg(match):
            orig_u = match.group(1).strip('\'"')
            matched = match_url(orig_u, url_map)
            if matched:
                return f"url('{asset_prefix}images/{matched}')"
            return match.group(0)
        new_style = re.sub(r'url\(([^)]+)\)', replace_bg, style)
        el['style'] = new_style

    # 6. Specific fix for Savvy assessment script in free-assessment page
    for s in soup.find_all('script'):
        if s.string and 'beginSavvy' in s.string:
            script_text = s.string
            script_text = script_text.replace('h.startsWith("localhost")?"local"', 'false?"local"')
            script_text = script_text.replace(
                'case"production":return"https://bundle.trysavvy.com/bundle.js"',
                f'case"production":return"{asset_prefix}js/savvy-bundle.js"'
            )
            s.string = script_text

    # 7. Add Navigation Helper for file:// protocol and local links
    helper_script = soup.new_tag('script')
    helper_script.string = f"""
      window.DL_DEPTH = '{depth_prefix}';
      if (window.location.protocol === 'file:') {{
        document.addEventListener('DOMContentLoaded', function() {{
          var depth = window.DL_DEPTH || '';
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
    """
    if soup.body:
        soup.body.append(helper_script)

    return str(soup)

def rewrite_css(url_map):
    css_path = os.path.join('assets', 'css', 'dreamlab.webflow.css')
    css_url = 'https://assets-global.website-files.com/6475b366ed49970529d05c4c/css/dreamlab-website-e0f709d63d04003d95aaea.webflow.925915b99.min.css'
    req = urllib.request.Request(css_url, headers=HEADERS)
    css_content = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', errors='ignore')
    
    # Replace Recoleta font url
    css_content = re.sub(
        r'https://assets\.website-files\.com/6475b366ed49970529d05c4c/6475b366ed49970529d05cb5_92cd2256-c74e-421f-bd64-a207c4063918\.woff',
        '../fonts/Recoleta.woff',
        css_content
    )
    
    # Replace all image URLs in CSS
    def replace_css_url(match):
        raw_u = match.group(1).strip('\'"')
        if raw_u.startswith('data:'):
            return match.group(0)
        matched = match_url(raw_u, url_map)
        if matched:
            return f"url('../images/{matched}')"
        return match.group(0)

    css_content = re.sub(r'url\(([^)]+)\)', replace_css_url, css_content)
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("Rewritten assets/css/dreamlab.webflow.css.")

def main():
    print("Loading url_to_local_img.json...")
    with open('url_to_local_img.json') as f:
        url_map = json.load(f)

    print("Rewriting CSS with normalized image paths...")
    rewrite_css(url_map)

    # Cache raw html for all pages
    cached_html = {}
    for p in PAGES:
        print(f"Fetching {p}...")
        cached_html[p] = fetch_html(p)

    for p in PAGES:
        print(f"Processing and saving {p}...")
        raw_html = cached_html[p]
        
        if p == '/':
            processed = process_page_html(raw_html, depth_prefix='', asset_prefix='assets/', url_map=url_map)
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(processed)
        else:
            rel_path = p.lstrip('/')
            parts = rel_path.split('/')
            
            if len(parts) == 1:
                # 1. Save pricing.html
                processed_root = process_page_html(raw_html, depth_prefix='', asset_prefix='assets/', url_map=url_map)
                with open(f"{rel_path}.html", 'w', encoding='utf-8') as f:
                    f.write(processed_root)
                    
                # 2. Save pricing/index.html
                os.makedirs(rel_path, exist_ok=True)
                processed_sub = process_page_html(raw_html, depth_prefix='../', asset_prefix='../assets/', url_map=url_map)
                with open(os.path.join(rel_path, 'index.html'), 'w', encoding='utf-8') as f:
                    f.write(processed_sub)
                    
            elif len(parts) == 2:
                parent_dir, slug = parts[0], parts[1]
                os.makedirs(parent_dir, exist_ok=True)
                
                # 1. Save blog/xyz.html
                processed_sub1 = process_page_html(raw_html, depth_prefix='../', asset_prefix='../assets/', url_map=url_map)
                with open(os.path.join(parent_dir, f"{slug}.html"), 'w', encoding='utf-8') as f:
                    f.write(processed_sub1)
                    
                # 2. Save blog/xyz/index.html
                sub_folder = os.path.join(parent_dir, slug)
                os.makedirs(sub_folder, exist_ok=True)
                processed_sub2 = process_page_html(raw_html, depth_prefix='../../', asset_prefix='../../assets/', url_map=url_map)
                with open(os.path.join(sub_folder, 'index.html'), 'w', encoding='utf-8') as f:
                    f.write(processed_sub2)

    print("All pages successfully processed and written!")

if __name__ == '__main__':
    main()
