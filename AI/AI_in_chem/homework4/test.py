# Ref: https://moonbooks.org/Articles/How-to-create-a-scatter-plot-with-several-colors-in-matplotlib-/
import matplotlib.pyplot as plt
import numpy as np

X = [[0, 1], [1, 2], [2, 3], [3, 4]]
X = np.array(X)

y = np.array([0, 0, 1, 2])

myCmap = np.array(['r', 'g', 'b'])
myLabelMap = np.array(['car', 'bicycle', 'plane'])

y_unique, id_unique = unique(y, return_index=True)
X_unique = X[id_unique]
X = asarray(X, dtype=float)

for j, yj in enumerate(y_unique):
    plt.scatter(X_unique[j, 0],
                X_unique[j, 1],
                color=myCmap[yj],
                label=myLabelMap[yj])

X[id_unique] = nan
plt.scatter(X[:, 0], X[:, 1], color=myCmap[y])

plt.legend(loc='upper right')

plt.show()