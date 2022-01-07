import cv2
import os
import numpy as np
import random

i = 0
for filepath in [
        '.\AI\AI_in_chem\YGO-AI\OCR\deck\deck_kaiba/',
        './AI\AI_in_chem\YGO-AI\OCR\deck\deck_yogi/'
]:
    for file_root_path, fold, img_name_list in os.walk(filepath):
        for img_name in img_name_list:
            img = cv2.imread(filepath + img_name)
            i += 1

            cv2.imwrite('AI\AI_in_chem\YGO-AI\CNN/CNN-img/' + str(i) + ".jpg",
                        img)
