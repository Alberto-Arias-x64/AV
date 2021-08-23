import cv2
import numpy
from matplotlib import pyplot as plot

imagen=cv2.imread('marcelo.jpg')
imagen=cv2.resize(imagen,(400,300))
cv2.imshow('imagen',imagen)
imagen=cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
plot.imshow(imagen)
plot.xticks([]),plot.yticks([])
plot.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
#print(imagen)