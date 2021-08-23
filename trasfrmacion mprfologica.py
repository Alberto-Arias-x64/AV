import cv2 as cv
import numpy as np
from matplotlib import pyplot as plot

img = cv.imread('euro.jpg',0)
img = cv.resize(img,(800,400))
img = cv.GaussianBlur(img,(5,5),1)

mascara = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 2);
kernel=np.ones((2,2), np.uint8)
closing = cv.morphologyEx(mascara, cv.MORPH_CLOSE, kernel)
dilation = cv.dilate(closing,kernel,iterations = 1)
#erosion = cv.erode(dilation,kernel,iterations = 1)
canny = cv.Canny(img, 50, 150)
canny = cv.bitwise_not(canny)


titulos=["Original","Thresch","Procesado","bordes"]
imgs=[img,mascara,dilation,canny]

for i in range(4):
	plot.subplot(2,2,i+1),plot.imshow(imgs[i],"gray")
	plot.title(titulos[i])
	plot.xticks([]),plot.yticks([])
plot.show()
#cv.imshow("caca",kernal)
cv.waitKey(0)
cv.destroyAllWindows()