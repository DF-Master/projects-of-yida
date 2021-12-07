from matplotlib import scale
import matplotlib.pyplot as plt
import numpy as np
from sklearn import cluster, datasets, manifold, metrics, random_projection
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# prepare data
digits = datasets.load_digits(
)  # digits datasets. a dict. 2 important keys: 'dat
print(digits.keys())
print("Dataset size: ", digits['data'].shape, digits['target'].shape)

# visualize the first 10 samples
# # for i in range(10):
# #     img = digits['data'][i].reshape(8, 8)
# #     label = digits['target'][i]
# #     plt.subplot(2, 5, i + 1)
# #     plt.imshow(img)
# #     plt.title("Label: " + str(label))

# plt.show()

### standarization
# digits_feature_mean = digits['data'].mean(axis=0)
# # print(digits_feature_mean.shape)
# digits_feature_sd = digits['data'].std(axis=0)
# # print(digits_feature_sd.shape)
# digits_data_std = (digits['data'] - digits_feature_mean) / digits_feature_sd

# print(digits_data_std.shape, digits_data_std[1])
# # print(digits_data_std.mean(axis=0), digits_data_std.std(axis=0))
# ### drop the nan features
# digits_data_std = digits_data_std[:, ~np.isnan(digits_data_std.sum(axis=0))]
# print(digits_data_std.shape)

### you can also perform this transformation with sklearn.preprocessing.StandardScaler()
from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler().fit(digits['data'])
# _data_std = scaler.transform(digits['data'])
_data_std = StandardScaler().fit_transform(digits['data'])
print(_data_std.mean(axis=0), _data_std.std(axis=0))
### By default, sklearn will avoid "divided by zero" and return zeros instead of "nan"
