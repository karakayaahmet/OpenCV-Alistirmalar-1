import cv2
from cv2 import waitKey
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture("hsv.mp4")
cv2.namedWindow("Trackbar")

cv2.createTrackbar("lh", "Trackbar", 0, 179, nothing)
cv2.createTrackbar("ls", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("lv", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("uh", "Trackbar", 0, 179, nothing)
cv2.createTrackbar("us", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("uv", "Trackbar", 0, 255, nothing)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640,480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("lh", "Trackbar")
    ls = cv2.getTrackbarPos("ls", "Trackbar")
    lv = cv2.getTrackbarPos("lv", "Trackbar")
    uh = cv2.getTrackbarPos("uh", "Trackbar")
    us = cv2.getTrackbarPos("us", "Trackbar")
    uv = cv2.getTrackbarPos("uv", "Trackbar")

    lower_blue = np.array([lh,ls,lv])
    upper_blue = np.array([uh,us,uv])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    bitwise = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("bitwise", bitwise)

    if waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
