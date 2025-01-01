from PIL import  Image
from PIL import ImageFont, ImageDraw

base_image = Image.open("photo.jpg")
slave_image = Image.open("sun.jpg")
base_image = base_image.resize((480, 270))
slave_image = slave_image.resize((120,70))
base_image.paste(slave_image, (30,170))

draw = ImageDraw.Draw(base_image)
font = ImageFont.truetype("arial.ttf", 30)
draw.text((20,40), 'Приветик!', font=font)

base_image.show()
# print(im.format, im.size, im.mode)
# out = im.resize((480, 270))
# out.show()