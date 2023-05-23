import cv2
import numpy as np 
path = "img2.jpg"
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('img2.jpg')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_rect = face_cascade.detectMultiScale(gray_img,1.1,5)
for (x,y,w,h) in face_rect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('IMAGE',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print(round(cv2.rectangle))