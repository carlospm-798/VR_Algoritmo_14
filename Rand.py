#función random

from random import seed
from random import randint as rand
import cv2


'''Función de rectángulos'''
#función de rectangulos random
def rrand(im, cantidad, semilla):

    cont: int = 0

    while(cont < cantidad):

        ob = rand(0,720)
        ob2 = rand(0, 480)
        ob3 = rand(0,720)
        ob4 = rand(0, 480)

        cv2.rectangle(im, (ob, ob2), (ob3, ob4), (255,255,255), -1)
        cont += 1

    semilla += 1

    return im

'''Función de circulos'''
#función de circulos random
def crand(im, cantidad, semilla):
    
    cont: int = 0

    while(cont < cantidad):

        rad = rand(2, 20)
        x = rand(0, 720)
        y = rand(0, 480)

        cv2.circle(im, (x,y), rad, (255,255,255), -1) #centro, radio, color, grosor
        cont += 1
    semilla += 2

    return im