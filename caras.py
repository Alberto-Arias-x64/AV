import cv2

clasificador=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("scarlett.jpg")
img=cv2.resize(img,(800,600))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face=clasificador.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in face:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

cv2.imshow("imagen",img)
cv2.waitKey(0)
cv2.destroyAllWindows()