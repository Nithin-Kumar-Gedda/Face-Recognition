import cv2
import numpy as np 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture('vid1.mp4')
while cap.isOpened():
    re,img = cap.read()
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_rect = face_cascade.detectMultiScale(gray_img,1.1)
    for (x,y,w,h) in face_rect:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('DETECTED FACE',img)
        #cv2.waitKey(0)
    if cv2.waitKey(1)  == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()