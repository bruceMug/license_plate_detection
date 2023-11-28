# import packages
from ultralytics import YOLO
import cv2
from sort.sort import *
from utils import get_car, read_license_plate


mot_tracker = Sort()  # create instance of the SORT tracker

# load models
coco_model = YOLO('yolov8n.pt')   # detecting cars
# license_plate_detector = YOLO('./models/license_plate_detector.pt') # detecting license plates

print('Reading video ...')
# read frames
cap = cv2.VideoCapture('./test_one.mp4')

# vehicles of interest
vehicles = [2, 3, 6, 5, 7]

# to track the frame count
frame_nmr = -1

while True:
    frame_nmr += 1
    ret, frame = cap.read()
    
    # 
    if ret and frame_nmr < 2:
        frame = cv2.resize(frame, (640, 480))
    
        # ------------------------------------------------------------------------------vehicles
        # detect vehicles
        detections = coco_model(frame)[0]  # returns a list of detections
        detections_ = [] # list of all bounding boxes
        
        for detection in detections.boxes.data.tolist():
            # one detection looks like [2043.2545166015625, 878.5299682617188, 2427.350341796875, 1226.425048828125, 0.894658625125885, 2.0]
            x1, y1, x2, y2, confidence_score, class_id = detection
            # print(detection)
            
            # we only want to detect vehicles
            if int(class_id) in vehicles:
                detections_.append([x1, y1, x2, y2, confidence_score])
                
        # track vehicles
        track_ids = mot_tracker.update(np.asarray(detections_))
        # print(track_ids)
        
        
        # ------------------------------------------------------------------------------plates
        """ this part is dependent on the model that will be trained """
        # detect license plates
        license_plates = license_plate_detector(frame)[0]
        
        for license_plate in license_plates.boxes.data.tolist():
            x1, y1, x2, y2, confidence_score, class_id = license_plate
            
            # assign license plate to given car
            """ we have captured all the plates and cars in a given frame and at this point we don't know which plate belongs to which car."""
            xcar1, ycar1, xcar2, ycar2, car_id = get_car(license_plate, track_ids)
            """ the returned car id is unique and will be used to identify the car through out the video"""
            
            # crop the plates
            license_plate_crop = frame[ int(y1):int(y2), int(x1):int(x2) ]
            
            # process the plate i.e convert to grayscale, threshold, etc
            license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
            _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV)
            # cv2.threshold(license_plate_crop_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
            
            # visualize the plate
            # cv2.imshow('Frame', license_plate_crop_gray)
            # cv2.imshow('Frame', license_plate_crop_thresh)
            # cv2.waitKey(0)
            
            
            # read license plate
            read_license_plate(license_plate_crop_thresh)
        
        
                        
                # draw a bounding box rectangle and label on the image
                # color = (0, 255, 0)
                # cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness=2)
                # cv2.putText(frame, str(int(class_id)), (int(x1), int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            
            # draw a bounding box rectangle and label on the image
            # color = (0, 255, 0)
            # cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness=2)
            # cv2.putText(frame, str(int(class_id)), (int(x1), int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            
        # show the output frame
        # cv2.imshow('Frame', frame)
        # key = cv2.waitKey(1) & 0xFF
        # if key == ord('q'):
        #     break




        # read plates


        # write results

