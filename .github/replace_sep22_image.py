from pathlib import Path

OLD = 'ChatGPT Image Sep 22, 2026, 02_32_42 PM.png'
NEW = 'ChatGPT Image Sep 24, 2026, 12_55_25 AM.png'
ROOT = Path('.')

text_exts = {'.html', '.json', '.xml', '.txt', '.md', '.css', '.js', '.yml', '.yaml'}
changed = []

for path in ROOT.rglob('*'):
    if not path.is_file() or '.git' in path.parts or '.github' in path.parts:
        continue
    if path.suffix.lower() not in text_exts:
        continue
    try:
        text = path.read_text(encoding='utf-8')
    except Exception:
        continue
    if OLD in text:
        path.write_text(text.replace(OLD, NEW), encoding='utf-8')
        changed.append(str(path))

if not changed:
    raise SystemExit('No references to old image were found')

remaining = []
for path in ROOT.rglob('*'):
    if not path.is_file() or '.git' in path.parts or '.github' in path.parts:
        continue
    if path.suffix.lower() not in text_exts:
        continue
    try:
        text = path.read_text(encoding='utf-8')
    except Exception:
        continue
    if OLD in text:
        remaining.append(str(path))

if remaining:
    raise SystemExit('Old image reference remains in: ' + ', '.join(remaining))

print('Replaced old image reference in:')
for p in changed:
    print('-', p)
