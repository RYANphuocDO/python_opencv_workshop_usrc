import cv2


#reading images
img = cv2.imread('..\Photos\Mywallpaper.png')
cv2.imshow('Wallpaper', img)


cv2.waitKey(0)