import cv2
import time
import csv

with open("Arduino\\badapple\\img.csv","w",newline='') as csvfile_edit:
    csv.writer(csvfile_edit).writerow(['BAD APPLE -- By Yida'])
    

for i in range(6569):
    # read the image file
    img = cv2.imread('Arduino\\badapple\\badapple-all\\BAimg'+str(i+1).zfill(8)+'.jpg', 0)
    img = cv2.resize(img,(25,16))

    ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    bw_img=bw_img//255
    print(bw_img)
    time.sleep(0.033)
    
    with open("Arduino\\badapple\\img.csv","a",newline='') as csvfile_edit:
        csv.writer(csvfile_edit).writerow(['##'])
        for j in bw_img:
            csv.writer(csvfile_edit).writerow(j)
        csv.writer(csvfile_edit).writerow(['##'])
        
        