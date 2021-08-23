import numpy as np
import cv2
from matplotlib import pyplot as plt 

#img=np.zeros((200,200),np.uint8)
img=cv2.imread("euro.jpg")
img=cv2.resize(img,(600,300))
imgg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
b,g,r=cv2.split(img)

cv2.imshow("img",img)
plt.subplot(2,3,1),plt.hist(img.ravel(),256,[0,256])
plt.title("Original")

plt.subplot(2,3,2),plt.hist(imgg.ravel(),256,[0,256])
plt.title("Gris")

plt.subplot(2,3,3),plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.title("Compuesto")

histo=cv2.calcHist([imgg],[0],None,[256],[0,256])
plt.subplot(2,3,5),plt.plot(histo)
plt.title("CV2")

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()