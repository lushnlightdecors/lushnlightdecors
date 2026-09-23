from pathlib import Path
import json
import re

ROOT = Path('.')
OLD = 'ChatGPT Image Sep 21, 2026, 11_50_39 PM.png'
VIDEO_POSTER = 'ChatGPT Image Sep 23, 2026, 04_30_42 PM.png'

ADDITIONS = {
    'mehndi-traditional': ['ChatGPT Image Sep 23, 2026, 03_15_55 PM.png'],
    'other': ['ChatGPT Image Sep 23, 2026, 03_17_35 PM.png'],
    'birthdays': [
        'ChatGPT Image Sep 23, 2026, 03_31_38 PM.png',
        'ChatGPT Image Sep 23, 2026, 04_07_04 PM.png',
    ],
    'baby-showers': [
        'ChatGPT Image Sep 23, 2026, 03_35_16 PM.png',
        'ChatGPT Image Sep 23, 2026, 03_39_27 PM.png',
    ],
    'weddings': ['ChatGPT Image Sep 23, 2026, 04_30_42 PM.png'],
}

PAGE_ADDITIONS = {
    'mehndi-traditional-decor/index.html': ADDITIONS['mehndi-traditional'],
    'birthday-decor/index.html': ADDITIONS['birthdays'],
    'baby-shower-decor/index.html': ADDITIONS['baby-showers'],
    'wedding-decor/index.html': ADDITIONS['weddings'],
}

PAGE_LABELS = {
    'mehndi-traditional-decor/index.html': 'Traditional',
    'birthday-decor/index.html': 'Birthday',
    'baby-shower-decor/index.html': 'Baby & Bridal Shower',
    'wedding-decor/index.html': 'Wedding',
}

# Update gallery.json. All Photos is generated dynamically from these category lists.
gallery_path = ROOT / 'gallery.json'
data = json.loads(gallery_path.read_text(encoding='utf-8'))
for cat in data.values():
    if isinstance(cat, dict) and isinstance(cat.get('photos'), list):
        cat['photos'] = [p for p in cat['photos'] if p != OLD]

for key, photos in ADDITIONS.items():
    current = data[key]['photos']
    for photo in reversed(photos):
        if photo in current:
            current.remove(photo)
        current.insert(0, photo)

data['baby-showers']['label'] = 'Baby & Bridal Shower'
gallery_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

# Helpers for dedicated category pages.
def remove_old_img_tags(text):
    return re.sub(r'\s*<img\b[^>]*' + re.escape(OLD) + r'[^>]*>', '', text, flags=re.I)

def add_gallery_images(text, images, label):
    pattern = re.compile(r'(<section\s+id="gallery".*?<div\s+class="gallery">)(.*?)(</div></div></section>)', re.S | re.I)
    m = pattern.search(text)
    if not m:
        raise SystemExit(f'Gallery section not found for {label}')
    body = m.group(2)
    additions = []
    for photo in images:
        if photo not in body:
            additions.append(f'<img src="../{photo}" loading="lazy" alt="{label} decor by LushnLight Decors in Toronto and the GTA">')
    if additions:
        body = ''.join(additions) + body
        text = text[:m.start()] + m.group(1) + body + m.group(3) + text[m.end():]
    return text

for rel, images in PAGE_ADDITIONS.items():
    p = ROOT / rel
    text = p.read_text(encoding='utf-8')
    text = remove_old_img_tags(text)
    text = add_gallery_images(text, images, PAGE_LABELS[rel])

    if rel == 'baby-shower-decor/index.html':
        text = text.replace('Baby Shower', 'Baby & Bridal Shower')
        text = text.replace('baby shower', 'baby & bridal shower')
        text = text.replace('Baby%20Shower', 'Baby%20%26%20Bridal%20Shower')

    p.write_text(text, encoding='utf-8')

# Main page: fresh video poster + consistent Baby & Bridal Shower naming.
index_path = ROOT / 'index.html'
index = index_path.read_text(encoding='utf-8')
index = remove_old_img_tags(index)
index = re.sub(r'poster="[^"]+"', f'poster="{VIDEO_POSTER}"', index, count=1)
index = index.replace('<h3>Baby Showers</h3>', '<h3>Baby & Bridal Showers</h3>')
index = index.replace('Explore Baby Shower Decor →', 'Explore Baby & Bridal Shower Decor →')
index = index.replace('<option>Baby Shower</option>', '<option>Baby & Bridal Shower</option>')
index_path.write_text(index, encoding='utf-8')

# Verify all requested additions exist in gallery.json and old image is no longer referenced.
check = json.loads(gallery_path.read_text(encoding='utf-8'))
for key, photos in ADDITIONS.items():
    for photo in photos:
        if photo not in check[key]['photos']:
            raise SystemExit(f'Missing {photo} from {key}')

remaining = []
for p in ROOT.rglob('*'):
    if not p.is_file() or '.git' in p.parts or '.github' in p.parts:
        continue
    if p.suffix.lower() not in {'.html', '.json', '.xml', '.txt', '.md', '.css', '.js'}:
        continue
    try:
        txt = p.read_text(encoding='utf-8')
    except Exception:
        continue
    if OLD in txt:
        remaining.append(str(p))
if remaining:
    raise SystemExit('Old image still referenced in: ' + ', '.join(remaining))

print('Updated gallery categories, dedicated pages, video poster, and Baby & Bridal Shower naming.')
