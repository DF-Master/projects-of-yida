import csv
import numpy as np

csvsend=[]

with open('Arduino\\badapple\\img.csv', encoding='utf-8') as imgfile:
    with open('Arduino\\badapple\\badapplesend.csv',"w", encoding='utf-8') as imgsend:
        for i in imgfile:
            if len(i)>100:
                imgsend.write(i.strip('"').strip('\n').strip('"').strip('*').strip(',')+','+'\n')
            else:
                imgsend.write('#'+'\n')
        