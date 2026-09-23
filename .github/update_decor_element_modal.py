from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

text = text.replace('<div class="card decor-element-card"><h3>Floral Decor</h3><p>Modern floral arrangements and statement pieces that elevate your setup.</p></div>', '<button class="card decor-element-card decor-element-trigger" type="button" data-decor-element="floral"><h3>Floral Decor</h3><p>Modern floral arrangements and statement pieces that elevate your setup.</p><span class="learn-more">View Floral Decor →</span></button>', 1)
text = text.replace('<div class="card decor-element-card"><h3>Balloon Decor</h3><p>Custom garlands and arrangements designed around your preferred colour palette.</p></div>', '<button class="card decor-element-card decor-element-trigger" type="button" data-decor-element="balloon"><h3>Balloon Decor</h3><p>Custom garlands and arrangements designed around your preferred colour palette.</p><span class="learn-more">View Balloon Decor →</span></button>', 1)
text = text.replace('<div class="card decor-element-card"><h3>Backdrops & Centerpieces</h3><p>Arch stands, draping, decals, cake tables and elegant centerpiece options.</p></div>', '<button class="card decor-element-card decor-element-trigger" type="button" data-decor-element="accessories"><h3>Centerpieces, Welcome Stands & Accessories</h3><p>Explore centerpieces, welcome stands, lamps, candelabras, decorative lights, curtain lights and other finishing touches.</p><span class="learn-more">View Accessories →</span></button>', 1)

css = '''
.decor-element-trigger{width:100%;text-align:left;font:inherit;color:inherit;cursor:pointer;appearance:none;transition:transform .22s ease,box-shadow .22s ease,border-color .22s ease}
.decor-element-trigger:hover{transform:translateY(-4px);box-shadow:0 14px 34px rgba(18,63,42,.12);border-color:var(--gold)}
.decor-element-trigger .learn-more{display:inline-block;margin-top:10px;color:var(--gold);font-weight:700;font-size:.9rem}
.decor-element-modal{position:fixed;inset:0;z-index:120;background:rgba(12,24,18,.94);display:none;align-items:center;justify-content:center;padding:24px}
.decor-element-modal.open{display:flex}
.decor-element-modal-shell{position:relative;width:min(1180px,94vw);max-height:92vh;background:#fbf8ef;border-radius:22px;padding:72px 28px 28px;overflow:auto;box-shadow:0 22px 70px rgba(0,0,0,.28)}
.decor-element-modal h2{font-family:Georgia,serif;color:var(--wine);text-align:center;margin:0 0 8px;font-size:2.25rem}
.decor-element-modal-note{text-align:center;color:#52635a;margin:0 auto 24px;max-width:700px}
.decor-element-modal-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.decor-element-modal-grid img{width:100%;height:320px;object-fit:cover;border-radius:16px;display:block;cursor:pointer;transition:transform .3s ease}
.decor-element-modal-grid img:hover{transform:scale(1.025)}
.decor-element-empty{text-align:center;background:#fff;border:1px solid #e8dfcf;border-radius:18px;padding:42px 24px;color:#52635a}
.decor-element-empty strong{display:block;color:var(--wine);font-family:Georgia,serif;font-size:1.25rem;margin-bottom:8px}
.decor-element-close{position:absolute;right:20px;top:18px;border:0;background:#fff;color:var(--wine);width:44px;height:44px;border-radius:50%;font-size:1.5rem;cursor:pointer;box-shadow:0 4px 16px rgba(0,0,0,.12)}
.decor-element-viewer{position:fixed;inset:0;z-index:130;background:rgba(12,24,18,.97);display:none;align-items:center;justify-content:center;padding:24px}
.decor-element-viewer.open{display:flex}
.decor-element-viewer img{max-width:min(1100px,90vw);max-height:86vh;object-fit:contain;border-radius:10px}
.decor-element-viewer button{position:absolute;border:0;background:rgba(255,255,255,.92);color:var(--wine);width:44px;height:44px;border-radius:50%;font-size:1.5rem;cursor:pointer}
.decor-viewer-close{right:22px;top:22px}.decor-viewer-prev{left:22px}.decor-viewer-next{right:22px}
@media(max-width:760px){.decor-element-modal{padding:10px}.decor-element-modal-shell{width:96vw;padding:66px 14px 20px}.decor-element-modal-grid{grid-template-columns:1fr 1fr}.decor-element-modal-grid img{height:230px}.decor-viewer-prev{left:8px}.decor-viewer-next{right:8px}.decor-viewer-close{right:8px;top:8px}}
@media(max-width:480px){.decor-element-modal-grid{grid-template-columns:1fr}.decor-element-modal-grid img{height:auto}}
'''
if '.decor-element-modal{' not in text:
    text = text.replace('</style>', css + '\n</style>', 1)

