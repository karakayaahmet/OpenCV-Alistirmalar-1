import cv2
import numpy as np

cap = cv2.VideoCapture("car.mp4")
subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640,480))
    mask = subtractor.apply(frame)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()