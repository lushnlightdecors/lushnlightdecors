from pathlib import Path

path=Path('index.html')
text=path.read_text(encoding='utf-8')

text=text.replace('nav{position:sticky;top:0;z-index:10;background:rgba(255,250,247,.95);border-bottom:1px solid #eadfd9;backdrop-filter:blur(10px)}','nav{position:sticky;top:0;z-index:10;background:#E8D6B8;border-bottom:1px solid #d8c49e;backdrop-filter:blur(10px)}',1)

css='''
/* Themed decor element modal backgrounds */
.decor-element-modal::before{content:"";position:absolute;inset:0;pointer-events:none;opacity:.42;background-repeat:repeat;background-size:260px 260px}
.decor-element-modal.theme-floral::before{background-color:#254b38;background-image:radial-gradient(circle at 28px 28px,rgba(255,255,255,.18) 0 7px,transparent 8px),radial-gradient(circle at 58px 48px,rgba(232,214,184,.2) 0 10px,transparent 11px),radial-gradient(ellipse at 88px 78px,rgba(255,255,255,.09) 0 12px,transparent 13px),linear-gradient(35deg,transparent 47%,rgba(255,255,255,.08) 48% 50%,transparent 51%)}
.decor-element-modal.theme-balloon::before{background-color:#315343;background-image:radial-gradient(ellipse at 42px 52px,rgba(232,214,184,.24) 0 24px,transparent 25px),radial-gradient(ellipse at 122px 98px,rgba(255,255,255,.16) 0 21px,transparent 22px),radial-gradient(ellipse at 198px 42px,rgba(182,149,100,.24) 0 19px,transparent 20px),linear-gradient(72deg,transparent 48%,rgba(255,255,255,.07) 49% 50%,transparent 51%)}
.decor-element-modal.theme-accessories::before{background-color:#3a4d42;background-image:linear-gradient(45deg,transparent 46%,rgba(232,214,184,.13) 47% 49%,transparent 50%),linear-gradient(-45deg,transparent 46%,rgba(255,255,255,.08) 47% 49%,transparent 50%),radial-gradient(circle at 65px 65px,rgba(182,149,100,.18) 0 4px,transparent 5px),radial-gradient(circle at 190px 165px,rgba(255,255,255,.11) 0 3px,transparent 4px)}
.decor-element-modal-shell{position:relative;z-index:1}
'''
if '/* Themed decor element modal backgrounds */' not in text:
    text=text.replace('</style>',css+'\n</style>',1)

old="""async function openCategory(key){
    const all=await loadData();const cat=all[key];if(!cat)return;
    currentPhotos=Array.isArray(cat.photos)?cat.photos:[];
"""
new="""async function openCategory(key){
    const all=await loadData();const cat=all[key];if(!cat)return;
    modal.classList.remove('theme-floral','theme-balloon','theme-accessories');
    modal.classList.add(key==='floral'?'theme-floral':key==='balloon'?'theme-balloon':'theme-accessories');
    currentPhotos=Array.isArray(cat.photos)?cat.photos:[];
"""
if old not in text:
    raise SystemExit('openCategory block not found')
text=text.replace(old,new,1)

path.write_text(text,encoding='utf-8')
