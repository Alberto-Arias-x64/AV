import cv2
import numpy as np 

cap=cv2.VideoCapture(0)
ret,frame1=cap.read()
ret,frame2=cap.read()

while cap.isOpened():

	dif=cv2.absdiff(frame1,frame2)

	g=cv2.cvtColor(dif,cv2.COLOR_BGR2GRAY)
	blur=cv2.GaussianBlur(g,(3,3),0)
	_,th=cv2.threshold(blur,50,255,cv2.THRESH_BINARY)
	d=cv2.dilate(th,None,iterations=3)
	contornos,_=cv2.findContours(d,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	#cv2.imshow("caca",th)#control

	for contornos in contornos:
		(x,y,w,h)=cv2.boundingRect(contornos)
		if cv2.contourArea(contornos)<1000:
			continue
		cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
		cv2.putText(frame1,"Estado: Movimiento",(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
	cv2.imshow("video",frame1)
	frame1=frame2
	ret,frame2=cap.read()
	if cv2.waitKey(1) == 27:break
cap.release()
cv2.destroyAllWindows()