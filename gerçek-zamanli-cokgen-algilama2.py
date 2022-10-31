import cv2
from cv2 import arcLength
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Settings")

cv2.createTrackbar("lower-hue","Settings",0,180,nothing)
cv2.createTrackbar("lower-saturation","Settings",0,255,nothing)
cv2.createTrackbar("lower-value","Settings",0,255,nothing)
cv2.createTrackbar("upper-hue","Settings",0,180,nothing)
cv2.createTrackbar("upper-saturation","Settings",0,255,nothing)
cv2.createTrackbar("upper-value","Settings",0,255,nothing)

font = cv2.FONT_HERSHEY_COMPLEX

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("lower-hue","Settings")
    ls = cv2.getTrackbarPos("lower-saturation","Settings")
    lv = cv2.getTrackbarPos("lower-value","Settings")
    uh = cv2.getTrackbarPos("upper-hue","Settings")
    us = cv2.getTrackbarPos("upper-saturation","Settings")
    uv = cv2.getTrackbarPos("upper-value","Settings")

    lower_color = np.array([lh,ls,lv])
    upper_color = np.array([uh,us,uv])

    mask = cv2.inRange(hsv, lower_color, upper_color)
    kernel = np.ones((5,5), np.uint8)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        epsilon = 0.02*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)

        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 400:
            cv2.drawContours(frame, [approx], 0, (0), 5)
            
            if len(approx) == 3:
                cv2.putText(frame, "ucgen", (x,y), font, 1, (0))

            elif len(approx) == 4:
                cv2.putText(frame, "dortgen", (x,y), font, 1, (0))

            elif len(approx) == 5:
                cv2.putText(frame, "besgen", (x,y), font, 1, (0))

            else:
                cv2.putText(frame, "yuvarlak", (x,y), font, 1, (0))

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()