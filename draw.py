import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Point the image a certain color
#blank[200:300, 300:400] = 255,0,0 # BGR
#cv.imshow('Blue', blank)

# 2. Draw a Rectangle
#cv.rectangle(blank, (0,0), (250,250), (0,0,255), thickness=cv.FILLED) # -1
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=2)
cv.imshow('Rectangle', blank)

# 3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (0,255,0), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a Line
cv.line(blank, (50,50), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=2)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Jorge!', (25,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,255), 2)
cv.imshow('Text', blank)

#img = cv.imread('resources/photos/cat.jpg')
#cv.imshow('Cat', img)

cv.waitKey(0)