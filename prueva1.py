import cv2
import numpy

imagen=cv2.imread('marcelo.jpg',0)
cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(imagen)