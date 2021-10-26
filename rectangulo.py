#Paredes Márquez Carlos
#Algoritmo de rectangulo
#20 10 2021

import cv2

im = cv2.imread('gato.jpg')

cv2.rectangle(im, (200,100), (100,300), (0,0,255), 3) #valor final en negativo para rellenar el circulo

cv2.imshow('Image0', im)
cv2.waitKey(0)