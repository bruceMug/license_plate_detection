import numpy as np
import cv2
from func import func

# from pc camera
cap = cv2.VideoCapture(0)

# from live Ip camera
# cap = cv2.VideoCapture('http://192.168.1.107:8080/video')

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# saving video
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))


while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    func()
    out.write(frame)
    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
