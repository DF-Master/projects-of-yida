import cv2
import os
import numpy as np
import random
import pydeck


def get_pid_to_name():

    pidtoname_cnnid_dic = {}
    cnnid = 0
    con = pydeck.loadDatabase(
        'C:/Users/jiang/Documents/GitHub/projects-of-yida/AI/AI_in_chem/YGO-AI/cdbopen/cards_en.cdb'
    )

    for filepath in [
            '.\AI\AI_in_chem\YGO-AI\OCR\deck\deck_kaiba/',
            './AI\AI_in_chem\YGO-AI\OCR\deck\deck_yogi/'
    ]:
        for file_root_path, fold, img_name_list in os.walk(filepath):
            for img_name in img_name_list:
                img = cv2.imread(filepath + img_name)
                cnnid += 1
                pid = img_name.split('.')[0]
                card_name = pydeck.getText(pid, 'name')
                pidtoname_cnnid_dic[card_name] = cnnid
    print(pidtoname_cnnid_dic)
    return pidtoname_cnnid_dic


if __name__ == '__main__':
    get_pid_to_name()