#Paredes Márquez Carlos
#Algoritmo de circulos
#20 10 2021

import cv2

im = cv2.imread('tenis.jpg')

cv2.circle(im, (400,320), 200, (0,0,255), 3)

cv2.imshow('Image0', im)
cv2.waitKey(0)