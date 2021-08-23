import cv2
import numpy as np 

img=cv2.imread("formas.jpg",0)
img=cv2.GaussianBlur(img,(3,3),0)
_,th=cv2.threshold(img,200,255,cv2.THRESH_BINARY)
contornos,_=cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for contornos in contornos:
	aprox=cv2.approxPolyDP(contornos,0.01*cv2.arcLength(contornos,True),True)
	cv2.drawContours(img,[aprox],-1,(0,0,0),2)
	x=aprox.ravel()[0]
	y=aprox.ravel()[1]

	if len(aprox)==3: cv2.putText(img,"Triangulo",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
	elif len(aprox)==4: cv2.putText(img,"Cuadrado",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
	#elif aspectRatio >= 0.95 and aspectRatio <= 1.05:cv2.putText(img, "circulo", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
	elif len(aprox) == 5: cv2.putText(img, "Pentagono", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
	elif len(aprox) == 10: cv2.putText(img, "Estrella", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
	else :cv2.putText(img, "Circulo", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

cv2.imshow("XD",img)
cv2.waitKey(0)
cv2.destroyAllWindows()