#Add properties to captured images
import cv2
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while(True):
    flag, frame = cap.read()
    if(flag == True):
        pass

    
    elif cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Unable to open Camera")
        break
cap.release()
cv2.destroyAllWindows()