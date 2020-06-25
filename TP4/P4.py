#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import cv2
import numpy as np
import os

path = os.path.dirname(os.path.realpath(__file__))
print(path)


drawing = False # true if mouse is pressed

ix = -1
iy = -1
fx = 0
fy = 0

img = cv2.imread( path + '/leon.png')  
img_orig = cv2.imread(path + '/leon.png')  #Cargamos dos veces porque la variable img se modificará

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
        cv2.imshow( ' image ' , imagen )

cv2.imshow( ' image ' , img )

cv2.namedWindow ( ' image ' )
cv2.setMouseCallback(' image ', draw_rectangle)

while ( 1 ):           # Sostiene la imagen 
    k = cv2.waitKey ( 1 ) &0xFF

    if k == ord( 'g' ) :
        cv2.imwrite(path + '/resultado.png' , imagen)
        print ("Guardado!")
    if k == ord( 'r' ) :
        img=cv2.imread(path + '/leon.png')   
        cv2.imshow( ' image ' , img )
        print ("Imagen Restaurada")
    if k == ord( 'q' ) :
        break        #Finaliza
    
cv2.destroyAllWindows()