#Challenge: Draw the grid lines of the sudoku image by detecting the lines using a Hough transform. Use image sudoku.png from the Github.
#It's not fully detected but I have tried my best tho

import cv2
import numpy as np

frame = cv2.imread('../Photos/sudoku.png')
edges = cv2.Canny(frame,100,800) 

minLineLength=100
maxLineGap=10
edges = cv2.Canny(frame,100,200)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
blankImage = np.zeros(frame.shape)

#draw the lines onto our blank image
for l in lines:
    for x1,y1,x2,y2 in l:
        cv2.line(blankImage,(x1,y1),(x2,y2),(0,255,0),4)



cv2.imshow("original", frame)
cv2.imshow("lines", blankImage)
cv2.waitKey(-1)
