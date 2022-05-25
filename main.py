from PIL import Image, ImageChops, ImageEnhance
import itertools
# Number list
def detect(f,mode):
    numbers=[
    [1,[0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]],
    [4,[0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0]],
    [4,[0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0]],
    [0,[0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]],
    [1,[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1]],
    [3,[0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1]],
    [8,[0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1]],
    [7,[1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0]],
    [9,[0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1]],
    [9,[0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1]],
    [1,[0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]],
    [4,[0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0]],
    [3,[0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]],
    [9,[0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0]],
    [8,[0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0]],
    [8,[0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0]],
    [0,[0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1]],
    [0,[0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1]],
    [4,[0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0]],
    ]

    numbers2=[
        [1,[0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1]],
        [0,[0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]],
        [1,[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1]],
        [0,[0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]],
        [0,[0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1]]
    ]

    recognit=""
    img = f.convert("RGB")
    pixdata = img.load()
    temp=[]
    res=[]
    nums=[]
    gren=[]
    found=False
    innum=0
    for x in range(img.size[0]):
        if innum >img.size[1]-3:
            right=x-1
            found = False
            nums.append([left,right])
        innum=0
        for y in range(2,img.size[1]):
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
        for y in range(5,img.size[1]-4):
            if pixdata[x, y]!=(255, 255, 255):
                right=x
                found=True
    for i in nums:
        x, y = i
        if y-x<4:
            gren.append(i)
    for i in gren:
        nums.remove(i)

    # for i in nums:
    #     x,y=i
    #     for l in range(x,y):
    #         pixdata[l, 11] = (255, 53, 53)

    # for i in nums:
    #     x,y=i
    #     for l in range(x,y):
    #         pixdata[l, 11] = (255, 53, 53)
    #

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
    # img.show()
    for i in nums:
        index=0
        incrementy = img.size[1] / 4
        onenum,secnum=i
        incrementx = (secnum-onenum)/4
        basicx = incrementx
        for x in range(4):
            basey=incrementy
            for y in range(4):
                if pixdata[onenum + basicx-incrementx/2, 0+basey-incrementy/2] == (0, 0, 0):
                    temp.append(1)
                else:
                    temp.append(0)
                basey+=incrementy
            basicx+=incrementx
        index+=1
        res.append(temp)
        temp=[]
    if mode==1:
        for i in res:
            for n in numbers:
                for s in n:
                    if i == s:
                        recognit+=str(n[0])
    else:
        for i in res:
            for n in numbers2:
                for s in n:
                    if i == s:
                        recognit+=str(n[0])

    return int(recognit)

if __name__ == '__main__':
    f = Image.open("f1.jpg")
    fin=detect(f, 1)
    print(fin)



