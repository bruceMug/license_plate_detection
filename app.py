from ultralytics import YOLO
import cv2
from sort.sort import *
from utils import get_car, read_license_plate, write_csv
from plates import read_detect_plates
from tqdm import tqdm

mot_tracker = Sort()  # create instance of the SORT tracker

# load models
coco_model = YOLO('./models/yolov8n.pt')   # detecting cars


def main(video_path, output_path):
    print('Reading video ...')
    cap = cv2.VideoCapture(video_path)

    vehicles = [2, 3, 6, 5, 7]  # vehicles of interest
    results = {}

    # to track the frame count
    frame_nmr = -1
    frame_array = []

    frame_nmr += 1

    while (cap.isOpened()):
        ret, frame = cap.read()

        if ret:
            # frame = cv2.resize(frame, (640, 480))
            results[frame_nmr] = {}

            # ------------------------------------------------------------------------------vehicles
            # detect vehicles
            detections = coco_model(frame)[0]  # returns a list of detections
            detections_ = []

            for detection in tqdm(detections.boxes.data.tolist()):
                x1, y1, x2, y2, confidence_score, class_id = detection

                # draw bounding box
                frame = cv2.rectangle(frame, (int(x1), int(
                    y1)), (int(x2), int(y2)), (0, 255, 0), 1)

                frame_array.append(frame)

                if int(class_id) in vehicles:
                    detections_.append([x1, y1, x2, y2, confidence_score])

            # track vehicles
            track_ids = mot_tracker.update(np.asarray(detections_))

            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
        else:
            break

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(
        f"{output_path}/output_video.mp4", fourcc, 30, (1920, 1080))
    for i in tqdm(range(len(frame_array))):
        out.write(frame_array[i])
    out.release()

    cap.release()
    cv2.destroyAllWindows()
    exit
