import easyocr
from PIL import Image
import numpy as np
import cv2

# img = Image.open('C:/Users/jiang/Downloads/QQ图片20211213192419.jpg').resize(
# (59 * 3, 86 * 3))
img = Image.open('C:/Users/jiang/Downloads/1.jpg')
# img = cv2.GaussianBlur(np.array(img), (3, 3), 0)
# cv2.imwrite('./AI/AI_in_chem/YGO-AI/OCR/deck/img_test.jpg', img)
reader = easyocr.Reader(
    ['en'])  # this needs to run only once to load the model into memory
result = reader.readtext(np.array(img), detail=0)
# result = reader.readtext('./AI/AI_in_chem/YGO-AI/OCR/deck/img_test.jpg')
print("Result:", result)
