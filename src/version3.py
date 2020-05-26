from PIL import Image
from time import time

img = Image.open('img/1.png')
image = img.load()

len_x, len_y = img.size

start_time = time()

for x in range(len_x):
    for y in range(len_y):
        image[x,y] = (255-image[x,y][0], image[x,y][1], image[x,y][2], image[x,y][3])
        image[x,y] = (image[x,y][0], 255-image[x,y][1], image[x,y][2], image[x,y][3])
        image[x,y] = (image[x,y][0], image[x,y][1], 255-image[x,y][2], image[x,y][3])

elapsed_time = time() - start_time

# img.show()
import pyperclip; pyperclip.copy("{:.5f}".format(elapsed_time)) # copy at the clipboard