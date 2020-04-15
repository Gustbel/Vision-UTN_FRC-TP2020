path='/media/gustavo/DATOS/Facu/6to/Vision/Practicos/Practico2'

import cv2
img = cv2.imread(path + '/leon.png', 0)    

for i in img:
    for j in i:
        if j<230:
            j=0
        else:
            j=255


cv2.imwrite(path + '/resultado.png' , img)

