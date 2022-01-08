#Add properties to captured images
import cv2
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
    if flag == True:
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
        grey = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        cv2.imshow("New Frame", frame)
        
    else:
        break
cap.release()
cv2.destroyAllWindows()

