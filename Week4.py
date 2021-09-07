import cv2
import copy

# reading images
img = cv2.imread('Photos/Mywallpaper.png')
cv2.imshow('Original', img)

#Rescaling
newscale = 0.5
width = int(img.shape[1])
height = int(img.shape[0])
newWidth = int(img.shape[1]*newscale)
newHeight = int(img.shape[0]*newscale)
dimensions = (width, height)
resizedimage = cv2.resize(img, (newWidth, newHeight))
cv2.imshow('Resized', resizedimage)

#Drawing a circle at the center
circle = copy.copy(img)
cv2.circle(circle,(round(width/2),round(height/2)),44,(0,0,255),thickness=2)
cv2.imshow('Circle',circle)

#Making grey scale:
greyScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Greyscale', greyScale)

#Making blur
blur = cv2.GaussianBlur(greyScale, (9, 9), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur)

#Making canny
canny = cv2.Canny(blur, 10, 50)
cv2.imshow('Canny Layer', canny)

#Rotating 45 degree
rotPoint = (width // 2, height // 2)
rotMat = cv2.getRotationMatrix2D(rotPoint, 45, scale=1.0)

rotate = cv2.warpAffine(img, rotMat, dimensions)
cv2.imshow('Rotate', rotate)

cv2.waitKey(0)