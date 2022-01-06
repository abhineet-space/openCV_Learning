# Different geometric shapes using opencv
# Reading and displaying an image from file
import cv2

img1 = cv2.imread('data/Photo.jpeg', -1) # 0 :Grayscale


cv2.imshow('Display window 1', img1)

k = cv2.waitKey(0) & 0xFF
if k == 27 : 
    cv2.destroyAllWindows
elif k == ord('s'):
    cv2.imwrite('Grascale.png',img1)
    cv2.destroyAllWindows

