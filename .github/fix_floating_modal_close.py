from pathlib import Path

p = Path('index.html')
text = p.read_text(encoding='utf-8')
marker = '/* Floating close button for decor element modals */'
css = r'''
/* Floating close button for decor element modals */
.decor-element-modal.open .decor-element-close{
  position:fixed!important;
  top:max(16px, env(safe-area-inset-top))!important;
  right:max(16px, env(safe-area-inset-right))!important;
  z-index:140!important;
  width:48px!important;
  height:48px!important;
  display:grid!important;
  place-items:center!important;
  background:#FFFDF8!important;
  color:#163D32!important;
  border:1px solid #C2A56D!important;
  box-shadow:0 8px 24px rgba(0,0,0,.24)!important;
}
.decor-element-modal.open .decor-element-close:hover{
  background:#C2A56D!important;
  color:#163D32!important;
}
@media(max-width:760px){
  .decor-element-modal.open .decor-element-close{
    top:max(10px, env(safe-area-inset-top))!important;
    right:max(10px, env(safe-area-inset-right))!important;
    width:46px!important;
    height:46px!important;
  }
}
'''

if marker not in text:
    idx = text.rfind('</style>')
    if idx == -1:
        raise SystemExit('No closing style tag found')
    text = text[:idx] + '\n' + css + '\n' + text[idx:]
    p.write_text(text, encoding='utf-8')
    print('Added floating decor modal close button CSS')
else:
    print('Floating modal close CSS already present')
