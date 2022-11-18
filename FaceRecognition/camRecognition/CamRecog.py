import cv2
import numpy as np
Face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
find = cv2.VideoCapture(0)
while find.isOpened():
    r,img = find.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = Face_cascade.detectMultiScale(gray)
    for a,b,c,d in face:
        cv2.rectangle(img,(a,b),(a+c,b+d),(255,0,0),3)
        cv2.imshow("LIVE RECOGNITION",img)
    key = cv2.waitKey(1)
    if key == ord('s'):
        break
find.release()
cv2.destroyAllWindows()


