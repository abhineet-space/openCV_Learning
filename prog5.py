#Add Current date and time on a live video
import cv2
import datetime
cap = cv2.VideoCapture(0)
#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(3))
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(4))
# set width and height
#cap.set(3, 1208) # CAP_PROP_FRAME_WIDTH Short code = 3
#cap.set(4, 720) # CAP_PROP_FRAME_HEIGHT short code = 4
#print("New Width and height")
#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while (True):
    flag, frame = cap.read()
    if (flag == True):
        font = cv2.FONT_HERSHEY_SIMPLEX
        Text = 'Width' + str(cap.get(3)) + ' Height' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10,50), font, 1.5, (0,255,255), 2, cv2.LINE_AA )
        cv2.imshow("New Frame", frame)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

