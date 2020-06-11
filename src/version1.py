from PIL import Image
from time import time
import numpy as np

img = Image.open('img/1-16.bmp') # open image
data = img.load()

len_x, len_y = img.size # take the size of the image
start_time = time() # start the time
# algorithm 1 for change the image

for y in range(len_y):
    """
    Los algoritmos toman el valor de y para las filas y x para las columnas.
    Esto es porque a la hora de convertir los bits en una lista de lista (simil de matrices en python)
    para poder recorrer correctamente como los algoritmos de los lineamos toca invertir las variables.
    En pocas palabra en estos algoritmos y (algoritmo) es igual a x (lineamientos)
    y X (algoritmo) es igual a y (lineamientos)
    """
    for x in range(len_x):
        data[x,y] = (255-data[x,y][0], data[x,y][1], data[x,y][2])
        data[x,y] = (data[x,y][0], 255-data[x,y][1], data[x,y][2])
        data[x,y] = (data[x,y][0], data[x,y][1], 255-data[x,y][2])

elapsed_time = time() - start_time # time finished the algorithm

import pyperclip; pyperclip.copy("{:.5f}".format(elapsed_time)) # copy at the clipboard
