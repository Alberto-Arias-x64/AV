import cv2
import numpy as np 
img=cv2.imread("euro.jpg")
#img=cv2.resize(img,(800,400))
imgg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2=cv2.imread("euroespejo.jpg",0)
w,h=img2.shape[::-1]

res=cv2.matchTemplate(imgg,img2,cv2.TM_CCORR_NORMED)
th=0.999;
loc=np.where(res>=th)
for pt in zip(*loc[::-1]):
	cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)

cv2.imshow("camion",img)
cv2.waitKey(0)
cv2.destroyAllWindows()