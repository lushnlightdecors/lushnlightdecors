from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

old_floral = ".decor-element-modal.theme-floral .decor-element-modal-shell{background-image:url('/Flower.png')!important}"
old_accessories = ".decor-element-modal.theme-accessories .decor-element-modal-shell{background-image:url('/Accessories.png')!important}"
new_floral = ".decor-element-modal.theme-floral .decor-element-modal-shell{background-image:url('/Accessories.png')!important}"
new_accessories = ".decor-element-modal.theme-accessories .decor-element-modal-shell{background-image:url('/Flower.png')!important}"

if old_floral not in text:
    raise SystemExit('Current Floral background mapping not found')
if old_accessories not in text:
    raise SystemExit('Current Accessories background mapping not found')

text = text.replace(old_floral, new_floral, 1)
text = text.replace(old_accessories, new_accessories, 1)
path.write_text(text, encoding='utf-8')
print('Swapped Flower.png and Accessories.png modal mappings')
