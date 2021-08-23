import cv2
import numpy as np 
img=cv2.imread("euro.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.resize(img,(800,400))
blur=cv2.blur(img,(3,3))
edges=cv2.Canny(blur,100,150,None)
lines=cv2.HoughLines(edges,1,np.pi/180,145)
img=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imshow("camion",img)
cv2.waitKey(0)
cv2.destroyAllWindows()