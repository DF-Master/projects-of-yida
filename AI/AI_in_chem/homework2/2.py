import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Open data
train_data = pd.read_csv("./AI/AI_in_chem/homework2/train.csv",
                         header=0,
                         sep=",")
test_data = pd.read_csv("./AI/AI_in_chem/homework2/test.csv",
                        header=0,
                        sep=",")


# Draw Boxplot Chart
def draw_data_boxplot(str_header):
    data = [str(i) for i in train_data[str_header].values.tolist()]
    data_interested = []
    data_uninterested = []
    response = train_data["Response"].values.tolist()
    for i in range(len(data)):
        if response[i] == 0:
            data_uninterested.append(float(data[i]))
        else:
            data_interested.append(float(data[i]))

    # print(data_interested)
    # print(data_uninterested)
    # print(np.asarray(data_interested).reshape(-1, 1))
    # print(np.random.random((10, 1)))

    # Plt Draw
    plt.figure(figsize=(6, 4.5), dpi=120)
    bp = plt.boxplot(
        np.asarray([
            np.asarray(data_interested).reshape(-1, 1),
            np.asarray(data_uninterested).reshape(-1, 1)
        ]),
        labels=[str_header + " Interested", str_header + " Uninterested"],
        showmeans=True)
    plt.xlabel("Data Labels")
    plt.ylabel("Values")
    plt.savefig("./AI/AI_in_chem/homework2/" + str_header + ".png",
                bbox_inches="tight")
    # print(bp['whiskers'][0].get_xydata()[0][1],
    #       bp['whiskers'][1].get_xydata()[0][1],
    #       bp['caps'][0].get_xydata()[0][1], bp['caps'][1].get_xydata()[0][1],
    #       bp['medians'][0].get_xydata()[0][1],
    #       bp['means'][0].get_xydata()[0][1])
    plt.close("all")


draw_data_boxplot("Age")
draw_data_boxplot("Annual_Premium")
