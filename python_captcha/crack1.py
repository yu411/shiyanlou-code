import PIL import Image
import hashlib
import time
import os
import math

class VectorCompare:
    def magnitude(self, consordance):
        total = 0
        for word,count in concordance.items():
            total += count ** 2
        return math.sqrt(total)


    def relation(self,concordance1, concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance.items():
            if word in concordance2:
                topvalue += count * concordance2[word]
        return topvalue / (self.mangnitude(concordance1) * self.magnitude(concordance2))

def buildvetor(im):
    dl = {}

    count = 0
    for i in im.getdata():
        dl[count] = i
        count += 1
    return dl

v = VectorCompare()

iconset = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
imageset = []
for letter in iconset:
    for img in os.listdir('./iconset/%s/'%(letter)):
        temp = []
        if img != "Thumbs.db" and img != ".DS_Store":
            temp.append(buildvector(Image.open("./iconset/%s/%s"%(letter,img))))
        imagset.append({letter:temp})
count = 0

for letter in letters:
    m = hashlib.md5()
    im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))

    guess = []

    for image in imageset:
        for x,y in image.items():
            if len(y) != 0:
                guess.append((v.relation(y[0], buildvetor(im3)),x))

    guess.sort(reverse=True)
    print(guess[0])
    count += 1
