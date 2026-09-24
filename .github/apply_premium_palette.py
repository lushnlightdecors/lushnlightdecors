from pathlib import Path
import re

ROOT = Path('.')

# LushnLight premium palette
# Deep Forest Green #163D32
# Warm Ivory        #FFFDF8
# Soft Champagne    #F4EBDD
# Muted Gold        #C2A56D
# Dusty Blush       #E8D6D1
# Charcoal Green    #283A34
# Soft White        #FFFFFF

replacements = {
    '#123f2a': '#163D32',
    '#d9c9a6': '#E8D6D1',
    '#fbf8ef': '#FFFDF8',
    '#27332d': '#283A34',
    '#b69564': '#C2A56D',
    '#e8d6b8': '#F4EBDD',
    '#d8c49e': '#E6D8C2',
    '#d9cbc5': '#E2D7C9',
    '#eee1dc': '#E9E1D5',
    '#e7ddd2': '#E9E1D5',
    '#e8dfcf': '#E9E1D5',
    '#f5e9e5': '#F4EBDD',
    '#2f2227': '#163D32',
    '#173427': '#163D32',
    '#f8eeee': '#FFFDF8',
    '#f8f4e9': '#FFFDF8',
}

OVERRIDE = r'''
/* LushnLight premium colour palette — Sep 2026 */
body{background:#FFFDF8!important;color:#283A34!important}
nav{background:#F4EBDD!important;border-bottom-color:#E6D8C2!important}
.card,.quote-form,.review-card,.trust-card,.process-card,.faq details{border-color:#E9E1D5!important}
.btn{background:#163D32!important;color:#FFFFFF!important;border-color:#163D32!important;transition:background-color .22s ease,color .22s ease,border-color .22s ease,transform .22s ease}
.btn:hover{background:#C2A56D!important;color:#163D32!important;border-color:#C2A56D!important}
.btn.alt{background:transparent!important;color:#163D32!important;border-color:#163D32!important}
.btn.alt:hover{background:#C2A56D!important;color:#163D32!important;border-color:#C2A56D!important}
.category-tabs button{border-color:#163D32!important;color:#163D32!important}
.category-tabs button.active,.category-tabs button:hover{background:#163D32!important;color:#FFFFFF!important}
.social{background:#F4EBDD!important}
footer,.footer{background:#163D32!important;color:#FFFDF8!important}
footer a,.footer a,footer p,footer .family,.footer p{color:#FFFDF8!important}
footer a:hover,.footer a:hover,.footer-links a:hover{color:#C2A56D!important}
'''

updated = []
for path in ROOT.rglob('*.html'):
    if '.git' in path.parts or '.github' in path.parts:
        continue
    text = path.read_text(encoding='utf-8')
    original = text

    # Replace existing brand palette values case-insensitively.
    for old, new in replacements.items():
        text = re.sub(re.escape(old), new, text, flags=re.I)

    # Add champagne variable to the main homepage root palette if it is not present.
    if path.as_posix() == 'index.html' and '--champagne:' not in text:
        text = text.replace('--white:#fff}', '--white:#FFFFFF;--champagne:#F4EBDD}', 1)
        text = text.replace('--white:#FFFFFF}', '--white:#FFFFFF;--champagne:#F4EBDD}', 1)

    # Add one final, consistent palette override to every page.
    marker = '/* LushnLight premium colour palette — Sep 2026 */'
    if marker not in text:
        idx = text.rfind('</style>')
        if idx == -1:
            raise SystemExit(f'No closing style tag found in {path}')
        text = text[:idx] + OVERRIDE + '\n' + text[idx:]

    if text != original:
        path.write_text(text, encoding='utf-8')
        updated.append(str(path))

if not updated:
    raise SystemExit('No HTML files were updated')

print('Updated palette in:')
for p in updated:
    print('-', p)
