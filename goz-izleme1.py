import cv2
from cv2 import waitKey

cap = cv2.VideoCapture("eye_motion.mp4")

while True:
    ret, frame = cap.read()
    if ret is False:
        break

    roi = frame[80:210, 230:450]

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    _,thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
    
    cv2.imshow("roi", roi)

    if cv2.waitKey(80) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()