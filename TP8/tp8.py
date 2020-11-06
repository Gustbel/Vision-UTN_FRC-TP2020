#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @name: tp7.py
# @authors: Gustavo Bruno
#           Jeremias Baez Carballo
#

import cv2
import numpy as np
import os

path = os.path.dirname(os.path.realpath(__file__))
print(path)

p1, p2, p3, p4 = (-1,-1), (-1,-1), (-1,-1), (-1,-1)
cPoint = 1

def seleccionPuntos(event, x, y, flags, param):
    global cPoint, p1, p2, p3, p4, img
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Mouse button pressed")
        if cPoint == 1:
            p1 = x, y
            cv2.circle(img, p1, 3, (255, 0, 0), 2)
        elif cPoint == 2:
            p2 = x, y
            cv2.circle(img, p2, 3, (0, 255, 0), 2)
        elif cPoint == 3:
            p3 = x, y
            cv2.circle(img, p3, 3, (0, 0, 255), 2)
        elif cPoint == 4:
            p4 = x, y
            cv2.circle(img, p4, 3, (0, 255, 255), 2)
        cPoint += 1
        cv2.imshow("imagen", img)

def homografia(imagen, height, width):
    height, width = imagen.shape[0], imagen.shape[1]
    source = np.array([p1, p2, p4, p3], dtype=np.float32) # Inverted point to respect transformation order
    dest = np.array([[0, 0], [width, 0], [0 , height], [width, height]], dtype=np.float32)
    matrix = cv2.getPerspectiveTransform(source, dest)
    result = cv2.warpPerspective(imagen, matrix,(width, height))
    return result

try:
    img = cv2.imread(path+"/img/input.jpg", cv2.IMREAD_COLOR)
    original = img.copy()
    cv2.namedWindow("imagen")
    cv2.setMouseCallback("imagen", seleccionPuntos)
    print("Seleccione 4 puntos en orden de sentido horario de la siguiente manera: \n p1---p2\n |     \
        |\n p4---p3\nPara realizar la homografia presione h, para volver a seleccionar los puntos\
         presione r, para salir q")
    xySize = img.shape
    print("Size: ", xySize)
    while(True):
        cv2.imshow("imagen", img)
        # cv2.imshow("imagen2", img2)
        key = cv2.waitKey(0) & 0xFF
        if key == ord("h"):
            w = int(input("Ingrese el ancho de la imagen rectangular de salida deseado:\n"))
            h = int(input("Ingrese el alto de la imagen rectangular de salida deseado:\n"))
            print("Guardando el resultado de la imagen en salida.png")
            salida = homografia(original, h, w)
            cv2.imwrite(path+"/img/salida.png", salida)
            cv2.namedWindow("salida")
            cv2.imshow("salida", salida)
        elif key == ord("r"):
            print("Restaurando imagen, habilitando nueva seleccion")
            img = original.copy()
            cPoint = 1
            p1, p2, p3, p4 = (-1,-1), (-1,-1), (-1,-1), (-1,-1)
            cv2.destroyWindow("salida")
        elif key == ord("q"):
            print("Saliendo del programa...\n")
            break
    cv2.destroyAllWindows()
except Exception as e:
    print("Excepcion ejecutando el programa: %s", e)
    cv2.destroyAllWindows()