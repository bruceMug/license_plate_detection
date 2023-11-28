# import packages
from ultralytics import YOLO
import cv2

# load models
coco_model = YOLO('yolov8n.pt')   # detecting cars
license_plate_detector = YOLO('./models/license_plate_detector.pt')  # detecting license plates


# read frames
cap = cv2.VideoCapture('./test_one.mp4')

# to track the frame count
frame_nmr = 0

while True:
    frame_nmr += 1
    ret, frame = cap.read()
    
    # 
    if ret and frame_nmr < 10:
    
        # detect vehicles
        detections = coco_model(frame)  # returns a list of detections
        print(detections)

        # track vehicles


        # detect license plates


        # assign plate to car


        # crop and process the plates


        # read plates


        # write results

