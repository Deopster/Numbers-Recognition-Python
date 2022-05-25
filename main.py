from PIL import Image, ImageChops, ImageEnhance
import itertools
# Number list
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
    [0,[0]]
    ]

def detect(f):
    scale=4
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

    #Отображение коробок букв

    # for i in nums:
    #     x,y=i
    #     for l in range(x,y):
    #         pixdata[l, 11] = (255, 53, 53)
    # img.show()

    #конец блока
    for i in nums:
        index=0
        incrementy = img.size[1] / scale
        onenum,secnum=i
        incrementx = (secnum-onenum)/scale
        basicx = incrementx
        for x in range(scale):
            basey=incrementy
            for y in range(scale):
                if pixdata[onenum + basicx-incrementx/2, 0+basey-incrementy/2] == (0, 0, 0):
                    temp.append(1)
                else:
                    temp.append(0)
                basey+=incrementy
            basicx+=incrementx
        index+=1
        res.append(temp)
        temp=[]
    f = open('traindata.txt', 'a')
    f.write("\n" + "------ Scale = "+str(scale) + "\n");
    f.close()
    for i in res:
        found = False
        for n in numbers:
            if found is False:
                pass
            if n == numbers[len(numbers) - 1] and found is False:
                recognit += '*'
                f = open('traindata.txt', 'a')
                f.write('[*' + ',' + str(n[1]) + '],' + "\n");
                f.close()
            for s in n:
                if i == s:
                    recognit += str(n[0])
                    f = open('traindata.txt', 'a')
                    f.write('[' + str(n[0]) + ',' + str(n[1]) + '],' + "\n");
                    f.close()
                    found = True
    return recognit

if __name__ == '__main__':

    f = Image.open("f3.jpg")
    print(detect(f))

