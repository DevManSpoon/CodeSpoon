import cv2 

img = cv2.imread('test.jpg') 

bAvg = cv2.blur(img,(7,7)) 
cv2.imshow('Averaging',bAvg) 
cv2.waitKey(0) 

gBlur = cv2.GaussianBlur(img, (3,3),0) 
cv2.imshow('Gaussian Blur', gBlur) 
cv2.waitKey(0) 

cv2.destroyAllWindows() 
