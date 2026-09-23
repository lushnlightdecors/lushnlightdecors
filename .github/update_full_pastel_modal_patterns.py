from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

css = r'''
/* Full-panel pastel luxury artwork for decor element modals */
.decor-element-modal{background:rgba(35,33,31,.66)!important}
.decor-element-modal::before{display:none!important;background:none!important;opacity:0!important}
.decor-element-modal-shell{
  background-color:#fffaf5!important;
  background-repeat:repeat!important;
  background-position:0 0!important;
  background-size:520px 380px!important;
}
.decor-element-modal.theme-floral .decor-element-modal-shell{
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='520' height='380' viewBox='0 0 520 380'%3E%3Cdefs%3E%3Cfilter id='b'%3E%3CfeGaussianBlur stdDeviation='8'/%3E%3C/filter%3E%3C/defs%3E%3Cg opacity='.25' filter='url(%23b)'%3E%3Ccircle cx='70' cy='70' r='58' fill='%23f4d6dc'/%3E%3Ccircle cx='135' cy='55' r='45' fill='%23ded6ef'/%3E%3Ccircle cx='455' cy='80' r='60' fill='%23d9e7f3'/%3E%3Ccircle cx='400' cy='315' r='68' fill='%23f7dfc9'/%3E%3Ccircle cx='110' cy='315' r='58' fill='%23dbe7d6'/%3E%3C/g%3E%3Cg fill='none' stroke='%23c9a46b' stroke-width='2' opacity='.34'%3E%3Cpath d='M20 180C80 150 95 110 118 68'/%3E%3Cpath d='M390 360C410 305 450 270 510 250'/%3E%3Cpath d='M285 20C300 70 340 100 390 115'/%3E%3C/g%3E%3Cg opacity='.34'%3E%3Cg transform='translate(82 175)'%3E%3Cellipse rx='30' ry='13' fill='%23f2cdd5' transform='rotate(0)'/%3E%3Cellipse rx='30' ry='13' fill='%23e5d2ee' transform='rotate(60)'/%3E%3Cellipse rx='30' ry='13' fill='%23d8e6f3' transform='rotate(120)'/%3E%3Ccircle r='8' fill='%23d5ae75'/%3E%3C/g%3E%3Cg transform='translate(430 195) scale(.8)'%3E%3Cellipse rx='30' ry='13' fill='%23f5d7c4'/%3E%3Cellipse rx='30' ry='13' fill='%23dce8d8' transform='rotate(60)'/%3E%3Cellipse rx='30' ry='13' fill='%23e0d7ef' transform='rotate(120)'/%3E%3Ccircle r='8' fill='%23d5ae75'/%3E%3C/g%3E%3C/g%3E%3Cg fill='%239db6a3' opacity='.22'%3E%3Cellipse cx='145' cy='110' rx='42' ry='13' transform='rotate(-35 145 110)'/%3E%3Cellipse cx='170' cy='135' rx='38' ry='12' transform='rotate(28 170 135)'/%3E%3Cellipse cx='340' cy='270' rx='44' ry='13' transform='rotate(-28 340 270)'/%3E%3C/g%3E%3Cg fill='%23e4bdd0' opacity='.25'%3E%3Ccircle cx='260' cy='205' r='8'/%3E%3Ccircle cx='280' cy='220' r='5'/%3E%3Ccircle cx='240' cy='230' r='6'/%3E%3C/g%3E%3C/svg%3E")!important;
}
.decor-element-modal.theme-balloon .decor-element-modal-shell{
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='520' height='380' viewBox='0 0 520 380'%3E%3Cdefs%3E%3Cfilter id='b'%3E%3CfeGaussianBlur stdDeviation='7'/%3E%3C/filter%3E%3C/defs%3E%3Cg opacity='.22' filter='url(%23b)'%3E%3Ccircle cx='95' cy='75' r='62' fill='%23f4d3db'/%3E%3Ccircle cx='450' cy='80' r='55' fill='%23d8e5f4'/%3E%3Ccircle cx='390' cy='310' r='64' fill='%23e2d6ef'/%3E%3Ccircle cx='105' cy='310' r='58' fill='%23dce9dc'/%3E%3C/g%3E%3Cg stroke='%23c7a36f' stroke-width='2' fill='none' opacity='.28'%3E%3Cpath d='M84 122C90 175 70 210 82 262'/%3E%3Cpath d='M450 125C438 172 462 218 447 268'/%3E%3Cpath d='M300 106C308 150 292 193 304 235'/%3E%3C/g%3E%3Cg opacity='.42'%3E%3Cellipse cx='82' cy='82' rx='34' ry='44' fill='%23f5cad6'/%3E%3Cellipse cx='142' cy='55' rx='29' ry='38' fill='%23e4d3ef'/%3E%3Cellipse cx='445' cy='86' rx='32' ry='42' fill='%23d5e4f2'/%3E%3Cellipse cx='390' cy='315' rx='36' ry='46' fill='%23f4d7c2'/%3E%3Cellipse cx='305' cy='72' rx='26' ry='35' fill='%23d9e9da'/%3E%3Cellipse cx='118' cy='302' rx='31' ry='40' fill='%23f0d8e5'/%3E%3C/g%3E%3Cg fill='%23d4ad71' opacity='.45'%3E%3Ccircle cx='230' cy='82' r='5'/%3E%3Ccircle cx='255' cy='118' r='4'/%3E%3Ccircle cx='340' cy='250' r='5'/%3E%3Ccircle cx='188' cy='248' r='4'/%3E%3C/g%3E%3Cg stroke='%23d9b58a' stroke-width='5' fill='none' opacity='.22'%3E%3Cpath d='M15 250C90 205 130 215 185 260'/%3E%3Cpath d='M340 18C390 48 420 46 505 15'/%3E%3C/g%3E%3C/svg%3E")!important;
}
.decor-element-modal.theme-accessories .decor-element-modal-shell{
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='520' height='380' viewBox='0 0 520 380'%3E%3Cdefs%3E%3Cfilter id='b'%3E%3CfeGaussianBlur stdDeviation='7'/%3E%3C/filter%3E%3C/defs%3E%3Cg opacity='.20' filter='url(%23b)'%3E%3Ccircle cx='75' cy='80' r='58' fill='%23f2d5dc'/%3E%3Ccircle cx='455' cy='65' r='56' fill='%23dce6f4'/%3E%3Ccircle cx='425' cy='325' r='62' fill='%23e1d7ee'/%3E%3Ccircle cx='100' cy='310' r='55' fill='%23dce7d8'/%3E%3C/g%3E%3Cg fill='none' stroke='%23c4a06d' stroke-width='2' opacity='.34'%3E%3Cpath d='M80 120h64v98H80zM92 138h40M112 120V94M100 94h24M70 218h84'/%3E%3Cpath d='M320 82v105M294 112h52M304 112v25M336 112v25M290 137h34M322 137h34M298 137v22M348 137v22M312 187h16M302 195h36'/%3E%3Cpath d='M395 235h70v88h-70zM405 248h50M430 235v-28M414 207h32'/%3E%3C/g%3E%3Cg stroke='%23d8b57d' stroke-width='1.5' fill='none' opacity='.30'%3E%3Cpath d='M190 35C220 45 255 45 285 35'/%3E%3Cpath d='M198 38v15M220 42v18M245 43v19M270 40v17'/%3E%3C/g%3E%3Cg fill='%23f3cfd7' opacity='.30'%3E%3Ccircle cx='165' cy='285' r='18'/%3E%3Ccircle cx='192' cy='305' r='13'/%3E%3C/g%3E%3Cg fill='%23d9e5f1' opacity='.30'%3E%3Ccircle cx='450' cy='175' r='18'/%3E%3C/g%3E%3Cg fill='%23dce7d8' opacity='.28'%3E%3Cellipse cx='245' cy='285' rx='36' ry='11' transform='rotate(-28 245 285)'/%3E%3C/g%3E%3C/svg%3E")!important;
}
.decor-element-modal-shell h2,
.decor-element-modal-shell .decor-element-modal-note,
.decor-element-modal-grid{position:relative;z-index:1}
.decor-element-modal-grid img{box-shadow:0 7px 20px rgba(18,63,42,.10)}
.decor-element-empty{background:rgba(255,255,255,.84)!important;backdrop-filter:blur(4px)}
'''

if '/* Full-panel pastel luxury artwork for decor element modals */' not in text:
    text = text.replace('</style>', css + '\n</style>', 1)

path.write_text(text, encoding='utf-8')
