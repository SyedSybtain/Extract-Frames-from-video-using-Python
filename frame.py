import cv2
import os

if not os.path.exists("frames"):
  os.mkdir("frames")
vidcap = cv2.VideoCapture('sample.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frames/frams%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
