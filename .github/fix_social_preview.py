from pathlib import Path
import shutil

html_path = Path('index.html')
text = html_path.read_text(encoding='utf-8')

source_image = Path('ChatGPT Image Sep 21, 2026, 10_07_30 PM.png')
preview_image = Path('social-preview.png')
if not source_image.exists():
    raise SystemExit(f'Missing source preview image: {source_image}')
shutil.copyfile(source_image, preview_image)

old_og = '<meta property="og:image" content="https://lushnlightdecors.ca/ChatGPT Image Sep 21, 2026, 10_07_30 PM.png">'
new_og = '''<meta property="og:image" content="https://lushnlightdecors.ca/social-preview.png?v=20260923">
<meta property="og:image:secure_url" content="https://lushnlightdecors.ca/social-preview.png?v=20260923">
<meta property="og:image:type" content="image/png">
<meta property="og:image:alt" content="LushnLight Decors event decor in Toronto and the GTA">
<meta property="og:site_name" content="LushnLight Decors">'''
old_twitter = '<meta name="twitter:image" content="https://lushnlightdecors.ca/ChatGPT Image Sep 21, 2026, 10_07_30 PM.png">'
new_twitter = '''<meta name="twitter:image" content="https://lushnlightdecors.ca/social-preview.png?v=20260923">
<meta name="twitter:image:alt" content="LushnLight Decors event decor in Toronto and the GTA">'''
old_schema = '"image":"https://lushnlightdecors.ca/ChatGPT Image Sep 21, 2026, 10_07_30 PM.png"'
new_schema = '"image":"https://lushnlightdecors.ca/social-preview.png?v=20260923"'

for old, new, label in [
    (old_og, new_og, 'Open Graph image'),
    (old_twitter, new_twitter, 'Twitter image'),
    (old_schema, new_schema, 'schema image'),
]:
    if old not in text:
        raise SystemExit(f'Could not find current {label} metadata')
    text = text.replace(old, new, 1)

html_path.write_text(text, encoding='utf-8')
print('Created social-preview.png and updated social metadata')
