import cv2
import numpy as np 
#import matplotlib.pylab as plt

region=[(275,270),(400,100),(580,270)]

def region_de_interes(img,vertices):
	mascara=np.zeros_like(img)
	#canal=img.shape[2]
	match=(255,)#*canal
	cv2.fillPoly(mascara,vertices,match)
	enmascarado=cv2.bitwise_and(img,mascara)
	return enmascarado

img=cv2.imread("euro.jpg")
imgc=cv2.resize(img,(800,400))
img=cv2.cvtColor(imgc,cv2.COLOR_BGR2GRAY)
blur=cv2.blur(img,(3,3))
edges=cv2.Canny(blur,80,150,apertureSize=3)
img=region_de_interes(edges,np.array([region],np.int32))
#cv2.imshow("imagen",edges)

lineas=cv2.HoughLinesP(img,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for line in lineas:
    x1,y1,x2,y2 = line[0]
    cv2.line(imgc,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow('image', imgc)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
