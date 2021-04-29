import csv

csvsend=[]

with open('Arduino\\badapple\\img.csv', encoding='utf-8') as imgfile:
    slice8*5 =[]
    for i in imgfile:
        if len(i)==50: #csv长度为50
            slice25 = i.strip('\n').split(',')
            
            
            # 制作单位5的list
            slice5 = []
            for i in range(5):
                k=''
                for q in slice25[i*5:i*5+5]:
                    k+=q
                slice5.append(k)
            
        # 每8个List组合一次