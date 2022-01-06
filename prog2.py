# CApture save live video
import cv2

cap= cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')  #to get fourcc
out = cv2.VideoWriter('output.mp4',fourcc,20.0,(640,480)) # to save video
print(cap.isOpened())
while(True):

    flag, frame = cap.read()
    if (flag == True):
        out.write(frame)
    #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame Name', grey)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
out.release()
cv2.destroyAllWindows()