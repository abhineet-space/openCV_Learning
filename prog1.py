# Reading and displaying an image from file
import cv2

img1 = cv2.imread('data/Photo.jpeg', 0) # 0 :Grayscale
img2 = cv2.imread('data/Photo.jpeg', 1) # 0 : Color
img3 = cv2.imread('data/Photo.jpeg', -1) # 0 : Original


cv2.imshow('Display window 1', img1)
cv2.imshow('Display window 2', img2)
cv2.imshow('Display window 3', img3)

k = cv2.waitKey(0) & 0xFF
if k == 27 : 
    cv2.destroyAllWindows
elif k == ord('s'):
    cv2.imwrite('Grascale.png',img1)
    cv2.destroyAllWindows

