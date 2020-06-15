#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import pathlib
import os

path = os.path.dirname(os.path.realpath(__file__))
print(path)

mpress = False
ix, iy = 1, 1
fx, fy = 1, 1

def seleccion(event, x, y, flags, param):
    global mpress, mode, ix, iy, fx, fy
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Mouse button pressed")
        mpress = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if mpress == True:
            pass
            # print("Mouse button dragging")
            # cv2.rectangle(img, (ix,iy), (x,y), (0, 0, 0), 2)
            # cv2.imshow("Imagen", img)
    elif event == cv2.EVENT_LBUTTONUP:
        print("Mouse button released")
        mpress = False
        fx, fy = x, y
        cv2.rectangle(img, (ix,iy), (fx,fy), (0, 0, 0), 2)
        cv2.imshow("Imagen", img)

try:
    img = cv2.imread(path+"/imgs/simpsons.jpeg", cv2.IMREAD_COLOR)
    cv2.namedWindow("Imagen")
    cv2.setMouseCallback("Imagen", seleccion)
    print("Seleccione un rectangulo en la imagen presionando y arrastrando el mouse.\
         Presione g para guardar, r para volver a la imagen original y q para salir\n")
    xySize = img.shape
    print("Size: ", xySize)        
    while(True):
        cv2.imshow("Imagen", img)
        key = cv2.waitKey(0) & 0xFF
        if key == ord("g"):
            print("Guardando imagen como salidaSeleccion.png\n")
        elif key == ord("r"):
            print("Restaurando imagen original\n")
        elif key == ord("q"):
            print("Saliendo del programa...\n")
            break
    cv2.destroyAllWindows()
except Exception as e:
    print("Excepcion ejecutando el programa: %s", e)
    cv2.destroyAllWindows()
    
