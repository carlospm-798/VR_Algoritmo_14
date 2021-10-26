#Paredes Márquez Carlos
#Algoritmo 14
#20 10 2021

import cv2
import numpy as np
import Rand
import contorno
import delimitador

print('\nBienvenido al algoritmo 14.\n\n\n')

res: str = True

while(res == True):

    semilla = 0

    print('Escoja una cantidad de cuadrados:')
    cant1: int = int(input(':    '))
    print('\nEscoja una cantidad de circulos:')
    cant2: int = int(input(':    '))

    im = np.zeros((480,720,3), dtype= np.uint8) #480c * 720f y 3 canales

    im = Rand.rrand(im, cant1, semilla)
    im = Rand.crand(im, cant2, semilla)

    print('Ver el contorno:    [Si / si]')
    respc: str = str(input(':    '))

    if(respc == 'si' or respc == 'Si'):
        contorno.cont(im)
    
    print('Ver el delimitador:    [Si / si]')
    respd: str = str(input(':    '))

    sum = cant1 + cant2

    c: int = 0

    while(c < sum):

        if(respd == 'si' or respd == 'Si'):
            delimitador.deli(im)
        
        c += 1

    cv2.imshow('Image0', im)
    cv2.waitKey(0)

    print('\n\n\nvolver a repetir programa:    [si / Si]')
    print('caso contrario, presione cualquier tecla:\n\n\n')
    res = str(input(':    '))

    if(res == 'Si' or res == 'si'):
        res = True
    else:
        break