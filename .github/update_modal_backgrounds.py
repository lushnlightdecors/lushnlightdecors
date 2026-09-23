from pathlib import Path
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')

replacements = {
    'floral': ".decor-element-modal.theme-floral .decor-element-modal-shell{background-image:url('/Flower.png')!important}",
    'balloon': ".decor-element-modal.theme-balloon .decor-element-modal-shell{background-image:url('/BAlloon.png')!important}",
    'accessories': ".decor-element-modal.theme-accessories .decor-element-modal-shell{background-image:url('/Accessories.png')!important}",
}

for theme, replacement in replacements.items():
    pattern = rf"\.decor-element-modal\.theme-{theme} \.decor-element-modal-shell\{{background-image:url\('[^']+'\)!important(?:;background-position:[^}}]+!important)?\}}"
    text, count = re.subn(pattern, replacement, text, count=1)
    if count != 1:
        raise SystemExit(f'Could not update {theme} modal background')

path.write_text(text, encoding='utf-8')
print('Updated modal backgrounds to Flower.png, BAlloon.png, Accessories.png')
