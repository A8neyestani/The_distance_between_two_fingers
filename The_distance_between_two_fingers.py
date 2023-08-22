'''
Author: Arman Neyestani 
https://github.com/A8neyestani
A8neyestani@protonmail.com
'''

import cv2
import time
import os
import handTrackingModule as htm
import numpy as np
import math

# Initialize the video capture from the default camera (index 0).
cap = cv2.VideoCapture(0)

# Create a hand detector object using the handTrackingModule.
detector = htm.handDetector()

# List to store finger X positions (not used in the code provided).
fingerX = []

while True:
    # Capture a frame from the video feed.
    success, frame = cap.read()

    # Exit the loop if the frame isn't captured successfully.
    if not success or frame is None:
        break

    # Detect hands in the frame.
    img = detector.findHands(frame)

    # Get the landmark positions of the detected hand.
    lmList = detector.findPosition(img, draw=False)

    # Ensure there are enough landmarks to calculate volume (distance between landmarks 4 and 8).
    if len(lmList) > 5:
        # Calculate the "volume" which is  the distance between the landmarks 4 and 8.
        volume = math.sqrt((lmList[8][1] - lmList[4][1]) ** 2 + (lmList[8][2] - lmList[4][2]) ** 2)

        # Calculate the mid-point between landmarks 4 and 8.
        x = (lmList[8][1] + lmList[4][1]) // 2
        y = (lmList[8][2] + lmList[4][2]) // 2

        # Display the calculated "volume" on the frame.
        frame = cv2.putText(frame, str(int(volume)), (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                            2, color=(255, 255, 0), thickness=2)

    # Show the processed frame.
    cv2.imshow("image", frame)

    # Exit the loop if the 'q' key is pressed.
    if cv2.waitKey(1) == ord("q"):
        break

# Release the video capture object and close all OpenCV windows.
cap.release()
cv2.destroyAllWindows()
