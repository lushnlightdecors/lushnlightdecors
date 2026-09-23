from pathlib import Path
import re

service_pages = [
    Path('wedding-decor/index.html'),
    Path('birthday-decor/index.html'),
    Path('baby-shower-decor/index.html'),
    Path('aqiqah-decor/index.html'),
    Path('mehndi-traditional-decor/index.html'),
]

shared_footer = '''<footer><div class="wrap"><img src="../IMG_9756.PNG" alt="LushnLight Decors" style="width:180px;max-height:90px;object-fit:contain"><div class="footlinks"><a href="../">Home</a><a href="../wedding-decor/">Wedding Decor</a><a href="../birthday-decor/">Birthday Decor</a><a href="../baby-shower-decor/">Baby Shower Decor</a><a href="../aqiqah-decor/">Aqiqah Decor</a><a href="../mehndi-traditional-decor/">Mehndi & Traditional</a></div><p style="opacity:.78;font-size:.88rem">Creating Unforgettable Moments across Toronto & the GTA.</p></div></footer>'''

service_css = '''
/* Unified secondary gallery hover + footer */
#gallery .gallery img{transition:transform .3s ease;cursor:pointer}
#gallery .gallery img:hover{transform:scale(1.025)}
.page-lightbox-thumb{cursor:pointer!important}
.page-lightbox button{width:44px!important;height:44px!important;font-size:1.5rem!important;background:rgba(255,255,255,.92)!important}
footer{background:#E8D6B8!important;color:#123F2A!important;padding:42px 0!important;text-align:center!important;margin-top:0!important}
footer .footlinks{display:flex;justify-content:center;gap:18px;flex-wrap:wrap;font-size:.88rem;margin:12px 0 0}
footer a{color:#123F2A!important}
footer p,footer .family{color:#52635A!important}
footer img{filter:none!important}
footer .footlinks a:hover,footer a:hover{color:#B69564!important}
'''

for path in service_pages:
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'<footer\b[^>]*>.*?</footer>', shared_footer, text, count=1, flags=re.S)
    text = text.replace('.page-lightbox-thumb{cursor:zoom-in}', '.page-lightbox-thumb{cursor:pointer}')
    if '/* Unified secondary gallery hover + footer */' not in text:
        text = text.replace('</style>', service_css + '\n</style>', 1)
    path.write_text(text, encoding='utf-8')

about = Path('about/index.html')
text = about.read_text(encoding='utf-8')
text = text.replace('.page-lightbox-thumb{cursor:zoom-in}', '.page-lightbox-thumb{cursor:pointer}')
about_css = '''
/* Match homepage gallery hover */
.evolve-photo{transition:transform .3s ease;cursor:pointer}
.evolve-photo:hover{transform:scale(1.025)}
.page-lightbox-thumb{cursor:pointer!important}
.page-lightbox button{width:44px!important;height:44px!important;font-size:1.5rem!important;background:rgba(255,255,255,.92)!important}
'''
if '/* Match homepage gallery hover */' not in text:
    text = text.replace('</style>', about_css + '\n</style>', 1)
about.write_text(text, encoding='utf-8')

home = Path('index.html')
text = home.read_text(encoding='utf-8')
old = '<div><h3>LushnLight Decors</h3><p>Elegant event decor for weddings, birthdays, baby showers, Aqiqah and special celebrations.</p><p><strong>Serving Toronto &amp; the GTA</strong></p></div>'
new = '<div><img class="footer-logo" src="IMG_9756.PNG" alt="LushnLight Decors logo"><p>Elegant event decor for weddings, birthdays, baby showers, Aqiqah and special celebrations.</p><p><strong>Serving Toronto &amp; the GTA</strong></p></div>'
text = text.replace(old, new, 1)
home_css = '''
.footer-logo{display:block;width:180px;max-height:90px;object-fit:contain;object-position:left center;margin:0 0 12px}
@media(max-width:760px){.footer-logo{margin:0 auto 12px;object-position:center}}
'''
if '.footer-logo{display:block;width:180px' not in text:
    text = text.replace('</style>', home_css + '\n</style>', 1)
home.write_text(text, encoding='utf-8')
