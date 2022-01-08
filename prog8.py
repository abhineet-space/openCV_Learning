# TODO: Basic Arithmetic operations on images
import cv2
img = cv2.imread('Data\messi.jpg')
img2 = cv2.imread('Data\Logo.jpg')
print('Image Shape(rows, columns and channels) : ',img.shape) 
print('Image Size(no of pixels) : ',img.size)
print("Image Data Type : ",img.dtype)

b,g,r = cv2.split(img)
#print(b,g,r)
img = cv2.merge((b,g,r))


#ball = img[373:423, 496:546]
#img[382:432, 181:231] = ball
img = cv2.resize(img,100,100)
img2 = cv2.resize(img2,100,100)

dst = cv2.add(img,img2)


cv2.imshow('Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()