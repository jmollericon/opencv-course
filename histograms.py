import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('resources/photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
#cv.imshow('Circle', mask)

gray_masked = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow('Image Gray Masked', gray_masked)

# Gratscale histogram
#gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
gray_hist = cv.calcHist([gray], [0], gray_masked, [256], [0,256])

plt.figure('Figure 1')
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

# Colour Histogram
colour_masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Image Colour Masked', colour_masked)

plt.figure('Figure 2')
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
  #hist2 = cv.calcHist([img], [i], None, [256], [0, 256])
  hist2 = cv.calcHist([img], [i], mask, [256], [0, 256])
  plt.plot(hist2, color=col)
  plt.xlim([0, 256])
plt.show()

cv.waitKey(0)