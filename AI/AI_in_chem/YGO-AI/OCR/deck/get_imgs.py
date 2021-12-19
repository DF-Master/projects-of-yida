from shutil import copyfile

with open('./AI/AI_in_chem/YGO-AI/OCR/deck/yogi.txt') as deck:

    for i in deck:
        try:
            i = str(int(i))
        except:
            continue
        else:
            print(i, type(i))
            copyfile("H:/MyCardLibrary/ygopro/pics/" + i + ".jpg",
                     "./AI/AI_in_chem/YGO-AI/OCR/deck/deck_yogi/" + i + ".jpg")
