import cv2
import numpy as np

img=cv2.imread('marcelo.jpg')
img=cv2.resize(img,(400,300))
print(img.shape)
print(img.size)
print(img.dtype)

cara=img[79:154,140:249]#[154:79,249:140]
cv2.imshow('face',cara)
cara=cv2.resize(cara,(400,300))

salida1=cv2.add(img,cara)
cv2.imshow('imagenxd',salida1)

salida=cv2.addWeighted(img,0.3,cara,0.7,0)
cv2.imshow('imagenover',salida)

ands=cv2.bitwise_and(img,cara)
cv2.imshow('imagen',ands)

ors=cv2.bitwise_or(img,cara)
cv2.imshow('imagen2',ors)

nots=cv2.bitwise_not(img)
cv2.imshow('imagen3',nots)

xors=cv2.bitwise_xor(img,cara)
cv2.imshow('imagen4',xors)

cv2.waitKey(0)
cv2.destroyAllWindows()