from ultralytics import YOLO
import cv2
from sort.sort import *
from utils import get_car, read_license_plate, write_csv
from plates import read_detect_plates
from tqdm import tqdm

mot_tracker = Sort()  # create instance of the SORT tracker
detectModel = YOLO('./models/yolov8n.pt')   # detecting cars


def main(video_path, output_path):
    print('Reading video ...')
    cap = cv2.VideoCapture(video_path)

    vehicles = [2, 3, 6, 5, 7]  # vehicles of interest
    results = {}

    # to track the frame count
    frame_nmr = -1

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(
        f"{output_path}/output_video.mp4", fourcc, 30, (1920, 1080))

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.resize(frame, (1920, 1080))

        # Detect vehicles
        detections = detectModel(frame)[0]
        detections_ = []

        for detection in tqdm(detections.boxes.data.tolist()):
            x1, y1, x2, y2, confidence_score, class_id = detection

            frame = cv2.rectangle(frame, (int(x1), int(
                y1)), (int(x2), int(y2)), (0, 255, 0), 1)

            if int(class_id) in vehicles:
                detections_.append([x1, y1, x2, y2, confidence_score])

        track_ids = mot_tracker.update(np.asarray(detections_))
        frame = read_detect_plates(frame, track_ids)
        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
