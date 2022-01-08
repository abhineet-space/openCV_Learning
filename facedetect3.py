# TODO: Detect Eye from live feed 
import cv2
eye_cascade = cv2.CascadeClassifier('predefined/haarcascade_eye_tree_eyeglasses.xml')
face_cascade = cv2.CascadeClassifier('predefined/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
    flag, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in faces :
        cv2.rectangle(frame, (x,y), (x+w, y+h),(255,0,0),3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh),(0,255,0),2)

    cv2.imshow('Face & Eye Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
'''
img = cv2.imread('Data/face.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0),3)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),3)
cv2.imshow('Face & Eye detection', img)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
'''



