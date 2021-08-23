import cv2 as cv
import numpy as np 

img=cv.imread("euro.jpg",0)
img=cv.resize(img,(600,300))
layer=img.copy()
gp=[layer]

#lr2=cv.pyrUp(img)
lr=cv.pyrDown(img)
for i in range(3):
	layer=cv.pyrDown(layer)
	gp.append(layer)

cv.imshow("imagen",layer)

cv.waitKey(0)
cv.destroyAllWindows()