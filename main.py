from PIL import Image, ImageChops, ImageEnhance
im = Image.open("f.png")
img = im.convert("RGB")
pixdata = img.load()
for x in range(img.size[0]):
    for y in range(5,16):
        if pixdata[x, 11]!=(255, 255, 255):
            left=x
            break
print(x)