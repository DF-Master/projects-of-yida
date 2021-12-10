import easyocr
from PIL import Image
import numpy as np
import cv2

img = Image.open(
    './AI/AI_in_chem/YGO-AI/OCR/deck/deck_kaiba/2129638.jpg').resize(
        (59 * 3, 86 * 3))
img = cv2.GaussianBlur(np.array(img), (3, 3), 0)
cv2.imwrite('./AI/AI_in_chem/YGO-AI/OCR/deck/img_test.jpg', img)
reader = easyocr.Reader(
    ['ch_sim',
     'en'])  # this needs to run only once to load the model into memory
# result = reader.readtext(np.array(img))
result = reader.readtext('./AI/AI_in_chem/YGO-AI/OCR/deck/img_test.jpg')
print("Result:", result[0][1], result[0][2])
