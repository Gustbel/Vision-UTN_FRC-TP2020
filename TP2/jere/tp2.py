#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @name: tp2.py
# @authors: Jeremias Baez Carballo
#           Gustavo Bruno
#

import cv2
import numpy as np

img = cv2.imread("hojas-sobre-blanco.png", 0)

alto,ancho = img.shape
result = np.zeros(img.shape)

try : 
    print(img.shape)
    print(type(img[1][1]))
    print(img.item(1,1))
    print(type(img))
    print(type(result))
    while True:
        print("Ingrese el umbral que desea aplicar a la imagen para generar la silueta: ")
        thr = int(input())
        for row in range(alto):
            for col in range(ancho):
                if img.item(row,col) > thr: 
                    result[row][col] = 255
                else:
                    result[row][col] = 0
        cv2.imwrite("resultado.png", result)
        print("Imagen resultado generada! Presione Ctrl+c para salir o vuelva a ingresar otro umbral")
except KeyboardInterrupt:
    print("\nSaliendo del programa!")
