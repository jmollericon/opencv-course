import cv2 as cv

def rescaleFrame(frame, scale=0.75):
  # this is for Images, Videos and Live Video
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)
  dimensions = (width, height)
  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
  # this is for Live Video
  capture.set(3, width)
  capture.set(4, height)

# reading image
img = cv.imread('resources/photos/cat.jpg')
cv.imshow('Cat (large image)', img)

resized_image = rescaleFrame(img)
cv.imshow('Cata resized', resized_image)

# reading videos
capture = cv.VideoCapture('resources/videos/dog.mp4')

while True:
  isTru, frame = capture.read()
  frame_resized = rescaleFrame(frame, scale=.2)
  cv.imshow('Video', frame)
  cv.imshow('Video Resized', frame_resized)

  if cv.waitKey(20) & 0xFF==ord('d'):
    break

capture.release()
cv.destroyAllWindows()