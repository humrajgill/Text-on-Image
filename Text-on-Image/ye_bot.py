import textwrap
from PIL import Image, ImageDraw, ImageFont
import requests, json
import random

apiURL = "https://api.kanye.rest"

imgSize = [800,800]
myFont = ImageFont.truetype('Roboto-Medium.ttf', 48)
fontColor = 'white'

colors = ['C9E3AC', '90BE6D', 'EA9010', '37371F', 'CCB7AE', '565264', 'F5FDC6', 'F5C396', 'D0B17A', 'C44536','772E25', 'EDDDD4',
          '197278', 'CA054D', 'B96D40', 'A4D4B4', '3B1C32', '531CB3', 'AA7BC3', 'CC92C2', 'DBA8AC', '134611', '3DA35D', 'E8FCCF'
         ]

rdm = random.randrange(0,24) # for color and image

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# Image Generation
def create_image(size, bgColor, message, font, fontColor):
    W, H = size
    image = Image.new('RGBA', size, bgColor)
    
    bg = Image.open(f'images/ye{(int(rdm/2))}.png').resize(imgSize) #.convert('RGBA') if not png
    bg.putalpha(100)
    
    image = Image.alpha_composite(image,bg)
    draw = ImageDraw.Draw(image)
    
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    
    draw.multiline_text(((W-w)/2, (H-h)/2), message, font=font, fill=fontColor, align='center')
    return image

# Quote Generation
headers = {'Accept': 'application/json'}
def get_quote():
    r = requests.get(apiURL)
    quote_dict = json.loads(r.text)
    text = textwrap.wrap(quote_dict['quote'], width=30, subsequent_indent="\n")
    return "".join(text)


quoteStr = get_quote()
myImage = create_image(imgSize, hex_to_rgb(colors[rdm]), quoteStr, myFont, fontColor)
myImage.show()

# myImage.save("kquote.png")

