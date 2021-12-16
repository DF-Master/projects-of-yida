import csv
from os import read
with open('./AI/AI_in_chem/YGO-AI/OCR/deck/ocr_data.csv',
          "r",
          encoding="latin-1") as f:
    reader = csv.reader(f)
    for i in reader:
        print(i)
