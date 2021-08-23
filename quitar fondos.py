import numpy as np
import cv2 as cv
cap = cv.VideoCapture("truck.mp4")
fgbg =cv.createBackgroundSubtractorMOG2(detectShadows=False)
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    frame=cv.resize(frame,(600,400))
    fgmask = fgbg.apply(frame)

    cv.imshow('Frame', frame)
    cv.imshow('FG MASK Frame', fgmask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
cap.release()
cv.destroyAllWindows()