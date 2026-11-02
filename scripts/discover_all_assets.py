import urllib.request
import re
import os
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

pages = [
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

base_url = 'https://dreamlab-website-e0f709d63d04003d95aaea.webflow.io'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

all_assets = set()
pages_data = {}

for p in pages:
    url = urljoin(base_url, p)
    print(f'Fetching page: {p}...')
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
    pages_data[p] = html
    soup = BeautifulSoup(html, 'html.parser')
    
    # CSS
    for l in soup.find_all('link', rel='stylesheet'):
        href = l.get('href')
        if href:
            all_assets.add(urljoin(url, href))
            
    # JS
    for s in soup.find_all('script', src=True):
        src = s.get('src')
        if src:
            all_assets.add(urljoin(url, src))
            
    # Icons
    for link in soup.find_all('link', rel=lambda r: r and any(x in r for x in ['icon', 'apple-touch-icon', 'image'])):
        href = link.get('href')
        if href:
            all_assets.add(urljoin(url, href))
            
    # Images in img tag
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            all_assets.add(urljoin(url, src))
        srcset = img.get('srcset')
        if srcset:
            for item in srcset.split(','):
                part = item.strip().split(' ')[0]
                if part:
                    all_assets.add(urljoin(url, part))

# CSS assets (from CSS files)
css_files = [a for a in all_assets if a.endswith('.css') or '.css' in a]
print('Found CSS files to parse:', len(css_files))

for css_url in css_files:
    try:
        req = urllib.request.Request(css_url, headers=headers)
        css_content = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
        matches = re.findall(r'url\([\'"]?([^\'"\)]+)[\'"]?\)', css_content)
        for m in matches:
            if not m.startswith('data:'):
                all_assets.add(urljoin(css_url, m))
    except Exception as e:
        print(f'Error fetching CSS {css_url}: {e}')

print(f'\nTotal unique assets discovered: {len(all_assets)}')
with open('discovered_assets.json', 'w') as f:
    json.dump(list(all_assets), f, indent=2)

print('Saved discovered_assets.json successfully.')
