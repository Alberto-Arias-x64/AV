import cv2
import datetime

video=cv2.VideoCapture(0);
#fourcc=cv2.VideoWriter_fourcc(*'XVID')
#out= cv2.VideoWriter('salida.avi',fourcc,60.0,(800,600))
#video.set(3,1000)
#video.set(4,1000)
print(video.get(3))
print(video.get(4))
fuente=cv2.FONT_HERSHEY_SIMPLEX
texto='Width:'+ str(video.get(3))+'Height:'+str(video.get(4))

while(True):
	ret,frame=video.read()
	if ret:
		#out.write(frame)
		hora=str(datetime.datetime.now())
		frame=cv2.putText(frame,hora[0:19],(10,50),fuente,1,(0,255,255),2,cv2.LINE_AA)
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		cv2.imshow('Video XD',gray)
		if cv2.waitKey(1) & 0xFF ==ord('q'):break
	else:break
#out.release()
video.release()
cv2.destroyAllWindows()
