"""Generate the site's icon and social card. Requires Pillow."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT = Path(__file__).resolve().parents[1]
INK, RED, PAPER, TINT = '#0d253f', '#ab4545', '#f8f5ec', '#f1e4df'
BLUE = '#163e6a'
def book(d, scale, offset=(0,0), fill=PAPER):
    def pt(x,y):return (offset[0]+x*scale,offset[1]+y*scale)
    d.polygon([pt(x,y) for x,y in [(10,16),(32,22),(54,16),(54,46),(32,52),(10,46)]],fill=fill)
    d.line([pt(32,22),pt(32,52)],fill=INK,width=max(1,round(3*scale)))
    for a,b in [((16,26),(26,29)),((16,35),(26,38)),((38,29),(48,26)),((38,38),(48,35))]:
        d.line([pt(*a),pt(*b)],fill=INK,width=max(1,round(2.5*scale)))
svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="{BLUE}"/><path d="M10 16 32 22 54 16V46L32 52 10 46Z" fill="{TINT}"/><path d="M32 22V52" stroke="{INK}" stroke-width="3"/><path d="m16 26 10 3m-10 6 10 3m12-9 10-3m-10 12 10-3" fill="none" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/></svg>'
(ROOT/'assets/favicon.svg').write_text(svg+'\n')
ic=Image.new('RGB',(512,512),BLUE);book(ImageDraw.Draw(ic),8,fill=TINT)
ic.save(ROOT/'favicon.ico',sizes=[(16,16),(32,32),(48,48)])
ic.resize((180,180),Image.Resampling.LANCZOS).save(ROOT/'assets/apple-touch-icon.png')
def font(name,size):return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/'+name+'.ttf',size)
im=Image.new('RGB',(1200,630),PAPER);d=ImageDraw.Draw(im)
d.rectangle((0,0,1200,15),fill=BLUE)
d.text((64,49),'the book club.',font=font('DejaVuSans-Bold',29),fill=INK)
d.text((64,95),'L O N D O N',font=font('DejaVuSans',15),fill=INK)
d.line((64,140,1136,140),fill='#d8d4ce',width=2)
for y,t in [(178,'An old book.'),(260,'Big questions.'),(342,'Good company.')]:
    d.text((60,y),t,font=font('DejaVuSerif',67),fill=RED if y==342 else INK)
d.ellipse((855,198,1105,448),fill=RED)
book(d,3,(884,225))
d.text((64,463),'Make up your own mind.',font=font('DejaVuSans-Bold',27),fill=RED)
d.rectangle((0,544,1200,630),fill=BLUE)
d.text((64,572),'Waterloo, London · Questions welcome.',font=font('DejaVuSans',21),fill=PAPER)
d.text((868,575),'thebookclub.london',font=font('DejaVuSans',20),fill=TINT)
im.save(ROOT/'assets/book-club-social-v3.jpg',quality=90,optimize=True)
