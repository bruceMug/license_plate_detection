# import packages
from ultralytics import YOLO
import cv2
from sort.sort import *
from utils import get_car, read_license_plate, write_csv
from plates import read_detect_plates


mot_tracker = Sort()  # create instance of the SORT tracker

# load models
coco_model = YOLO('./models/yolov8n.pt')   # detecting cars
# license_plate_detector = YOLO('./models/license_plate_detector.pt') # detecting license plates

print('Reading video ...')
# read frames
cap = cv2.VideoCapture('./test_one.mp4')

# vehicles of interest
vehicles = [2, 3, 6, 5, 7]
results = {}

# to track the frame count
frame_nmr = -1

while True:
    frame_nmr += 1
    ret, frame = cap.read()
    
    # 
    if ret and frame_nmr < 50:
        frame = cv2.resize(frame, (640, 480))
        # print(frame_nmr)
        results[frame_nmr] = {}
        # print(results)
    
        # ------------------------------------------------------------------------------vehicles
        # detect vehicles
        detections = coco_model(frame)[0]  # returns a list of detections
        detections_ = [] # list of all bounding boxes
        
        for detection in detections.boxes.data.tolist():
            x1, y1, x2, y2, confidence_score, class_id = detection
            
            if int(class_id) in vehicles:
                detections_.append([x1, y1, x2, y2, confidence_score])
                
        
    else:
        break
        
# print(output)
# save results to file
# write_csv(output, './results.csv')