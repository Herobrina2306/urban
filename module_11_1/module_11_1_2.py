from PIL import Image, ImageOps, ImageDraw

im = Image.open('kitten.jpg')

print(im.format, im.size, im.mode)
size = (850, 720)
with Image.open('kitten.jpg') as img_:
    img_ = ImageOps.fit(img_, size)
    draw = ImageDraw.Draw(img_)
    draw.text((100, 650), 'I love Python', font_size=50)
    img_ = img_.crop((0, 0, 700, 720))
    img_.save('kit.png')
    img_.show()

