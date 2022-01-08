from run_CNN import CNN, mySet
import make_scancard_number_tag
import os
import cv2
import numpy as np
from torch.utils.data import DataLoader

model_cnn = CNN(True, 0.1)
model_cnn.load_checkpoint('H:\code\checkpoints\model_cnn_0.1.pt')

# get cnnid to card_name list
cnnid_to_cardname_dic = make_scancard_number_tag.get_pid_to_name()

# input dir
inputpath = 'H:\\code\\CNN_val\\recognized_pics_using_border_and_color_selected\\recognized_pics_using_border_and_color_selected/'
images_list = []

# Input Img
for file_root_path, fold, img_name_list in os.walk(inputpath):
    for img_name in img_name_list:
        img = cv2.imread(inputpath + img_name)
        img = cv2.resize(img[100:410, 50:360], (134, 134))
        img = img.astype(np.float32) / 255
        img = np.moveaxis(img, -1, 0)
        try:
            img_id = int(cnnid_to_cardname_dic[img_name.split('_')[0]])
        except:
            if img_name.split('_')[0] == 'Aussa the Earth Charmer':
                img_id = 80
            elif img_name.split('_')[0] == 'IP Masquerena':
                img_id = 63
            elif img_name.split('_')[
                    0] == 'Number 38 Hope Harbinger Dragon Titanic Galaxy':
                img_id = 22

        images_list.append((img, img_id))

images_set = mySet(images_list)

valloader = DataLoader(images_set,
                       32,
                       shuffle=False,
                       num_workers=1,
                       drop_last=False)

if __name__ == '__main__':
    accuracy, confusion_matrix = model_cnn.evaluation(valloader)
    print(accuracy, "/n", confusion_matrix.tolist())
    with open('.\\AI\\AI_in_chem\\YGO-AI\\CNN\\result.txt', "w") as f:
        f.writelines(str(accuracy))
        for i in confusion_matrix.tolist():
            f.writelines("\n")
            f.writelines(str(i))
