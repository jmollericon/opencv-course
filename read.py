import cv2 as cv

# reading image
img = cv.imread('resources/photos/cat.jpg')
cv.imshow('Cat', img)

# reading large image
img2 = cv.imread('resources/photos/cat_large.jpg')
cv.imshow('Cat (large image)', img2)

#reading videos
capture = cv.VideoCapture('resources/videos/dog.mp4')
while True:
  isTru, frame = capture.read()
  cv.imshow('Video', frame)

  if cv.waitKey(20) & 0xFF==ord('d'):
    break

capture.release()
cv.destroyAllWindows()