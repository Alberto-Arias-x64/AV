import cv2
import numpy as np
"""
video=cv2.VideoCapture(0);
ret,img=video.read()
video.release()
"""
def evento2(eve,x,y,bandera,parametro):
	if eve==cv2.EVENT_LBUTTONDOWN:
		azul=img[y,x,0]
		verde=img[y,x,1]
		rojo=img[y,x,2]
		hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		print("Color BGR: [",azul,verde,rojo,"]")
		print("Color HSV:",hsv[y][x])

#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread('euro.jpg')
img=cv2.resize(img,(600,300))
cv2.imshow('imagen',img)
cv2.setMouseCallback('imagen',evento2)
cv2.waitKey(0)
cv2.destroyAllWindows()