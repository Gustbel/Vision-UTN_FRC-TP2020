#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import cv2
import numpy as np
import math 
import os

path = os.path.dirname(os.path.realpath(__file__))
print(path)


drawing = False # true if mouse is pressed

ix = -1
iy = -1
fx = 0
fy = 0

img = cv2.imread( path + '/leon.png')  

print("Se aplicará una Transformación Euclidiana.")
angle = int(input("Ingrese el ángulo:"))
tx = int(input("Ingrese Traslaxion X (en píxeles):"))
ty = int(input("Ingrese Traslaxion Y (en píxeles):"))



def trans_euclidiana(a, x, y, im):
    (h , w) = (im.shape[0], im.shape[1])
    #Rotación
    center = (w/2 , h/2)
    M = cv2.getRotationMatrix2D(center, a, 1)
    rotated = cv2.warpAffine(im, M, (w, h))
    #Traslación
    M = np.float32([[1,0,x],[0, 1,y]])
    i = cv2.warpAffine(rotated, M, (w,h))
    return i


def draw_rectangle (event, x, y, flags, param):
    global ix, iy, fx, fy, drawing, imagen
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix , iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True :
            imagen = img.copy()
            cv2.rectangle(imagen, (ix,iy), (x ,y) , (0,0,0), 1)
            cv2.imshow( ' image ' , imagen )
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        imagen = img.copy()
        cv2.rectangle(imagen, (ix,iy), (x,y), (0,0,0), -1)
        fx, fy = x, y
        imagen = img[iy: fy, ix: fx]
        cv2.imshow(' image ', imagen )
        print("Presione e para hacer la transformación, guardar y salir")




dst = trans_euclidiana(angle, tx, ty, img) # Acá ejecutamos la función Euclidiana que transforma la imagen completa del punto A  
cv2.imwrite(path + '/resultado_a.png' , dst)


cv2.imshow(' image ', img )
cv2.setMouseCallback(' image ', draw_rectangle)


while ( 1 ):           # Sostiene la imagen
    k = cv2.waitKey ( 1 ) &0xFF

    if k == ord( 'e' ) :
        dst = trans_euclidiana(angle, tx, ty, imagen)# Acá ejecutamos la función Euclidiana que transforma   
        cv2.imwrite(path + '/resultado_b.png' , dst)
        break
    
cv2.destroyAllWindows()