import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Settings")

cv2.createTrackbar("lower-hue","Settings",0,180,nothing)
cv2.createTrackbar("lower-saturation","Settimgs",0,255,nothing)
cv2.createTrackbar("lower-value","Settings",0,255,nothing)
cv2.createTrackbar("upper-hue","Settings",0,180,nothing)
cv2.createTrackbar("upper-saturation","Settings",0,255,nothing)
cv2.createTrackbar("upper-value","Settings",0,255,nothing)

font = cv2.FONT_HERSHEY_COMPLEX

while True:
    ret,frame = cap.read()

    lh = cv2.getTrackbarPos("lower-hue","Settings")
    ls = cv2.getTrackbarPos("lower-saturation","Settings")
    lv = cv2.getTrackbarPos("lower-value","Settings")
    uh = cv2.getTrackbarPos("upper-hue","Settings")
    us = cv2.getTrackbarPos("upper-saturation","Settings")
    uv = cv2.getTrackbarPos("upper-value","Settings")