import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow("Frame")

circles = []

def mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x,y))


cv2.setMouseCallback("Frame", mouse)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    for center in circles:
        cv2.circle(frame, center, 5, (255, 0, 0), -1)

    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)

    if key == 27:
        break
    
    elif key == ord("t"):
        circles = []

cap.release()
cv2.destroyAllWindows()