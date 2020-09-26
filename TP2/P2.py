# -*- coding: utf-8 -*-

# En el string 'path' se debe poner la dirección absoluta del directorio donde se encuentran los archivos
# porque no pude hacer que "cv2.imread" lea la dirección relativa. 

import os
import cv2

path = os.path.dirname(os.path.realpath(__file__))

img = cv2.imread( path + '/leon.png', 0)  

a, b = img.shape

for i in range(0,a):
    for j in range(0,b):
        if img[i][j]<100:
            img[i][j]=0
        else:
            img[i][j]=255

cv2.imwrite(path + '/resultado.png' , img)

