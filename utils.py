import string
import easyocr

reader = easyocr.Reader(['en'], gpu=False)

# mapping characters for character conversion


def write_csv(results, output_path):
    """ write content to csv file"""
    
    
def license_complies_format(text):
    """ check if license complies with the format
        this is where you check if the plate is 7 characters long and also
        the format of Ugandan plates i.e both old (i.e 4 alphabets and 3 numbers)
        and new plates ()"""
    
    
def format_license(text):
    """ format license to the required format"""
    


#  important from the computer vision point of view
def read_license_plate(license_plate_crop):
    """ read license plate from image"""
    
    
def get_car(license_plate, vehicle_tracker_ids):
    """ get car details
    Args:
        license_plate: receives a license plate containing the coordinates of the license plate (x1, y1, x2, y2)
        vehicle_tracker_ids: list of vehicle track ids and corresponding coordinates (x1, y1, x2, y2)
        
    Returns:
        tuple containing the vehicle id and the vehicle coordinates
    
    """
    
    return 0, 0, 0, 0, 0