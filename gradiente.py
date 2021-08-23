import cv2 as cv
import numpy as np 

img=cv.imread("euro.jpg",0)
img=cv.resize(img,(400,300))

lap=cv.Laplacian(img,cv.CV_64F,ksize=1)
lap=np.uint8(np.absolute(lap))
edges = cv.Canny(img,50,250)
sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=3)
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=3)
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))
sobelultra = cv.bitwise_or(sobelx,sobely)

cv.imshow("imagen",img)
cv.imshow("laplace",lap)
cv.imshow("x",sobelx)
cv.imshow("y",sobely)
cv.imshow("Canny",edges)
cv.imshow("x+y",sobelultra)

cv.waitKey(0)
cv.destroyAllWindows()