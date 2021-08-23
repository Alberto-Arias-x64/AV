import cv2
import numpy as np

imagen=cv2.imread('marcelo.jpg',1)
#imagen=np.zeros([600,800,3], np.uint8)

imagen=cv2.line(imagen,(0,0),(255,255),(255,0,0),5)
imagen=cv2.rectangle(imagen,(255,255),(555,555),(255,0,0),5)
font=cv2.FONT_HERSHEY_SIMPLEX
imagen=cv2.putText(imagen,'opencv',(10,500),font,4,(255,255,0),10,cv2.LINE_AA)
cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()