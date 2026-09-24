from pathlib import Path

PAGES = [
    'about/index.html',
    'wedding-decor/index.html',
    'birthday-decor/index.html',
    'baby-shower-decor/index.html',
    'aqiqah-decor/index.html',
    'mehndi-traditional-decor/index.html',
]

EVENT_PAGES = set(PAGES[1:])

NAV_CSS = r'''
/* Homepage-style navigation hover for secondary pages */
.links a{position:relative;transition:color .22s ease,transform .22s ease,letter-spacing .22s ease}
@media(hover:hover) and (pointer:fine){
  .links a:after{content:"";position:absolute;left:50%;right:50%;bottom:2px;height:1.5px;background:#C2A56D;transition:left .22s ease,right .22s ease}
  .links a:hover{color:#C2A56D!important;transform:translateY(-2px);letter-spacing:.055em}
  .links a:hover:after{left:0;right:0}
}
'''

CTA_CSS = r'''
/* Highlight and center event-page quote CTA */
.cta .btn{
  display:block!important;
  width:max-content;
  max-width:100%;
  margin:24px auto 0!important;
  background:#C2A56D!important;
  color:#163D32!important;
  border:1px solid #C2A56D!important;
  box-shadow:0 8px 22px rgba(0,0,0,.16);
}
.cta .btn:hover{
  background:#FFFDF8!important;
  color:#163D32!important;
  border-color:#FFFDF8!important;
  transform:translateY(-2px);
}
'''

for rel in PAGES:
    path = Path(rel)
    text = path.read_text(encoding='utf-8')
    marker = '/* Homepage-style navigation hover for secondary pages */'
    if marker in text:
        continue

    css = '\n' + NAV_CSS
    if rel in EVENT_PAGES:
        css += '\n' + CTA_CSS

    idx = text.rfind('</style>')
    if idx == -1:
        raise SystemExit(f'No closing style tag in {rel}')
    text = text[:idx] + css + '\n' + text[idx:]
    path.write_text(text, encoding='utf-8')
    print('Updated', rel)

# Verification
for rel in PAGES:
    text = Path(rel).read_text(encoding='utf-8')
    if 'Homepage-style navigation hover for secondary pages' not in text:
        raise SystemExit(f'Navigation hover missing from {rel}')
    if rel in EVENT_PAGES and 'Highlight and center event-page quote CTA' not in text:
        raise SystemExit(f'CTA fix missing from {rel}')

print('Secondary navigation hover and CTA styling verified.')
