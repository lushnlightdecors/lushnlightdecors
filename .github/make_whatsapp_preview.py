from pathlib import Path
from PIL import Image, ImageOps

src = Path('ChatGPT Image Sep 21, 2026, 10_07_30 PM.png')
out = Path('social-preview.jpg')
html_path = Path('index.html')

if not src.exists():
    raise SystemExit(f'Missing source image: {src}')

img = Image.open(src).convert('RGB')
img = ImageOps.fit(img, (1200, 630), method=Image.Resampling.LANCZOS, centering=(0.72, 0.5))

quality = 78
while quality >= 48:
    img.save(out, 'JPEG', quality=quality, optimize=True, progressive=True)
    if out.stat().st_size <= 450_000:
        break
    quality -= 5

if out.stat().st_size > 600_000:
    raise SystemExit(f'Preview still too large: {out.stat().st_size} bytes')

text = html_path.read_text(encoding='utf-8')
text = text.replace('https://lushnlightdecors.ca/social-preview.png?v=20260923', 'https://lushnlightdecors.ca/social-preview.jpg?v=20260923b')
text = text.replace('<meta property="og:image:type" content="image/png">', '<meta property="og:image:type" content="image/jpeg">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">')
html_path.write_text(text, encoding='utf-8')

print(f'Created {out} at {out.stat().st_size} bytes, quality={quality}')
