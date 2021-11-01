import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import shape
import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import pearsonr
from sklearn.linear_model import LogisticRegression

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


def digfeature(i, name=""):
    i.replace('Male', 0, inplace=True)
    i.replace('Female', 1, inplace=True)
    i.replace('Yes', 1, inplace=True)
    i.replace('No', 0, inplace=True)
    i.replace('< 1 Year', 0, inplace=True)
    i.replace('1-2 Year', 1, inplace=True)
    i.replace('> 2 Years', 2, inplace=True)

    ## Normalize
    mm = MinMaxScaler()
    i = np.delete(mm.fit_transform(i), [0], axis=1)  # delete ip list
    i = i[:, i.var(axis=0) > 0.01]

    # Pearson
    print("feature shape == " + str(i.shape[1]))

    nfeature = i.shape[1]
    corrmat = np.ones((nfeature, nfeature), dtype=float)
    for x in range(nfeature):
        for y in range(x + 1, nfeature):
            corrmat[y, x] = corrmat[x, y] = pearsonr(i[:, x], i[:, y])[0]

    # Display Pearson correlation coefficient matrix with color bar

    plt.figure(figsize=(4, 3), dpi=120)
    plt.matshow(corrmat)
    plt.colorbar()
    # plt.show()
    plt.savefig("./AI/AI_in_chem/homework2/" + name + "_pearsonfeature.png",
                bbox_inches="tight")
    plt.close("all")

    #根据方差（阈值为归一化后0.01），去掉Annual_Premium与Driving_License项目，再根据实际意义去掉ID项。根据Pearson结果，可以看出2（Region_Code）和7（Vintage）对8（Response）二者可能是独立的

    i = np.delete(i, [2, 7], axis=1)
    print("after pearson feature shape == " + str(i.shape[1]))

    return i


def module_Regression(solver="lbfgs",
                      penalty="l2",
                      C=1.0,
                      class_weight="balanced",
                      data=train_split_data):
    model = LogisticRegression(solver=solver,
                               penalty=penalty,
                               C=C,
                               class_weight=class_weight)
    model.fit(train_split_data[:, :-1], train_split_data[:, -1])
    # Plot the decision boundary
    b = .5  # Padding length in the boundary
    h = .02  # Step size in t.he mesh grid


train_split_data = digfeature(train_split_data, "train_split_data")

# print(train_split_data[:, :-1])
# print(train_split_data[:, -1])
module_Regression()
