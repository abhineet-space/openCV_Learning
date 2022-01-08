# TODO: Detect face from live feed.
import cv2
face_cascade = cv2.CascadeClassifier('predefined/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
while(True):
    flag, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 3)
    cv2.imshow('Result',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()