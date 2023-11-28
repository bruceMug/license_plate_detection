# import packages
from ultralytics import YOLO
import cv2

# load models
coco_model = YOLO('yolov8n.pt')   # detecting cars
# license_plate_detector = YOLO('./models/license_plate_detector.pt')  # detecting license plates

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
    
        # detect vehicles
        detections = coco_model(frame)[0]  # returns a list of detections
        # print(detections)
        for detection in detections.boxes.data.tolist():
            # one detection looks like [2043.2545166015625, 878.5299682617188, 2427.350341796875, 1226.425048828125, 0.894658625125885, 2.0]
            x1, y1, x2, y2, confidence_score, class_id = detection
            print(detection)
            
            # we only want to detect vehicles
            if int(class_id) in vehicles:
                pass
            
            # draw a bounding box rectangle and label on the image
            # color = (0, 255, 0)
            # cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness=2)
            # cv2.putText(frame, str(int(class_id)), (int(x1), int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            
        # show the output frame
        # cv2.imshow('Frame', frame)
        # key = cv2.waitKey(1) & 0xFF
        # if key == ord('q'):
        #     break
        

        # track vehicles


        # detect license plates


        # assign plate to car


        # crop and process the plates


        # read plates


        # write results

