import numpy as np
import matplotlib.pyplot as pyp


### VARS ###

clr_rectangle = [25, 128, 40]      #(green)
clr_triangle = [225,100, 225]    #(purple)
clr_fade =  [225, 130, 50] #(red)
clr_fade_applied = [-15,10,0]

cookie_clrA = [69,42,19]
cookie_clrB = [75,40,23]
cookie_clrC = [87,47,26]
cookie_clrD = [139,75,43]
cookie_clrE = [185,115,53]
cookie_clrF = [217,131,62]
cookie_clrG = [232,152,80]


### DATAGEN ###
base_img = np.zeros([16,16,3], dtype=np.uint8)
img = np.zeros([16,16,3], dtype=np.uint8) #datagen
#imgB = imgA[:]
#imgC = imgA[:]
#imgD = imgA[:]

### SHAPES ###

def rectangle(pos, size, clr):
    for y in range(size[1]):
        for x in range(size[0]):
            img[pos[1], pos[0]] = clr #matplotlib uses [y,x] instead of [x,y], also should be dynamic but didn't have enough time
            pos[0] += 1
        pos[1] += 1
        pos[0] -= size[0]
    
    

def triangle(pos, size, clr):
    for y in range(size[1]):
        for x in range(size[0] - (y + 1)):
            img[pos[1],pos[0]] = clr
            pos[0] += 1
        pos[1] += 1
        pos[0] -= size[0] - y - 2
    

#def rectangle_fade(pos,size,clr,fade_clr):
#    for y in range(size[1]):
#        for x in range(size[0]):
#            imgC[pos[1], pos[0]] = clr
#            clr[0] += fade_clr[0]
#            clr[1] += fade_clr[1]
#            clr[2] += fade_clr[2]
#            print(clr, fade_clr)
#            pos[0] += 1
#        pos[1] += 1
#        pos[0] -= size[0]
#        clr[0] -= fade_clr[0] * size[0]
#        clr[1] -= fade_clr[1] * size[0]
#        clr[2] -= fade_clr[2] * size[0]


# special OwO

def rectangle_fade(pos, size, clr, fade_clr):
    for y in range(size[1]):
        for x in range(size[0]):
            img[pos[1],pos[0]] = clr
            pos[0] += 1
        pos[1] += 1
        pos[0] -= size[0]
        clr = np.add(clr, fade_clr) # compact!
        #clr[0] += fade_clr[0]
        #clr[1] += fade_clr[1]
        #clr[2] += fade_clr[2]
    

def cookie():
    rectangle([1,5],[14,6],cookie_clrD)
    rectangle([13,4],[1,1],cookie_clrD)

    rectangle([1,6],[14,3],cookie_clrF)

    rectangle([2,4],[12,8],cookie_clrG)

    rectangle([5,2],[6,1],cookie_clrE)
    rectangle([3,3],[10,1],cookie_clrE)
    rectangle([1,5],[1,1],cookie_clrE)
    rectangle([2,4],[1,1],cookie_clrE)

    rectangle([7,3],[4,1],cookie_clrF)

    rectangle([14,9],[1,2],cookie_clrA)
    rectangle([1,10],[1,1],cookie_clrA)
    rectangle([2,11],[1,1],cookie_clrA)
    rectangle([13,11],[1,1],cookie_clrA)
    rectangle([11,12],[2,1],cookie_clrA)
    rectangle([3,12],[2,1],cookie_clrA)
    rectangle([5,13],[6,1],cookie_clrA)

    rectangle([9,4],[1,1],cookie_clrF)
    rectangle([12,4],[1,2],cookie_clrF)
    rectangle([3,6],[1,1],cookie_clrD)
    rectangle([5,6],[2,1],cookie_clrF)
    rectangle([11,6],[1,1],cookie_clrF)
    rectangle([10,7],[1,2],cookie_clrF)
    rectangle([9,8],[1,1],cookie_clrF)
    rectangle([3,8],[1,1],cookie_clrF)
    rectangle([12,8],[1,1],cookie_clrF)
    rectangle([2,9],[1,1],cookie_clrF)
    rectangle([4,9],[1,1],cookie_clrF)
    rectangle([6,9],[1,1],cookie_clrF)
    rectangle([13,9],[1,1],cookie_clrF)
    rectangle([3,10],[1,1],cookie_clrF)
    rectangle([12,10],[1,1],cookie_clrF)
    rectangle([4,11],[1,1],cookie_clrF)
    rectangle([5,11],[6,1],cookie_clrF)

    rectangle([11,11],[1,1],cookie_clrE)
    rectangle([4,11],[1,1],cookie_clrE)
    rectangle([14,6],[1,3],cookie_clrE)
    rectangle([6,12],[4,1],cookie_clrE)

    rectangle([5,3],[1,1],cookie_clrC)
    rectangle([7,5],[1,1],cookie_clrD)
    rectangle([10,5],[1,1],cookie_clrD)
    rectangle([5,7],[1,1],cookie_clrD)
    rectangle([13,7],[1,1],cookie_clrD)

    rectangle([8,5],[1,2],cookie_clrA)
    rectangle([5,8],[1,1],cookie_clrA)
    rectangle([8,9],[1,1],cookie_clrA)
    rectangle([11,9],[1,1],cookie_clrA)
    rectangle([4,10],[1,1],cookie_clrA)
    rectangle([7,6],[1,1],cookie_clrA)
    rectangle([10,6],[1,1],cookie_clrC)

    rectangle([7,9],[1,1],cookie_clrD)

    rectangle([5,12],[1,1],cookie_clrD)
    rectangle([10,12],[1,1],cookie_clrD)

    rectangle([2,6],[1,1],cookie_clrC)

    rectangle([3,2],[2,1],[0,0,0])
    rectangle([11, 2], [4, 1], [0, 0, 0])
    rectangle([13,3], [2, 1], [0, 0, 0])
    rectangle([13, 4], [1, 1], cookie_clrE)
    rectangle([14,4],[1,1],[0,0,0])

    rectangle([6,3],[1,1],cookie_clrD)


### CALLS ###

rectangle([3,2],[5,6],clr_rectangle)
pyp.imshow(img)
pyp.show()
img = base_img[:]


triangle([3,2],[6,5],clr_triangle)
pyp.imshow(img)
pyp.show()
img = base_img[:]

rectangle_fade([3,2],[12,9],clr_fade,clr_fade_applied)
pyp.imshow(img)
pyp.show()
img = base_img[:]

cookie()
pyp.imshow(img)
pyp.show()
img = base_img[:]
### SHOW ### # useless

#pyp.imshow(imgA)
#print("Showing [imgA]")
#pyp.imshow(imgB)
#print("Showing [imgB]")
#pyp.imshow(imgC)
#print("Showing [imgC]")
#pyp.imshow(imgD)
#print("Showing [imgD]")

pyp.show()
