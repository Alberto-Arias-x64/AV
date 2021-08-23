import cv2

clasificador=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)

while cap.isOpened():
	_,img=cap.read()
	img=cv2.resize(img,(800,600))
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	face=clasificador.detectMultiScale(gray,1.1,4)

	for (x,y,w,h) in face:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

	cv2.imshow("imagen",img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		cap.release()
cv2.destroyAllWindows()