# -*- coding: utf-8 -*-
from PIL import Image,ImageDraw,ImageFont,ImageOps
from pathlib import Path
import json
root=Path(__file__).parent
font='/System/Library/Fonts/Supplemental/Arial Unicode.ttf'
def f(n):return ImageFont.truetype(font,n)
im=Image.new('RGB',(1200,630),'#f5f2e9');d=ImageDraw.Draw(im)
# Original diagram avoids third-party photo licensing requirements in the share card.
d.rectangle((0,0,18,630),fill='#215647')
d.text((58,40),'URBAN STITCHING  /  TAIPEI',font=f(20),fill='#215647')
d.text((55,92),'城市縫合',font=f(88),fill='#202e2c')
d.text((60,225),'接回生活，',font=f(51),fill='#202e2c')
d.text((60,296),'還是換一種撕裂？',font=f(51),fill='#215647')
d.rounded_rectangle((60,418,570,477),radius=5,fill='#215647')
d.text((80,430),'8個國際案例 × 台北10處地圖',font=f(28),fill='#f5f2e9')
d.text((60,520),'步行・車行・公共空間・誰受益？',font=f(25),fill='#586762')
d.text((60,570),'公共空間研究筆記  |  2026.10.27',font=f(18),fill='#586762')
# Abstract city blocks and a corridor with a restored local crossing.
d.rounded_rectangle((670,40,1150,590),radius=20,fill='#e7e8dc')
for x,y,w,h in [(700,72,105,80),(828,72,128,80),(978,72,140,80),(700,177,165,70),(890,177,90,70),(1005,177,113,70),(700,398,100,63),(825,398,145,63),(995,398,123,63),(700,486,165,70),(890,486,228,70)]:d.rounded_rectangle((x,y,x+w,y+h),radius=6,fill='#b6c4b2')
d.rectangle((670,273,1150,367),fill='#334843')
for x in range(684,1140,42):d.rectangle((x,316,x+22,320),fill='#c0cdba')
d.line([(855,240),(855,402)],fill='#f5f2e9',width=56)
d.line([(855,240),(855,402)],fill='#ac4b30',width=10)
d.ellipse((836,222,874,260),fill='#ac4b30');d.ellipse((836,382,874,420),fill='#ac4b30')
d.text((925,302),'→',font=f(35),fill='#e2edb4')
d.text((925,335),'區域交通',font=f(16),fill='#e2edb4')
d.text((884,248),'接回地方',font=f(20),fill='#ac4b30')
im.save(root/'assets/share-card.jpg',quality=94,optimize=True)
print('share-card.jpg: 1200 × 630')
