import cv2 as cv
import numpy as np

img=cv.imread("marcelo.jpg",0)
img=cv.resize(img,(400,300))

kernel=np.ones((3,3),np.float32)/9
dts=cv.filter2D(img,-1,kernel)
blur=cv.blur(img,(3,3))
gblur=cv.GaussianBlur(img,(3,3),0)
median=cv.medianBlur(img,9)
bl=cv.bilateralFilter(img,9,75,75)

img=cv.imshow("imagen",img)
img=cv.imshow("distorcion",dts)	#desenfoque	
img=cv.imshow("blur",blur)    	#ruido simple
img=cv.imshow("gausst",gblur) 	#ruido de alta frecuencia
img=cv.imshow("mediana",median)	#filro sal y pimienta
img=cv.imshow("bilateral",bl)	#filro sal y pimienta

cv.waitKey(0)
cv.destroyAllWindows()