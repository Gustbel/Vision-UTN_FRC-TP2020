import cv2
import numpy as np

path='/media/gustavo/DATOS/Facu/6to/Vision/Practicos/Practico4'

drawing = False # true if mouse is pressed

ix = -1
iy = -1
fx = 0
fy = 0
entro = False

def draw_rectangle (event, x, y, flags, param):
    global ix, iy, fx, fy, drawing, entro
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix , iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True :
            cv2.rectangle(img, (ix,iy), (x ,y) , (0, 255, 0), 1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix,iy), (x,y), (0 , 255 , 0), -1)
        fx, fy = x, y
        entro = True
    

img = cv2.imread(path + '/leon.png')    
img_orig = cv2.imread(path + '/leon.png')  #Cargamos dos veces porque la variable img se modificará

cv2.namedWindow ( ' image ' )
cv2.setMouseCallback(' image ', draw_rectangle)


while ( 1 ):           # Sostiene la imagen 
    cv2.imshow( ' image ' , img )
    if entro == True:
        img = img_orig[iy: fy, ix: fx]    # Corta la imagen
        
    k = cv2.waitKey ( 1 ) &0xFF
    if k == ord( 'q' ) :
        mode = not mode         #Finaliza
    if k == ord( 'g' ) :
        cv2.imwrite(path + '/resultado.png' , img)
    if k == ord( 'r' ) :
        img=cv2.imread(path + '/leon.png')   
        entro = False
    
cv2.destroyAllWindows()