import cv2
import numpy as np

def evento2(eve,x,y,bandera,parametro):
	if eve==cv2.EVENT_LBUTTONDOWN:
		print(x,",",y)
		fuente=cv2.FONT_HERSHEY_SIMPLEX
		strxy=str(x)+','+str(y)
		#metodo     imagen,texto,posicion,fuente,tamaño,color,grosor
		cv2.putText(img,strxy,(x,y),fuente,0.8,(255,255,0),2)
		cv2.imshow('imagen',img)

	if eve==cv2.EVENT_RBUTTONDOWN:
		azul=img[y,x,0]
		verde=img[y,x,1]
		rojo=img[y,x,2]
		fuente=cv2.FONT_HERSHEY_SIMPLEX
		strxy=str(azul)+','+str(verde)+','+str(rojo)
		cv2.putText(img,strxy,(x,y),fuente,0.8,(0,255,255),2)
		hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		print(hsv[y][x])
		cv2.imshow('imagen',img)

#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread('euro.jpg')
img=cv2.resize(img,(600,300))
cv2.imshow('imagen',img)
cv2.setMouseCallback('imagen',evento2)
cv2.waitKey(0)
cv2.destroyAllWindows()