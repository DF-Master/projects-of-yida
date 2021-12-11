import easyocr
from PIL import Image
import numpy as np
import cv2
import csv


def ocr_cards(card_name, target, blur_x=3, blur_y=3, blur_sigma=0):
    try:
        img = Image.open('./AI/AI_in_chem/YGO-AI/OCR/deck/deck_kaiba/' +
                         card_name + ".jpg").resize((59 * 3, 86 * 3))
    except:
        img = Image.open('./AI/AI_in_chem/YGO-AI/OCR/deck/deck_yogi/' +
                         card_name + ".jpg").resize((59 * 3, 86 * 3))

    img = cv2.GaussianBlur(np.array(img), (blur_x, blur_y), blur_sigma)
    reader = easyocr.Reader(['ch_sim', 'en'])
    result = reader.readtext(img)
    if len(result) > 0:
        if len(result[0]) > 1:
            target.writerow([
                result[0][1], result[0][2], card_name, blur_x, blur_y,
                blur_sigma
            ])
            print("Result:", result[0][1], result[0][2], card_name, blur_x,
                  blur_y, blur_sigma)


with open('./AI/AI_in_chem/YGO-AI/OCR/deck/all_cards.txt', 'r') as deck:
    all_name = []
    for card_id in deck:
        if len(card_id.strip()) > 1:
            try:
                card_id = str(int(card_id))
            except:
                continue
            else:
                if card_id in all_name:
                    continue
                else:
                    all_name.append(card_id)

                    card_name = card_id
                    for blur_sigma in range(20):
                        for blur_x in [1, 3]:
                            for blur_y in [1, 3]:
                                with open(
                                        './AI/AI_in_chem/YGO-AI/OCR/deck/ocr_data.csv',
                                        "a") as file:
                                    writer = csv.writer(file)
                                    ocr_cards(card_name,
                                              writer,
                                              blur_x=blur_x,
                                              blur_y=blur_y,
                                              blur_sigma=blur_sigma / 10)
