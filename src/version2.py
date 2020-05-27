from PIL import Image
from time import time
import numpy as np

img = Image.open('img/4-32.bmp')
image = img.load()

len_x, len_y = img.size

start_time = time()

for y in range(len_y):
    for x in range(len_x):
        image[x,y] = (255-image[x,y][0], image[x,y][1], image[x,y][2])

for y in range(len_y):
    for x in range(len_x):
        image[x,y] = (image[x,y][0], 255-image[x,y][1], image[x,y][2])

for y in range(len_y):
    for x in range(len_x):
        image[x,y] = (image[x,y][0], image[x,y][1], 255-image[x,y][2])

elapsed_time = time() - start_time
# img.show()
import pyperclip; pyperclip.copy("{:.5f}".format(elapsed_time)) # copy at the clipboard