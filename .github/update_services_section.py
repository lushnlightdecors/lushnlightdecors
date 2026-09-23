from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

old = '''<section id="services"><div class="wrap"><div class="title"><h2>Decor for Every Celebration</h2><p>Stylish setups tailored to your theme, space and special occasion.</p></div><div class="grid">
<a class="card service-card-link" href="wedding-decor/"><h3>Weddings & Receptions</h3><p>Elegant backdrops, florals, draping, lighting and statement details for your celebration.</p><span class="learn-more">Explore Wedding Decor →</span></a>
<a class="card service-card-link" href="mehndi-traditional-decor/"><h3>Jaggo, Mehndi, Haldi or Traditional Event</h3><p>Colourful draping, florals, seating and backdrops for vibrant traditional celebrations.</p><span class="learn-more">Explore Traditional Decor →</span></a>
<a class="card service-card-link" href="birthday-decor/"><h3>Birthdays & Milestones</h3><p>Custom balloon palettes, backdrops, decals and cake-table styling for memorable birthdays.</p><span class="learn-more">Explore Birthday Decor →</span></a>
<a class="card service-card-link" href="baby-shower-decor/"><h3>Baby Showers</h3><p>Beautifully coordinated backdrops, balloons, florals and details for welcoming the little one.</p><span class="learn-more">Explore Baby Shower Decor →</span></a>
<a class="card service-card-link" href="aqiqah-decor/"><h3>Aqiqah</h3><p>Elegant, personalized decor with backdrops, balloons, florals and signage for a meaningful celebration.</p><span class="learn-more">Explore Aqiqah Decor →</span></a>
<div class="card"><h3>Floral Decor</h3><p>Modern floral arrangements and statement pieces that elevate your setup.</p></div>
<div class="card"><h3>Balloon Decor</h3><p>Custom garlands and arrangements designed around your preferred colour palette.</p></div>
<div class="card"><h3>Backdrops & Centerpieces</h3><p>Arch stands, draping, decals, cake tables and elegant centerpiece options.</p></div>
</div></div></section>'''

new = '''<section id="services"><div class="wrap"><div class="title"><h2>Decor for Every Celebration</h2><p>Stylish setups tailored to your theme, space and special occasion.</p></div><div class="grid celebration-grid">
<a class="card service-card-link" href="wedding-decor/"><h3>Weddings & Receptions</h3><p>Elegant backdrops, florals, draping, lighting and statement details for your celebration.</p><span class="learn-more">Explore Wedding Decor →</span></a>
<a class="card service-card-link" href="mehndi-traditional-decor/"><h3>Jaggo, Mehndi, Haldi or Traditional Event</h3><p>Colourful draping, florals, seating and backdrops for vibrant traditional celebrations.</p><span class="learn-more">Explore Traditional Decor →</span></a>
<a class="card service-card-link" href="birthday-decor/"><h3>Birthdays & Milestones</h3><p>Custom balloon palettes, backdrops, decals and cake-table styling for memorable birthdays.</p><span class="learn-more">Explore Birthday Decor →</span></a>
<a class="card service-card-link" href="baby-shower-decor/"><h3>Baby Showers</h3><p>Beautifully coordinated backdrops, balloons, florals and details for welcoming the little one.</p><span class="learn-more">Explore Baby Shower Decor →</span></a>
<a class="card service-card-link" href="aqiqah-decor/"><h3>Aqiqah</h3><p>Elegant, personalized decor with backdrops, balloons, florals and signage for a meaningful celebration.</p><span class="learn-more">Explore Aqiqah Decor →</span></a>
</div>
<div class="service-elements-heading"><div class="eyebrow">What We Style</div><h2>Decor Elements & Styling</h2><p>Mix and match the setup pieces and decorative elements that bring your event vision together.</p></div>
<div class="grid decor-elements-grid">
<div class="card decor-element-card"><h3>Floral Decor</h3><p>Modern floral arrangements and statement pieces that elevate your setup.</p></div>
<div class="card decor-element-card"><h3>Balloon Decor</h3><p>Custom garlands and arrangements designed around your preferred colour palette.</p></div>
<div class="card decor-element-card"><h3>Backdrops & Centerpieces</h3><p>Arch stands, draping, decals, cake tables and elegant centerpiece options.</p></div>
</div></div></section>'''

if old not in text:
    raise SystemExit('Expected services block was not found; no changes made.')

text = text.replace(old, new, 1)

css = '''
.service-elements-heading{text-align:center;max-width:720px;margin:58px auto 30px;padding-top:42px;border-top:1px solid #e7ddcd}
.service-elements-heading h2{font-family:Georgia,serif;font-size:2rem;color:var(--wine);margin:7px 0 8px}
.service-elements-heading p{margin:0 auto;max-width:650px;color:#52635a}
.decor-element-card{background:linear-gradient(180deg,#fff,#fcfaf4)}
@media(max-width:760px){.service-elements-heading{margin-top:42px;padding-top:34px}.service-elements-heading h2{font-size:1.8rem}}
'''

if '.service-elements-heading{' not in text:
    text = text.replace('</style>', css + '\n</style>', 1)

path.write_text(text, encoding='utf-8')
