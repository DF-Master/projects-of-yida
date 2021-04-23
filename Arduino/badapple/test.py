import cv2
import csv
  
# read the image file
img = cv2.imread('Arduino\\badapple\\index.jpg', 0)
img = cv2.resize(img,(25,16))
  
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
  
# converting to its binary form
# bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# bw=cv2.resize(bw_img,(260,160))

# cv2.imshow("Binary", bw)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



rn_img = bw_img//255
i = [list(i) for i in rn_img]

with open("Arduino\\badapple\\img.csv","w",newline='') as csvfile_edit:
    for j in i:
        csv.writer(csvfile_edit).writerow(j)

