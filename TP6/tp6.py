#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @name: tp6.py
# @authors: Gustavo Bruno
#           Jeremias Baez Carballo
#

import cv2
import numpy as np
import os

path = os.path.dirname(os.path.realpath(__file__))
print(path)

mpress = False
pInicial = (-1, -1)
pFinal = (-1, -1)
pSupport = (0, 0)

def seleccion(event, x, y, flags, param):
    global mpress, pInicial, pFinal, pSupport, img, original
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Mouse button pressed")
        mpress = True
        pInicial = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if mpress == True:
            # print("Mouse button dragging")
            if pSupport != (x, y):
                pSupport = x, y
                img = original.copy()
                cv2.rectangle(img, pInicial, pSupport, (0, 0, 0), 1)
                cv2.imshow("Imagen", img)
    elif event == cv2.EVENT_LBUTTONUP:
        print("Mouse button released")
        mpress = False
        pFinal = x, y
        cv2.rectangle(img, pInicial, pFinal, (0, 0, 0), 1)
        cv2.imshow("Imagen", img)

def translacion(imagen, x, y):
    height, width = imagen.shape[0], imagen.shape[1]
    matrix = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(imagen, matrix, (width, height))
    return shifted

def rotacion(imagen, angulo, centro=None, escala=1.0):
    height, width = imagen.shape[0], imagen.shape[1]
    if centro == None:
        centro = height/2, width/2
    matrix = cv2.getRotationMatrix2D(centro, angulo, escala)
    rotated = cv2.warpAffine(imagen, matrix, (width, height))
    return rotated

try:
    img = cv2.imread(path+"/img/carpincherto.jpg", cv2.IMREAD_COLOR)
    original = img.copy()
    cv2.namedWindow("Imagen")
    cv2.setMouseCallback("Imagen", seleccion)
    print("Seleccione un rectangulo en la imagen presionando y arrastrando el mouse.\
         Presione g para guardar, r para volver a la imagen original, e para transformacion euclidiana\
            , s para similaridad y q para salir\n")
    xySize = img.shape
    print("Size: ", xySize)        
    while(True):
        cv2.imshow("Imagen", img)
        key = cv2.waitKey(0) & 0xFF
        if key == ord("g"):
            print("Guardando imagen como resultado.png\n")
            result = img[pInicial[1]:pFinal[1], pInicial[0]:pFinal[0]]
            cv2.imwrite(path+"/img/resultado.png", result)
        elif key == ord("r"):
            print("Restaurando imagen original\n")
            img = original.copy()
        elif key == ord("e"):
            print("Se realizara una transformacion euclidiana de la selección, se guardara como\
                 resultadoe.png\n")
            angulo = float(input("Ingrese el angulo que desea rotar\n"))
            translx = int(input("Ingrese la translacion en x\n"))
            transly = int(input("Ingrese la translacion en y\n"))
            result = img[pInicial[1]:pFinal[1], pInicial[0]:pFinal[0]]
            result = translacion(result, translx, transly)
            # print("translacion correcta")
            result = rotacion(result, angulo)
            cv2.imwrite(path+"/img/resultadoe.png", result)
        elif key == ord("s"):
            print("Se realizara una transformacion de similaridad de la selección, se guardara como\
                 resultadosim.png\n")
            translx = int(input("Ingrese la translacion en x\n"))
            transly = int(input("Ingrese la translacion en y\n"))
            angulo = float(input("Ingrese el angulo que desea rotar\n"))
            escala = float(input("Ingrese la escala que quiere aplicar\n"))
            result = img[pInicial[1]:pFinal[1], pInicial[0]:pFinal[0]]
            result = translacion(result, translx, transly)
            # print("translacion correcta")
            result = rotacion(result, angulo, escala=escala)
            cv2.imwrite(path+"/img/resultadosim.png", result)
        elif key == ord("q"):
            print("Saliendo del programa...\n")
            break
    cv2.destroyAllWindows()
except Exception as e:
    print("Excepcion ejecutando el programa: %s", e)
    cv2.destroyAllWindows()