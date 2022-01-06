[1mdiff --git a/Data/Photo.jpeg b/Data/Photo.jpeg[m
[1mindex 87ea57b..ad4ddd8 100644[m
Binary files a/Data/Photo.jpeg and b/Data/Photo.jpeg differ
[1mdiff --git a/Grascale.png b/Grascale.png[m
[1mindex 9151899..7607d27 100644[m
Binary files a/Grascale.png and b/Grascale.png differ
[1mdiff --git a/prog3.py b/prog3.py[m
[1mindex 7a6e191..885c5c2 100644[m
[1m--- a/prog3.py[m
[1m+++ b/prog3.py[m
[36m@@ -1,12 +1,19 @@[m
 # Different geometric shapes using opencv[m
[31m-# Reading and displaying an image from file[m
[32m+[m[32mimport numpy as np[m
 import cv2[m
 [m
[31m-img1 = cv2.imread('data/Photo.jpeg', -1) # 0 :Grayscale[m
[31m-[m
[32m+[m[32mimg1 = np.zeros([512,1200,3],np.uint8)[m
 [m
[32m+[m[32m#img1 = cv2.imread('data/Photo.jpeg', -1) # -1 :Original[m
[32m+[m[32mimg1 = cv2.line(img1, (0,0), (255,255), (0,0,255), 5)[m
[32m+[m[32mimg1 = cv2.arrowedLine(img1, (0,255), (255,255), (0,0,255), 5)[m
[32m+[m[32mimg1 = cv2.rectangle(img1,(0,0),(500,230),(0,0,120),5)[m
[32m+[m[32mimg1 = cv2.circle(img1,(500,63),63,(0,255,0),-1)[m
[32m+[m[32mimg1 = cv2.putText(img1,"Test text",(10,500),cv2.FONT_HERSHEY_SIMPLEX, 4,(255,255,255),10,cv2.LINE_AA)[m
 cv2.imshow('Display window 1', img1)[m
 [m
[32m+[m
[32m+[m[32m#Closing and Saving[m
 k = cv2.waitKey(0) & 0xFF[m
 if k == 27 : [m
     cv2.destroyAllWindows[m
