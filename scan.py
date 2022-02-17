#Аристарх 16.10.21 (By LEDShack)
#Я ахуел пока написал то что работает криво
import cv2
from PIL import Image
face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
def pasport(src):
    #
    img = cv2.imread("screenshot/" + src)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade_db.\
            detectMultiScale(img, 1.1, 19)
    for (x,y,w,h) in faces:
        #cv2.rectangle(img, (x-30, y-67), (x+w+20 ,y+h+50), (0,255,0),2)
        crop = img[y-67:y+h+50, x-30:x+w+20]
    return crop
    #cv2.imshow("Cropped", crop)
    #cv2.imshow('rez', img)
    #cv2.waitKey()
    
def student(src):
    #
    img = cv2.imread("screenshot/" + src)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade_db.\
            detectMultiScale(img, 1.1, 19)
    for (x,y,w,h) in faces:
        #cv2.rectangle(img, (x-23, y-37), (x+w+23 ,y+h+51), (0,255,0),2)
        crop = img[y-37:y+h+51, x-23:x+w+23]
    return crop
    #cv2.imshow("Cropped", crop)
    #cv2.imshow('rez', img)
    #cv2.waitKey()
    
#student("test3.jpg")    
#pasport("test.jpg")
