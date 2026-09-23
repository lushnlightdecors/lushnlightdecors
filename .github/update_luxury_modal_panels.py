from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

css = r'''
/* Refined luxury decor modal panels */
.decor-element-modal{background:rgba(28,27,24,.72)!important}
.decor-element-modal::before{display:none!important;background:none!important;opacity:0!important}
.decor-element-modal-shell{background-color:#fbf8ef!important;background-repeat:no-repeat!important;background-position:right top,left bottom!important;background-size:270px auto,220px auto!important}
.decor-element-modal.theme-floral .decor-element-modal-shell{
background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='320' height='250' viewBox='0 0 320 250'%3E%3Cg fill='none' stroke='%23b69564' stroke-width='2' opacity='.22'%3E%3Cpath d='M236 20c-6 42-23 78-61 108-24 19-48 29-74 34'/%3E%3Cpath d='M191 77c18-22 37-32 58-34-2 20-14 39-38 51'/%3E%3Cpath d='M160 108c-7-27-3-49 11-67 16 17 22 39 17 66'/%3E%3C/g%3E%3Cg fill='%23d9c9a6' opacity='.28'%3E%3Cellipse cx='245' cy='42' rx='18' ry='8' transform='rotate(-38 245 42)'/%3E%3Cellipse cx='265' cy='56' rx='18' ry='8' transform='rotate(12 265 56)'/%3E%3Cellipse cx='252' cy='72' rx='18' ry='8' transform='rotate(52 252 72)'/%3E%3Cellipse cx='230' cy='62' rx='18' ry='8' transform='rotate(102 230 62)'/%3E%3Ccircle cx='248' cy='58' r='7' fill='%23b69564' opacity='.34'/%3E%3C/g%3E%3Cg fill='%23123f2a' opacity='.10'%3E%3Cellipse cx='90' cy='182' rx='38' ry='13' transform='rotate(-28 90 182)'/%3E%3Cellipse cx='132' cy='156' rx='34' ry='12' transform='rotate(26 132 156)'/%3E%3C/g%3E%3C/svg%3E"),url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='250' height='200' viewBox='0 0 250 200'%3E%3Cg fill='none' stroke='%23123f2a' stroke-width='2' opacity='.11'%3E%3Cpath d='M18 185c38-35 63-75 73-124'/%3E%3Cpath d='M58 130c-20-8-35-21-44-39 23-3 43 5 59 24'/%3E%3Cpath d='M77 91c19-16 39-21 60-17-7 22-21 38-44 47'/%3E%3C/g%3E%3C/svg%3E");
}
.decor-element-modal.theme-balloon .decor-element-modal-shell{
background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='320' height='250' viewBox='0 0 320 250'%3E%3Cg fill='none' stroke='%23b69564' stroke-width='2' opacity='.22'%3E%3Cellipse cx='238' cy='54' rx='34' ry='43'/%3E%3Cpath d='M238 97l-5 9h10zM238 106c-12 28-5 54 7 82'/%3E%3Cellipse cx='286' cy='86' rx='27' ry='35'/%3E%3Cpath d='M286 121l-4 8h8zM286 129c-14 24-18 46-14 70'/%3E%3C/g%3E%3Cg fill='%23d9c9a6' opacity='.24'%3E%3Cellipse cx='175' cy='34' rx='29' ry='38'/%3E%3Cpath d='M175 72l-5 8h10z' fill='%23b69564' opacity='.35'/%3E%3C/g%3E%3Cg fill='%23123f2a' opacity='.07'%3E%3Cellipse cx='108' cy='88' rx='26' ry='34'/%3E%3Cellipse cx='72' cy='48' rx='22' ry='29'/%3E%3C/g%3E%3C/svg%3E"),url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='230' height='190' viewBox='0 0 230 190'%3E%3Cg fill='none' stroke='%23123f2a' stroke-width='2' opacity='.10'%3E%3Cellipse cx='38' cy='140' rx='23' ry='31'/%3E%3Cpath d='M38 171l-4 7h8zM38 178c10-24 14-42 11-60'/%3E%3Cellipse cx='84' cy='154' rx='19' ry='26'/%3E%3Cpath d='M84 180c5-18 2-34-6-50'/%3E%3C/g%3E%3C/svg%3E");
}
.decor-element-modal.theme-accessories .decor-element-modal-shell{
background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='330' height='250' viewBox='0 0 330 250'%3E%3Cg fill='none' stroke='%23b69564' stroke-width='2' opacity='.22'%3E%3Cpath d='M250 30v116M224 60h52M234 60v25M266 60v25M218 85h32M250 85h32M226 85v22M274 85v22M242 146h16M232 154h36'/%3E%3Ccircle cx='224' cy='54' r='5'/%3E%3Ccircle cx='276' cy='54' r='5'/%3E%3Ccircle cx='218' cy='80' r='5'/%3E%3Ccircle cx='282' cy='80' r='5'/%3E%3Cpath d='M112 58h58v92h-58zM124 70h34M141 58V42M132 42h18M104 150h74'/%3E%3C/g%3E%3Cg fill='%23d9c9a6' opacity='.20'%3E%3Ccircle cx='295' cy='34' r='4'/%3E%3Ccircle cx='306' cy='52' r='3'/%3E%3Ccircle cx='288' cy='69' r='3'/%3E%3C/g%3E%3C/svg%3E"),url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='230' height='190' viewBox='0 0 230 190'%3E%3Cg fill='none' stroke='%23123f2a' stroke-width='2' opacity='.10'%3E%3Cpath d='M25 164h96M43 164V96h60v68M52 106h42M128 160v-52h44v52M137 117h26'/%3E%3Ccircle cx='184' cy='119' r='20'/%3E%3Cpath d='M184 99V82M184 139v18M164 119h-17M204 119h17'/%3E%3C/g%3E%3C/svg%3E");
}
.decor-element-modal-shell h2,.decor-element-modal-shell .decor-element-modal-note,.decor-element-modal-grid{position:relative;z-index:1}
'''

marker = '/* Refined luxury decor modal panels */'
if marker not in text:
    text = text.replace('</style>', css + '\n</style>', 1)

path.write_text(text, encoding='utf-8')
