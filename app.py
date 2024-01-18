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

