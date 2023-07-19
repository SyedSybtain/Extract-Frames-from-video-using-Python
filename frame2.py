import cv2
import os

if not os.path.exists("frames2"):
    os.mkdir("frames2")
# Opens the Video file
cap= cv2.VideoCapture('sample.mp4')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('frames2/frame'+str(i)+'.jpg',frame)
    i+=2

cap.release()
cv2.destroyAllWindows()
