import cv2 as cv
import numpy as np
from matplotlib import pyplot as plot

img = cv.imread('euro.jpg')
img = cv.resize(img,(600,300))

img2 = img[125:220,200:440]
hsv=cv.cvtColor(img2,cv.COLOR_BGR2HSV)
#hsv = cv.GaussianBlur(hsv, (5,5), 0)
u_b=np.array([250,50,255])#[103 255  76]
l_b=np.array([80,0,50])#[104 252 100]
mask=cv.inRange(hsv,l_b,u_b)
res=cv.bitwise_and(img2,img2,mask=mask)
"""
kernal=np.ones((2,2), np.uint8)
dilatacion = cv.dilate(mascara,kernal,iterations=1)

titulos=["Original","Separado","dilatado"]
imgs=[img,mascara,dilatacion]

for i in range(2):
	plot.subplot(2,1,i+1),plot.imshow(imgs[i],"gray")
	plot.title(titulos[i])
	plot.xticks([]),plot.yticks([])
plot.show()
"""
cv.imshow("origen",img)
cv.imshow("trabajado",res)

cv.waitKey(0)
cv.destroyAllWindows()