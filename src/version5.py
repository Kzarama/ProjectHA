from PIL import Image
from time import time

img = Image.open('img/1.png')
image = img.load()

len_x, len_y = img.size

start_time = time()

for y in range(0, len_y, 2):
    for x in range(0, len_x, 2):
        image[x,y] = (255-image[x,y][0], image[x,y][1], image[x,y][2], image[x,y][3])
        image[x,y] = (image[x,y][0], 255-image[x,y][1], image[x,y][2], image[x,y][3])
        image[x,y] = (image[x,y][0], image[x,y][1], 255-image[x,y][2], image[x,y][3])

        image[x+1,y] = (255-image[x+1,y][0], image[x+1,y][1], image[x+1,y][2], image[x+1,y][3])
        image[x+1,y] = (image[x+1,y][0], 255-image[x+1,y][1], image[x+1,y][2], image[x+1,y][3])
        image[x+1,y] = (image[x+1,y][0], image[x+1,y][1], 255-image[x+1,y][2], image[x+1,y][3])

        image[x,y+1] = (255-image[x,y+1][0], image[x,y+1][1], image[x,y+1][2], image[x,y+1][3])
        image[x,y+1] = (image[x,y+1][0], 255-image[x,y+1][1], image[x,y+1][2], image[x,y+1][3])
        image[x,y+1] = (image[x,y+1][0], image[x,y+1][1], 255-image[x,y+1][2], image[x,y+1][3])

        image[x+1,y+1] = (255-image[x+1,y+1][0], image[x+1,y+1][1], image[x+1,y+1][2], image[x+1,y+1][3])
        image[x+1,y+1] = (image[x+1,y+1][0], 255-image[x+1,y+1][1], image[x+1,y+1][2], image[x+1,y+1][3])
        image[x+1,y+1] = (image[x+1,y+1][0], image[x+1,y+1][1], 255-image[x+1,y+1][2], image[x+1,y+1][3])

elapsed_time = time() - start_time

# img.show()
import pyperclip; pyperclip.copy("{:.5f}".format(elapsed_time)) # copy at the clipboard