import cv2 as cv
import numpy as np

img=cv.imread("colores.jpg")
img=cv.resize(img,(400,300))
imgray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
vacio = np.zeros((300,400,3), np.uint8)


antythresh,thresh=cv.threshold(imgray,130,255,0)
edges = cv.Canny(img,130,250)
contours,hierarchy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

print(str(len(contours)))
#print(str(antythresh))

cv.drawContours(vacio,contours,-1,(0,255,0),1)

cv.imshow("normal",img)
cv.imshow("blanco y negro",thresh)
cv.imshow("canny",edges)
cv.imshow("deges",vacio)
cv.waitKey(0)
cv.destroyAllWindows()