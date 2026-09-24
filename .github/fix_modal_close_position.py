from pathlib import Path

p = Path('index.html')
text = p.read_text(encoding='utf-8')
start_marker = '/* Floating close button for decor element modals */'
end_marker = '</style>'

start = text.find(start_marker)
if start == -1:
    raise SystemExit('Floating close CSS marker not found')
end = text.find(end_marker, start)
if end == -1:
    raise SystemExit('Closing style tag not found')

replacement = '''/* Floating close button for decor element modals */
.decor-element-modal.open .decor-element-close{
  position:sticky!important;
  top:14px!important;
  right:auto!important;
  margin:-58px 0 10px auto!important;
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
    top:12px!important;
    right:auto!important;
    margin:-54px 0 8px auto!important;
    width:46px!important;
    height:46px!important;
  }
}

'''

text = text[:start] + replacement + text[end:]
p.write_text(text, encoding='utf-8')
print('Repositioned decor modal close button inside modal shell')
