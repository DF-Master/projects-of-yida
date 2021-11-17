import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import shape
import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import pearsonr
from sklearn.linear_model import LogisticRegression
import csv
from sklearn import metrics

# Open data
train_data_valid = pd.read_csv("./AI/AI_in_chem/homework2/train.csv",
                               header=0,
                               sep=",")

for i in [train_data_valid]:
    i.replace('Male', 0, inplace=True)
    i.replace('Female', 1, inplace=True)
    i.replace('Yes', 1, inplace=True)
    i.replace('No', 0, inplace=True)
    i.replace('< 1 Year', 0, inplace=True)
    i.replace('1-2 Year', 1, inplace=True)
    i.replace('> 2 Years', 2, inplace=True)

# Split Data
train_split_data, test_split_data = train_test_split(train_data_valid,
                                                     test_size=0.25,
                                                     shuffle=True)

with open("./AI/AI_in_chem/homework2/train_split_data.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(train_split_data.values.tolist())
with open("./AI/AI_in_chem/homework2/test_split_data.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(test_split_data.values.tolist())
print(f"""train_split_data Shape = {train_split_data.shape}
test_split_data = {test_split_data.shape}""")

# get better constant
data_list = []


# Digfeature
def digfeature(i, name=""):
    global test_split_data

    ## Normalize
    mm = MinMaxScaler()
    i = np.delete(mm.fit_transform(i), [0], axis=1)  # delete ip list
    test_split_data = np.delete(mm.fit_transform(test_split_data), [0], axis=1)
    i = i[:, i.var(axis=0) > 0.01]
    test_split_data = test_split_data[:, test_split_data.var(axis=0) > 0.01]

    # Pearson
    print("feature shape == " + str(i.shape[1] - 1))

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
    test_split_data = np.delete(test_split_data, [2, 7], axis=1)
    print("after pearson feature shape == " + str(i.shape[1] - 1))

    return i


def module_Regression(solver="lbfgs",
                      penalty="l2",
                      C=1.0,
                      class_weight="balanced",
                      train_data=train_split_data,
                      test_data=test_split_data):
    global data_list
    model = LogisticRegression(solver=solver,
                               penalty=penalty,
                               C=C,
                               class_weight=class_weight)
    train_data = np.asarray(train_data)
    model.fit(train_data[:, :-1], train_data[:, -1])
    Z_predict_test = model.predict(test_data[:, :-1])
    Z_predict_train = model.predict(train_data[:, :-1])

    for z in [test_data, train_data]:
        cm = metrics.confusion_matrix(z[:, -1], model.predict(z[:, :-1]))
        acc = metrics.accuracy_score(z[:, -1], model.predict(z[:, :-1]))
        recall = metrics.recall_score(z[:, -1], model.predict(z[:, :-1]))
        precision = metrics.precision_score(z[:, -1], model.predict(z[:, :-1]))
        f1 = metrics.f1_score(z[:, -1], model.predict(z[:, :-1]))
        auc = metrics.roc_auc_score(z[:, -1], model.predict(z[:, :-1]))
        print(f"""Confusion Matrix
        {cm}
        Accuracy = {acc:>.3f}
        Precision = {precision:>.3f}
        Recall = {recall:>.3f}
        F1 = {f1:>.3f}
        AUC = {auc:>.3f}""")

        data_list.append([
            solver, penalty, C,
            f"""Accuracy = {acc:>.3f},Precision = {precision:>.3f},Recall = {recall:>.3f},F1 = {f1:>.3f},AUC = {auc:>.3f}"""
        ])


# Plot the decision boundary

# b = .02  # Padding length in the boundary
# h = .05  # Step size in t.he mesh grid
# aa, bb, cc, dd, ee, ff = np.meshgrid(np.arange(0 - b, 1 + b, h),
#                                      np.arange(0 - b, 1 + b, h),
#                                      np.arange(0 - b, 1 + b, h),
#                                      np.arange(0 - b, 1 + b, h),
#                                      np.arange(0 - b, 1 + b, h),
#                                      np.arange(0 - b, 1 + b, h))
# Z = model.predict(np.c_[aa.ravel(),
#                         bb.ravel(),
#                         cc.ravel(),
#                         dd.ravel(),
#                         ee.ravel(),
#                         ff.ravel()]).reshape(
#                             aa.shape)  # Prediction in mesh grid
# plt.figure(figsize=(6, 4.5), dpi=120)
# # print(Z[:, :, 0, 0, 0, 0], Z[:, :, 0, 0, 0, 0].shape)
# print(Z)
# plt.pcolormesh(ff[0, :, 0, 0, 0, :],
#                bb[0, :, 0, 0, 0, :],
#                Z[0, :, 0, 0, 0, :],
#                shading="auto",
#                cmap=plt.cm.Wistia)  # Plot mesh grid with color map
# plt.scatter(data[:, 5],
#             data[:, 1],
#             c=data[:, -1],
#             edgecolor="black",
#             cmap=plt.cm.Wistia)  # Plot points in dataset
# plt.xlabel(
#     "Radius")  # Mean of distances from center to points on the perimeter
# plt.ylabel("Texture")  # Standard deviation of gray-scale values
# plt.xlim(-0.05, 1.05)
# plt.ylim(-0.05, 1.05)
# plt.show()

train_split_data = digfeature(train_split_data, "train_split_data")
print(test_split_data.shape)

for solver_choice in ['newton-cg', 'sag', 'saga', 'lbfgs']:
    for penalty_choice in ['l2', 'l1', 'elasticnet']:
        for c_choice in [2**i for i in range(-5, 5)]:
            try:
                module_Regression(solver=solver_choice,
                                  penalty=penalty_choice,
                                  C=c_choice,
                                  train_data=train_split_data,
                                  test_data=test_split_data)
            except:
                data_list.append([solver_choice, penalty_choice, 'Fail'])

# module_Regression(train_data=train_split_data, test_data=test_split_data)

with open("./AI/AI_in_chem/homework2/save_data_list.csv",
          "w") as save_data_list:
    writer = csv.writer(save_data_list)
    writer.writerows(data_list)