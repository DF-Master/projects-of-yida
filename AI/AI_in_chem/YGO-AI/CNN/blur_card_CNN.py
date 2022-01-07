import cv2
import os
import numpy as np
import random

filepath = '.\AI\AI_in_chem\YGO-AI\CNN\CNN-img/'
for file_root_path, fold, img_name_list in os.walk(filepath):
    for img_name in img_name_list:
        img = cv2.imread(filepath + img_name)
        #加随机模糊
        img = cv2.GaussianBlur(
            img, (random.randrange(1, 9, 2), random.randrange(1, 9, 2)), 0)
        # 加随机旋转
        rows, cols, color = img.shape
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2),
                                    random.randrange(-30, 30, 1),
                                    random.gauss(1, 0.1))
        # 加随机平移

        img = cv2.warpAffine(img, M, (cols, rows))
        cv2.imwrite('AI\AI_in_chem\YGO-AI\CNN/' + img_name, img)
        exit()