import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    roi = frame[50:250, 200:400] # frame[y1:y2, x1:x2]

    cv2.rectangle(frame, (200,50), (400,250), (0,0,255), 2)

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    lower_color = np.array([0, 45, 79], np.uint8)
    upper_color = np.array([17, 255, 255], np.uint8)

    mask = cv2.inRange(hsv, lower_color, upper_color)

    cv2.imshow("Frame", frame)
    cv2.imshow("roi", roi)
    cv2.imshow("mask", mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()