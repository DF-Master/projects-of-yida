import csv
import numpy as np

csvsend=[]

with open('Arduino\\badapple\\img.csv', encoding='utf-8') as imgfile:
    slicewrite=[]
    slice84 =[]
    for i in imgfile:
        if len(i)>30: #csv长度为40
            slice20 = i.strip('\n').split(',')
            
            
           
            # 制作单位5的list
            slice5 = []
            for i in range(4):
                k=''
                for q in slice20[i*5:i*5+5]:
                    k+=q
                slice5.append(k)
            print(slice5)
            if len(slice84)<8:
                slice84.append(slice5)
            else:
                slicewrite.append(np.transpose(slice84).tolist())
                slice84=[]
    with open('Arduino\\badapple\\badapplesend.csv',"w", encoding='utf-8') as imgsend:
        a=0
        b=[]
        for i in slicewrite:
            print(i)
            if a ==0:
                b = i 
                a = 1
            else:
                a = 0
                b= b+i
                csv.writer(imgsend).writerow(b)
                b=[]
        # 每8个List组合一次