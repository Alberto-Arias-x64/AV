import cv2
import numpy as np

def nada():
	pass

video=cv2.VideoCapture(0);

while True:
	#fr=cv2.imread("colores.jpg")
	ret,fr=video.read()
	fr=cv2.resize(fr,(400,300))

	hsv=cv2.cvtColor(fr,cv2.COLOR_BGR2HSV)
	hsv = cv2.GaussianBlur(hsv, (5,5), 0)
	l_b=np.array([100,90,55])#[103 255  76]
	u_b=np.array([120,255,140])#[104 252 100]
	mask=cv2.inRange(hsv,l_b,u_b)
	res=cv2.bitwise_and(fr,fr,mask=mask)
	
	cv2.imshow("imagen",fr)
	cv2.imshow("mascara",mask)
	cv2.imshow("resultado",res)

	tecla=cv2.waitKey(1)
	if tecla==27:break
cv2.destroyAllWindows()