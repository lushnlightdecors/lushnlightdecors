from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

replacements = [
    (
        ".decor-element-modal.theme-floral .decor-element-modal-shell{background-image:url('/modal-floral-bg.jpg')!important}",
        ".decor-element-modal.theme-floral .decor-element-modal-shell{background-image:url('/Flower.png')!important}"
    ),
    (
        ".decor-element-modal.theme-balloon .decor-element-modal-shell{background-image:url('/ChatGPT Image Sep 22, 2026, 01_42_06 AM.png')!important;background-position:center 35%!important}",
        ".decor-element-modal.theme-balloon .decor-element-modal-shell{background-image:url('/BAlloon.png')!important}"
    ),
    (
        ".decor-element-modal.theme-accessories .decor-element-modal-shell{background-image:url('/modal-accessories-bg.jpg')!important}",
        ".decor-element-modal.theme-accessories .decor-element-modal-shell{background-image:url('/Accessories.png')!important}"
    ),
]

for old, new in replacements:
    if old not in text:
        raise SystemExit(f'Expected CSS line not found: {old}')
    text = text.replace(old, new, 1)

path.write_text(text, encoding='utf-8')
print('Updated modal backgrounds to Flower.png, BAlloon.png, Accessories.png')
