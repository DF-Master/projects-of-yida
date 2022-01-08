import cv2
import os
import numpy as np
import random

filepath = '.\AI\AI_in_chem\YGO-AI\CNN\CNN-img-number-source/'

for file_root_path, fold, img_name_list in os.walk(filepath):

    for i in range(8192 * 5):
        img_name = str(random.randrange(1, len(img_name_list) + 1, 1))

        img = cv2.imread(filepath + img_name + ".jpg")
        #加随机模糊
        img = cv2.GaussianBlur(
            img, (random.randrange(1, 9, 2), random.randrange(1, 9, 2)), 0)
        # 加随机旋转
        rows, cols, color = img.shape
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2),
                                    random.randrange(-180, 180, 1),
                                    random.gauss(1, 0.1))
        img = cv2.warpAffine(img, M, (cols, rows))

        # 加随机平移
        T = np.float32([[1, 0, round(random.gauss(0, 25))],
                        [0, 1, round(random.gauss(0, 25))]])
        img = cv2.warpAffine(img, T, (cols, rows))

        # 进行裁剪
        img = cv2.resize(img[80:330, 35:285], (134, 134))
        cv2.imwrite('H:\code\CNN_img/' + str(i) + "_" + img_name + ".jpg", img)
