from PIL import Image
import numpy as np
import cv2
import imageio

img = Image.open('.\\AI\AI_in_chem\\YGO-AI\\OCR\\test.gif')
img = cv2.GaussianBlur(np.array(img), (3, 3), 0)
# 3，3为模糊范围，可以自行设置；后面的参数是模糊的标准差，0表示使用默认值
cv2.imwrite('.\\AI\\AI_in_chem\\YGO-AI\\OCR\\test_after.jpg', img)  # Save img
