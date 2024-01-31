""" this function is to detect license plates """
from ultralytics import YOLO
import cv2
from utils import get_car, read_license_plate, write_csv, log_output
from track_ids import track_ids

# load the trained model
license_plate_detector = YOLO('./models/license_plate_detector.pt')

def read_detect_plates(frame, results, frame_nmr, track_ids):
    # results[frame_nmr] = {}
    
    license_plates = license_plate_detector(frame)[0]
    # print(license_plates)

    """ 
    ``` https://docs.ultralytics.com/reference/engine/results/#ultralytics.engine.results.Boxes ```
    x.boxes returns all attributes information for the detected bounding boxes
    x.boxes.data returns only the coordinates of the bounding boxes in form of a tensor (high dimension array)
    We use tolist() to convert the tensor to a list

    Output: [[x1, y1, x2, y2, confidence_score, class_id], [x1, y1, x2, y2, confidence_score, class_id], ...]
        where the class_id is the class of the detected object i.e car, truck, plane etc
    """


    # loop over the detected license plates
    for license_plate in license_plates.boxes.data.tolist():
        x1, y1, x2, y2, conf, class_id = license_plate

        """ 
        At this point, we have a list of plates and vehicles and don't know what belongs to what.
        Match the license plates with the vehicles
        Use the get_car function to get the vehicle that the license plate belongs to 
        """

        xcar1, ycar1, xcar2, ycar2, car_id = get_car(license_plate, track_ids)

        # crop and grayscale the plates
        license_plate_crop = frame[int(y1):int(y2), int(x1):int(x2)]
        license_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
        # to easily read the plate, we apply a threshold (dense black and white)
        ret, license_plate_thresh = cv2.threshold(license_gray, 127, 255, cv2.THRESH_BINARY_INV)

        # read plate using ocr
        license_plate_text, plate_conf_score = read_license_plate(license_plate_thresh)
        # check if text /plate is valid
        if license_plate_text is not None:
            # log plate details
            # log_output([license_plate_text, frame_nmr])
            
            # store results in a dictionary
            results[frame_nmr][car_id] = {'car': {'bbox': [xcar1, ycar1, xcar2, ycar2]},
                                        'license_plate': {'bbox': [x1, y1, x2, y2],
                                                            'text': license_plate_text,
                                                            'box_confidence_score': conf,
                                                            'plate_text_score': plate_conf_score}}
            print(license_plate_text)
            
            # print(frame_nmr)
            # print(car_id)
            # write_csv(results, frame_nmr, car_id)
        else:
            print("I reach here -")
            pass
        # print('Onto another license plate -->')
        # print('I reach here -')
    
    # return results
