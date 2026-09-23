from pathlib import Path

p = Path('index.html')
text = p.read_text(encoding='utf-8')

text = text.replace('https://lushnlightdecors.ca/social-preview.jpg?v=20260923b', 'https://lushnlightdecors.ca/social-preview.jpg')
text = text.replace('<meta property="og:image:secure_url" content="https://lushnlightdecors.ca/social-preview.jpg">\n', '')

p.write_text(text, encoding='utf-8')
print('Simplified WhatsApp Open Graph image metadata')
