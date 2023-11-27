import string
import easyocr

reader = easyocr.Reader(['en'], gpu=False)

# mapping characters for character conversion


def write_csv(results, output_path):
    """ write content to csv file"""
    
    
