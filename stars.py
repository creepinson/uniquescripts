# Made by Creepinson
# Requirements:
# python3, pillow, numpy, and matplotlib.
# Enjoy!


import cv2
import time
from PIL import Image
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


def load_image(infilename):
    img = Image.open(infilename)
    img.load()
    data = np.asarray(img, dtype="int32")
    return data


img = load_image("sky.jpg")
img.resize([128, 256])
#img = np.random.rand(512, 512)
color = -512

fig = plt.figure()
im = plt.imshow(img, animated = True)


def update_fig(*args):
    global color
    for index, x in np.ndenumerate(img):
        img[index] = x * math.ceil(math.sin(x*color)) - math.tan(x)
    color+=5;
    im.set_data(img)
    return im


ani = animation.FuncAnimation(fig, update_fig, interval = 60)

plt.show()
