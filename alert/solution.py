from PIL import Image
from numpy import *


im = array(Image.open("alert.png"))

a, b, c = im.shape

for x in range(0, a):
    for y in range(0, b):
        print(im[x,y])
