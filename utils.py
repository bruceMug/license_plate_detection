import string
import easyocr
import csv, os, datetime

reader = easyocr.Reader(['en'], gpu=False)

# mapping characters for character conversion


def write_csv(results, frame_nmr, car_id):
    """ write content to csv file """
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H")
    output_path = f'./test_files/results_{formatted_time}.csv'
    file_exists = os.path.isfile(output_path)
    
    with open(output_path, 'a' if file_exists else 'w', newline='') as file:
        writer = csv.writer(file)
        header = ["frame_nmr", "car_id", "car_bbox", "license_plate_bbox", "license_plate_text", "bbox_score", "text_score"]
        
        if not file_exists:
            writer.writerow(header)
        
        row_values = [
            frame_nmr, 
            car_id, 
            results[frame_nmr][car_id]['car']['bbox'], 
            results[frame_nmr][car_id]['license_plate']['bbox'], 
            results[frame_nmr][car_id]['license_plate']['text'], 
            results[frame_nmr][car_id]['license_plate']['box_confidence_score'], 
            results[frame_nmr][car_id]['license_plate']['plate_text_score']
            ]
        writer.writerow(row_values)
    
    
def license_complies_format(text):
    """ check if license complies with the format
        this is where you check if the plate is 7 characters long and also
        the format of Ugandan plates i.e both old (i.e 4 alphabets and 3 numbers)
        and new plates ()"""
    
    
def format_license(text):
    """ format license to the required format"""
    


#  important from the computer vision point of view
def read_license_plate(license_plate_thresh):
    """ read license plate from the given cropped image
    Args:
        license_plate_crop: cropped image containing the license plate
        
    Returns:
        tuple containing the formatted license plate text and the confidence score

    """
    detections = reader.readtext(license_plate_thresh)
    return str('UAE 1234'), 0.9
    
    
    
def get_car(license_plate, vehicle_tracker_ids):
    """ get car details
    Args:
        license_plate: receives a license plate containing the coordinates of the license plate (x1, y1, x2, y2)
        vehicle_tracker_ids: list of vehicle track ids and corresponding coordinates (x1, y1, x2, y2)
        
    Returns:
        tuple containing the vehicle id and the vehicle coordinates
    
    """
    # License Plate => x1, y1, x2, y2, conf, class_id
    # Vehicle_tracker_ids => x1, y1, x2, y2, track_id
    x1, y1, x2, y2, l_confidence_score, class_id = license_plate
    # print(len(vehicle_tracker_ids))
    # print(vehicle_tracker_ids.tolist()[0])
    
    found = False
    for i in range(len(vehicle_tracker_ids)):
        xcar1, ycar1, xcar2, ycar2, car_id = vehicle_tracker_ids[i]
        
        if x1 > xcar1 and y1 > ycar1 and x2 < xcar2 and y2 < ycar2:
            found = True
            car_idx = i
        
    if found:
        return vehicle_tracker_ids[car_idx]
    
    return -1, -1, -1, -1, -1



    