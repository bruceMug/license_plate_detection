import easyocr
# import cv2

print('Reached here')
reader = easyocr.Reader(['en'], gpu=False) # this needs to run only once to load the model into memory
print('Reached here')

# image = cv2.imread('./test_files/test_two.jpg')
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

result = reader.readtext('./test_files/test_two.jpg', detail = 0)
print(f"The output is: {result}")
