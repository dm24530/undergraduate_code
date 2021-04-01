# -- coding: gbk --
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母(65-90表示26个大写英文字母)
def rndChar():
    return chr(random.randint(65,90))   #返回65~90之间的任意一个数，再将它转化成字母

def rndColor():  #随机颜色，一个验证码背景，一个字母本身，使用rgb模式
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

#设置验证码背景宽度x高度240x60:
width = 60 * 4
height = 60
#创建一个纯色的背景
image = Image.new('RGB', (width, height), (255, 255, 255))
#创建Font对象,36是字体大小：
font = ImageFont.truetype( 'C:\Windows\Fonts\AGENCYR.TTF', 36)
#创建Draw对象
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x, y),fill=rndColor())
#输出4个文字60 * t ，确定写字的位置
for t in range(4):
    draw.text((60 * t + 10,10),rndChar(),font = font,fill = rndColor2())
#模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')