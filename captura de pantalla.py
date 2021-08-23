import cv2
import numpy as np
import pyautogui
import time

cv2.namedWindow('imagen')

while(1):
	img = pyautogui.screenshot()#region=(0,0, 400, 300)
	frame = np.array(img)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)#CORRECION DE COLOR
	frame=cv2.resize(frame,(800,600))
	cv2.imshow('imagen',frame)
	time.sleep(0.03)#30fps
	k = cv2.waitKey(1)
	if k == 27:break
cv2.destroyAllWindows()

#print(frame)