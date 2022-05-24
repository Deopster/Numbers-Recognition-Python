from PIL import Image, ImageChops, ImageEnhance
import itertools
# Number list
one=[]



im = Image.open("f.jpg")
img = im.convert("RGB")
pixdata = img.load()
nums=[]
gren=[]
found=False
innum=0
for x in range(img.size[0]):
    if innum >17:
        right=x-1
        found = False
        nums.append([left,right])
    innum=0
    for y in range(2,20):
        if pixdata[x, y]!=(255, 255, 255):
            if found is False:
                left=x
                found=True
        else:
            if found is True:
                innum+=1
found=False
for x in reversed(range(img.size[0])):
    if found is  True:
        break
    for y in range(5,16):
        if pixdata[x, y]!=(255, 255, 255):
            right=x
            found=True
print(left,right)
print(nums)
for i in nums:
    x, y = i
    if y-x<6:
        gren.append(i)
for i in gren:
    nums.remove(i)
# for i in nums:
#     x,y=i
#     for l in range(x,y):
#         pixdata[l, 11] = (255, 53, 53)
# dump=img.crop((left, 0, right, img.size[1])).save('dump.jpg', quality=100)


# for i in nums:
#     incrementy = img.size[1] / 4
#     onenum,secnum=i
#     incrementx = (secnum-onenum)/4
#     basicx = incrementx
#     for x in range(4):
#         basey=incrementy
#         for y in range(4):
#             pixdata[onenum + basicx-incrementx/2, 0+basey-incrementy/2] = (255, 53, 53)
#             basey+=incrementy
#             print(basey)
#         basicx+=incrementx
print(nums)
img.show()


