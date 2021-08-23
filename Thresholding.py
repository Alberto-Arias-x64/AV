import cv2 as cv
import numpy as np
from matplotlib import pyplot as plot

img = cv.imread('marcelo.jpg')
img = cv.resize(img,(400,300))
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
_, th1 = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 100, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 100, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 100, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 100, 255, cv.THRESH_TOZERO_INV)
th6 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2);
th7 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2);
"""
cv.imshow("Image", img)
cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)
cv.imshow("th4", th4)
cv.imshow("th5", th5)
cv.imshow("th6", th6)
cv.imshow("th7", th7)
"""
titulos=["original","binario","inv binario","trunc","tozero","inv tozero","adaptativo","gasust adaptativo"]
imgs=[img,th1,th2,th3,th4,th5,th6,th7]

for i in range(8):
	plot.subplot(3,3,i+1),plot.imshow(imgs[i],"gray")
	plot.title(titulos[i])
	plot.xticks([]),plot.yticks([])
plot.show()

cv.waitKey(0)
cv.destroyAllWindows()