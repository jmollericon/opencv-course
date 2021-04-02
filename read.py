import cv2 as cv

# read image
img = cv.imread('resources/photos/cat.jpg')
cv.imshow('Cat', img)

# read large image
img2 = cv.imread('resources/photos/cat_large.jpg')
cv.imshow('Cat (large image)', img2)

cv.waitKey(0)