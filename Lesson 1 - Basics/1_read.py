import cv2
import numpy

#reading images
img = cv2.imread('..\Photos\cat.jpg')
cv2.imshow('Cat', img)


cv2.waitKey(0)
