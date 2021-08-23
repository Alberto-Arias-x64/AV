import cv2
import numpy

video=cv2.VideoCapture(0);
#fourcc=cv2.VideoWriter_fourcc(*'XVID')
#out= cv2.VideoWriter('salida.avi',fourcc,60.0,(800,600))

while(True):
	ret,frame=video.read()
	if ret:
		#out.write(frame)
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		cv2.imshow('Video XD',gray)
		if cv2.waitKey(1) & 0xFF ==ord('q'):
			break
	else:
		break
#out.release()
video.release()
cv2.destroyAllWindows()
