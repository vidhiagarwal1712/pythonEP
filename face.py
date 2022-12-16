import cv2 

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

image = cv2.imread("test.jpg")

faces = face_cascade.detectMultiScale(image,1.1,4)

for (x,y,w,h) in faces: 
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),5)

cv2.imshow("Face Detected",image)
cv2.waitKey()