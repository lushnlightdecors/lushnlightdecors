from pathlib import Path

path=Path('index.html')
text=path.read_text(encoding='utf-8')
css='''
/* Exact uploaded pastel backgrounds for decor element modals */
.decor-element-modal{background:rgba(35,33,31,.66)!important}
.decor-element-modal::before{display:none!important;background:none!important;opacity:0!important}
.decor-element-modal-shell{position:relative!important;overflow:auto!important;background-color:#fffaf5!important;background-repeat:no-repeat!important;background-position:center!important;background-size:cover!important}
.decor-element-modal-shell::before{content:"";position:absolute;inset:0;border-radius:inherit;background:rgba(255,250,245,.70);pointer-events:none;z-index:0}
.decor-element-modal.theme-floral .decor-element-modal-shell{background-image:url('/modal-floral-bg.jpg')!important}
.decor-element-modal.theme-balloon .decor-element-modal-shell{background-image:url('/modal-balloon-bg.jpg')!important}
.decor-element-modal.theme-accessories .decor-element-modal-shell{background-image:url('/modal-accessories-bg.jpg')!important}
.decor-element-modal-shell>*{position:relative;z-index:1}
.decor-element-modal-grid img{box-shadow:0 7px 20px rgba(18,63,42,.10)}
.decor-element-empty{background:rgba(255,255,255,.82)!important;backdrop-filter:blur(4px)}
'''
if '/* Exact uploaded pastel backgrounds for decor element modals */' not in text:
    text=text.replace('</style>',css+'\n</style>',1)
path.write_text(text,encoding='utf-8')
