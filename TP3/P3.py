# Se puso otro color de conversion porque Blanco y Negro da error en el archivo resultado output.avi

# En el string 'path' se debe poner la dirección absoluta del directorio donde se encuentran los archivos
# porque no pude hacer que "cv2.imread" lea la dirección relativa. 

path='/media/gustavo/DATOS/Facu/6to/Vision/Practicos/Practico3'

import sys
import cv2

cap = cv2.VideoCapture(path + "/original.avi")

fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # float
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # float
framesize = ( w , h )
#framesize = ( 640 , 480 )

delay = int(cap.get(cv2.CAP_PROP_FPS))    # Esta función obtiene el framerate original en type Float, lo convertimos a Integer
#delay = 33

out = cv2.VideoWriter(path + "/output.avi" , fourcc , delay , framesize )

cv2.VideoWriter()


while (cap.isOpened()):
    ret , frame = cap.read()

    if ret is True:
        #gray = cv2.cvtColor (frame , cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor (frame , cv2.COLOR_RGB2BGR) # Se puso este porque ByN da error en el archivo resultado output.avi
        out.write(gray)
        cv2.imshow('Image gray' , gray)
        if cv2.waitKey(delay) & 0xFF == ord ('q') :
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