markup = '''
<div class="decor-element-modal" id="decor-element-modal" aria-hidden="true" role="dialog" aria-modal="true" aria-label="Decor element gallery">
  <div class="decor-element-modal-shell">
    <button class="decor-element-close" type="button" aria-label="Close">×</button>
    <h2 id="decor-element-title">Decor Gallery</h2>
    <p class="decor-element-modal-note" id="decor-element-note">Explore examples from our decor collection.</p>
    <div class="decor-element-modal-grid" id="decor-element-modal-grid"></div>
  </div>
</div>
<div class="decor-element-viewer" id="decor-element-viewer" aria-hidden="true">
  <button class="decor-viewer-close" type="button" aria-label="Close">×</button>
  <button class="decor-viewer-prev" type="button" aria-label="Previous photo">‹</button>
  <img id="decor-element-viewer-image" alt="LushnLight Decors decor photo">
  <button class="decor-viewer-next" type="button" aria-label="Next photo">›</button>
</div>
'''
if 'id="decor-element-modal"' not in text:
    text = text.replace('</body>', markup + '\n</body>', 1)

script = '''
<script id="decor-element-gallery-script">
(function(){
  const triggers=[...document.querySelectorAll('.decor-element-trigger')];
  const modal=document.getElementById('decor-element-modal');
  const grid=document.getElementById('decor-element-modal-grid');
  const title=document.getElementById('decor-element-title');
  const note=document.getElementById('decor-element-note');
  const viewer=document.getElementById('decor-element-viewer');
  const viewerImage=document.getElementById('decor-element-viewer-image');
  if(!triggers.length||!modal||!grid||!viewer||!viewerImage)return;
  let data=null,currentPhotos=[],currentIndex=0;
  async function loadData(){if(data)return data;const r=await fetch('decor-elements.json?v='+Date.now());data=await r.json();return data;}
  function closeViewer(){viewer.classList.remove('open');viewer.setAttribute('aria-hidden','true');}
  function showViewer(i){if(!currentPhotos.length)return;currentIndex=(i+currentPhotos.length)%currentPhotos.length;viewerImage.src=currentPhotos[currentIndex];viewer.classList.add('open');viewer.setAttribute('aria-hidden','false');}
  function closeModal(){modal.classList.remove('open');modal.setAttribute('aria-hidden','true');document.body.style.overflow='';closeViewer();}
  async function openCategory(key){
    const all=await loadData();const cat=all[key];if(!cat)return;
    currentPhotos=Array.isArray(cat.photos)?cat.photos:[];
    title.textContent=cat.label;
    note.textContent=key==='floral'?'Floral-focused setups from our decor collection.':key==='balloon'?'Balloon-focused setups from our decor collection.':'Additional decor pieces including centerpieces, welcome stands, lamps, candelabras, lights and accessories.';
    if(currentPhotos.length){grid.innerHTML=currentPhotos.map((src,i)=>'<img src="'+src+'" loading="lazy" data-index="'+i+'" alt="'+cat.label+' by LushnLight Decors">').join('');}
    else{grid.innerHTML='<div class="decor-element-empty" style="grid-column:1/-1"><strong>New accessory gallery coming soon.</strong><span>We’re preparing photos of our centerpieces, welcome stands, lamps, candelabras, decorative lights, curtain lights and other accessories. New images added to this category will automatically appear here.</span></div>';}
    modal.classList.add('open');modal.setAttribute('aria-hidden','false');document.body.style.overflow='hidden';
  }
  triggers.forEach(btn=>btn.addEventListener('click',()=>openCategory(btn.dataset.decorElement)));
  grid.addEventListener('click',e=>{const img=e.target.closest('img[data-index]');if(img)showViewer(Number(img.dataset.index));});
  modal.querySelector('.decor-element-close').addEventListener('click',closeModal);
  modal.addEventListener('click',e=>{if(e.target===modal)closeModal();});
  viewer.querySelector('.decor-viewer-close').addEventListener('click',closeViewer);
  viewer.querySelector('.decor-viewer-prev').addEventListener('click',()=>showViewer(currentIndex-1));
  viewer.querySelector('.decor-viewer-next').addEventListener('click',()=>showViewer(currentIndex+1));
  viewer.addEventListener('click',e=>{if(e.target===viewer)closeViewer();});
  document.addEventListener('keydown',e=>{if(viewer.classList.contains('open')){if(e.key==='Escape')closeViewer();else if(e.key==='ArrowLeft')showViewer(currentIndex-1);else if(e.key==='ArrowRight')showViewer(currentIndex+1);}else if(modal.classList.contains('open')&&e.key==='Escape')closeModal();});
})();
</script>
'''
if 'id="decor-element-gallery-script"' not in text:
    text = text.replace('</body>', script + '\n</body>', 1)

path.write_text(text, encoding='utf-8')
