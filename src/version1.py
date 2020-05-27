from PIL import Image
from time import time
import numpy as np

img = Image.open('img/1-16.bmp') # open image
data = img.load()

len_x, len_y = img.size # take the size of the image
start_time = time() # start the time
# algorithm 1 for change the image
for y in range(len_y):
    for x in range(len_x):
        data[x,y] = (255-data[x,y][0], data[x,y][1], data[x,y][2]) # r
        data[x,y] = (data[x,y][0], 255-data[x,y][1], data[x,y][2]) # g
        data[x,y] = (data[x,y][0], data[x,y][1], 255-data[x,y][2]) # b

elapsed_time = time() - start_time # time finished the algorithm

import pyperclip; pyperclip.copy("{:.5f}".format(elapsed_time)) # copy at the clipboard

# img.show() # show the image
# ima = Image.fromarray(data)
# ima.show()

# import matplotlib.pyplot as plt;plt.imshow(data);plt.show()


# from PIL import Image
# from time import time

# # img = Image.open('img/1-8.png') # open image
# img = Image.open('img/4-32.png') # open image
# image = img.load() # load image
# len_x, len_y = img.size # take the size of the image
# start_time = time() # start the time
# # algorithm 1 for change the image
# for y in range(len_y):
#     for x in range(len_x):
#         image[x,y] = (255-image[x,y][0], image[x,y][1], image[x,y][2], image[x,y][3]) # r
#         image[x,y] = (image[x,y][0], 255-image[x,y][1], image[x,y][2], image[x,y][3]) # g
#         image[x,y] = (image[x,y][0], image[x,y][1], 255-image[x,y][2], image[x,y][3]) # b

# elapsed_time = time() - start_time # time finished the algorithm
# # img.show() # show the image
# import pyperclip; pyperclip.copy("{:.5f}".format(elapsed_time)) # copy at the clipboard

