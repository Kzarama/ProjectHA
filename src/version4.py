from PIL import Image
from time import time

img = Image.open('img/4-32.bmp')
image = img.load()

len_x, len_y = img.size

start_time = time()

"""
    Los algoritmos toman el valor de y para las filas y x para las columnas.
    Esto es porque a la hora de convertir los bits en una lista de lista (simil de matrices en python)
    para poder recorrer correctamente como los algoritmos de los lineamos toca invertir las variables.
    En pocas palabra en estos algoritmos y (algoritmo) es igual a x (lineamientos)
    y X (algoritmo) es igual a y (lineamientos)
"""

for y in range(len_y):
    for x in range(len_x):
        image[x,y] = (255-image[x,y][0], image[x,y][1], image[x,y][2])

for y in range(len_y):
    for x in range(len_x):
        image[x,y] = (image[x,y][0], 255-image[x,y][1], image[x,y][2])
        image[x,y] = (image[x,y][0], image[x,y][1], 255-image[x,y][2])

elapsed_time = time() - start_time

# img.show()
import pyperclip; pyperclip.copy("{:.5f}".format(elapsed_time)) # copy at the clipboard