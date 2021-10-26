#Función contorno

import cv2

def cont(im):

    ig = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    cnts, h= cv2.findContours(ig, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(im, cnts, -1, (0, 255, 0), 3)
