import cv2
import time
import os
import handTrackingModule as htm
import numpy as np
import math

cap = cv2.VideoCapture(0)
detector = htm.handDetector()

fingerX=[]
while True:
    _, frame = cap.read()
    if frame is None:
        break
    
    img = detector.findHands(frame)
    
    
    lmList = detector.findPosition(img, draw= False)
    if len(lmList)>5:
        volume= math.sqrt( ((lmList[8][1]-lmList[4][1])**2)+((lmList[8][2]-lmList[4][2])**2) )

        x=(lmList[8][1]+lmList[4][1])//2
        y=(lmList[8][2]+lmList[4][2])//2
        frame=cv2.putText(frame,str(int(volume)),(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,
        2,color=(255,255,0),thickness=2)

      
# cv2.add(frame,eraser)
    cv2.imshow("image", frame)
    #cv2.imshow('de',eraser)

    if cv2.waitKey(1) == ord("q"):
        break
#cv2.imshow('de',eraser)
cv2.destroyAllWindows()
cap.release()
