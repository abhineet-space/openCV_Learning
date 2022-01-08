# Different geometric shapes using opencv
import numpy as np
import cv2

img1 = np.zeros([512,1200,3],np.uint8)

#img1 = cv2.imread('data/Photo.jpeg', -1) # -1 :Original
img1 = cv2.line(img1, (0,0), (255,255), (0,0,255), 5)
img1 = cv2.arrowedLine(img1, (0,255), (255,255), (0,0,255), 5)
img1 = cv2.rectangle(img1,(0,0),(500,230),(0,0,120),5)
img1 = cv2.circle(img1,(500,63),63,(0,255,0),-1)
img1 = cv2.putText(img1,"Test text",(10,500),cv2.FONT_HERSHEY_SIMPLEX, 4,(255,255,255),10,cv2.LINE_AA)
cv2.imshow('Display window 1', img1)


#Closing and Saving
k = cv2.waitKey(0)
if k == 27 : 
    cv2.destroyAllWindows
elif k == ord('s'):
    cv2.imwrite('Grascale.png',img1)
    cv2.destroyAllWindows

