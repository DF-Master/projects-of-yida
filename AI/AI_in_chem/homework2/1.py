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

# print(set(train_data["Response"].values.tolist()))
# print(train_data)
# print(type[train_data])


# Draw data bar chart and pie chart
def draw_data_bar_pie(str_header):
    data = [str(i) for i in train_data[str_header].values.tolist()]
    data_class = {}
    response = train_data["Response"].values.tolist()
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

    plt.savefig("./AI/AI_in_chem/homework2/" + str_header + ".png",
                bbox_inches="tight")
    plt.close("all")


draw_data_bar_pie("Gender")
draw_data_bar_pie("Vehicle_Age")
draw_data_bar_pie("Previously_Insured")
draw_data_bar_pie("Vehicle_Damage")
