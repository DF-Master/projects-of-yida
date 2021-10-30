from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Open data
train_data_valid = pd.read_csv("./AI/AI_in_chem/homework2/train.csv",
                               header=0,
                               sep=",")

# Split Data
train_split_data, test_split_data = train_test_split(train_data_valid,
                                                     test_size=0.25,
                                                     shuffle=True)
print(f"""train_split_data Shape = {train_split_data.shape}
test_split_data = {test_split_data.shape}""")


def draw_data_bar_pie(str_header, list_data_name, save_name=""):
    data = [str(i) for i in list_data_name[str_header].values.tolist()]
    data_class = {}
    response = list_data_name["Response"].values.tolist()
    num = len(data)
    for i in list(set(data)):
        data_class[i] = 0
        data_class[i + "_response"] = 0

    for i in range(num):
        data_class[data[i]] += 1
        data_class[data[i] + "_response"] += int(response[i])

    for i in list(set(data)):
        i_response_ratio = float("{:.3f}".format(data_class[i + "_response"] /
                                                 data_class[i]))
        data_class[i + "_response_ratio"] = i_response_ratio

    # print(data_class)

    # Draw chart
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 6), dpi=120)
    fig.subplots_adjust(wspace=0.5)

    # Draw ax1 for bar chart
    xlocs = np.arange(0.5, len(list(set(data))) + 0.5)
    ax1.bar(
        xlocs,
        [data_class[i + "_response_ratio"] for i in list(set(data))],
        0.6,
        0.0,
        color="blue",
        label="Interested Ratio",
    )
    ax1.bar(
        xlocs,
        [
            1 - i for i in
            [data_class[i + "_response_ratio"] for i in list(set(data))]
        ],
        0.6,
        [data_class[i + "_response_ratio"] for i in list(set(data))],
        color="red",
        label="UnInterested Ratio",
    )
    ax1.set_title("Bar Chart " + str_header)
    ax1.set_ylabel("Percentage")
    ax1.set_xticks(xlocs)
    ax1.set_xticklabels(list(set(data)))
    ax1.legend(bbox_to_anchor=(0.98, 1.02))

    # Draw Pie

    ax2.pie(
        [data_class[i + "_response"] for i in list(set(data))] +
        [data_class[i] - data_class[i + "_response"] for i in list(set(data))],
        labels=[i + "_Interested" for i in list(set(data))] +
        [i + "_UnInterested" for i in list(set(data))],
        autopct="%.2f%%",
        startangle=90,
    )
    ax2.set_title("Pie Chart " + str_header)
    ax2.axis("equal")
    ax2.legend(loc="lower right")
    fig.suptitle(str_header + "_" + save_name + ".png", fontweight="bold")

    plt.savefig("./AI/AI_in_chem/homework2/" + str_header + "_" + save_name +
                ".png",
                bbox_inches="tight")
    plt.close("all")


# Dig boxfeature
def boxfeature(boxplt_name, plt_num=0):
    yquarter_down = boxplt_name['whiskers'][0 + plt_num * 2].get_xydata()[0][1]
    yquarter_up = boxplt_name['whiskers'][1 + plt_num * 2].get_xydata()[0][1]
    ymin = boxplt_name['caps'][0 + plt_num * 2].get_xydata()[0][1]
    ymax = boxplt_name['caps'][1 + plt_num * 2].get_xydata()[0][1]
    ymedian = boxplt_name['medians'][0 + plt_num].get_xydata()[0][1]
    ymean = boxplt_name['means'][0 + plt_num].get_xydata()[0][1]
    print(yquarter_down, yquarter_up, ymin, ymax, ymedian, ymean)
    return yquarter_down, yquarter_up, ymin, ymax, ymedian, ymean


# Draw Boxplot Chart
def draw_data_boxplot(str_header, list_data_name, save_name=""):
    data = [str(i) for i in list_data_name[str_header].values.tolist()]
    data_interested = []
    data_uninterested = []
    response = list_data_name["Response"].values.tolist()
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
    for i in [0, 1]:
        quarter_down, quarter_up, min, max, median, mean = boxfeature(bp, i)
        print(quarter_down, quarter_up, min, max, median, mean)
        for j in [quarter_down, quarter_up, min, max, median, mean]:
            plt.text(1.2 + i,
                     j,
                     '%.2f' % j,
                     verticalalignment='center',
                     fontsize=10,
                     backgroundcolor="white")

    plt.xlabel("Data Labels")
    plt.ylabel("Values")
    plt.suptitle(str_header + "_" + save_name + ".png", fontweight="bold")
    plt.savefig("./AI/AI_in_chem/homework2/" + str_header + "_" + save_name +
                ".png",
                bbox_inches="tight")


draw_data_bar_pie("Gender", train_data_valid, "train")
draw_data_bar_pie("Vehicle_Age", train_data_valid, "train")
draw_data_bar_pie("Previously_Insured", train_data_valid, "train")
draw_data_bar_pie("Vehicle_Damage", train_data_valid, "train")

draw_data_bar_pie("Gender", test_split_data, "test")
draw_data_bar_pie("Vehicle_Age", test_split_data, "test")
draw_data_bar_pie("Previously_Insured", test_split_data, "test")
draw_data_bar_pie("Vehicle_Damage", test_split_data, "test")

draw_data_boxplot("Age", train_data_valid, "train")
draw_data_boxplot("Annual_Premium", train_data_valid, "train")

draw_data_boxplot("Age", test_split_data, "test")
draw_data_boxplot("Annual_Premium", test_split_data, "test")