import cv2
import numpy

video=cv2.VideoCapture(0);
print(video.get(cv2.CAP_PROP_FRAME_WIDTH))
print(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(video.get(cv2.CAP_PROP_FPS))
while(True):
	ret,frame=video.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	nots=cv2.bitwise_not(frame)
	cv2.imshow('Video XD',nots)
	cv2.imshow('Video 2',frame)
	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break
video.release()
cv2.destroyAllWindows()