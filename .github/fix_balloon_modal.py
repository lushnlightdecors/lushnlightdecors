from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')
old = ".decor-element-modal.theme-balloon .decor-element-modal-shell{background-image:url('/modal-balloon-bg.jpg')!important}"
new = ".decor-element-modal.theme-balloon .decor-element-modal-shell{background-image:url('/ChatGPT Image Sep 22, 2026, 01_42_06 AM.png')!important;background-position:center 35%!important}"
if old not in text:
    raise SystemExit('Expected balloon modal CSS reference not found')
path.write_text(text.replace(old, new, 1), encoding='utf-8')
print('Updated balloon modal background reference')
