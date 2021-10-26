#Función delimitador

import cv2


def deli(im):
    
    ig = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    cnts, h = cv2.findContours(ig, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        x,y,w,h = cv2.boundingRect(c) #x,y, largo, alto

        cv2.rectangle(im, (x,y), (x+w,y+h), (0,0,255), 1) #superior izquierda, inferior derecha