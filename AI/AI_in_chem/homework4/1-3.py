import matplotlib.pyplot as plt
import numpy as np
from sklearn import cluster, datasets, manifold, metrics, random_projection
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from matplotlib.axes._axes import _log as matplotlib_axes_logger
# Stop printing small error
matplotlib_axes_logger.setLevel('ERROR')

# prepare data
digits = datasets.load_digits()
# digits datasets. a dict. 2 important keys: 'dat
print("Data keys: ", digits.keys())
print("Dataset size: ", digits['data'].shape, "\n", "Target size: ",
      digits['target'].shape)

### you can also perform this transformation with sklearn.preprocessing.StandardScaler()
_data_std = StandardScaler().fit_transform(digits['data'])
### By default, sklearn will avoid "divided by zero" and return zeros instead of "nan"

# PCA to 2D
pca = PCA()
x_pca_2 = pca.fit_transform(digits['data'])[:, 0:2]
print("x_pca_2 Shape:", x_pca_2.shape)

# tSNE to 2D
tsne = manifold.TSNE(n_components=2)
x_tsne_2 = tsne.fit_transform(digits['data'])
print(x_tsne_2.shape)


# Visualization (using pyplot)
def vistualization(target, c=digits['target'], name=''):
    category_colors = plt.get_cmap('tab10')(np.linspace(0., 1., 10))

    plt.figure(figsize=(6, 6), dpi=120)
    plt.xlabel('PC1')
    plt.xlabel('PC2')
    plt.title("1-3 " + name + "Result")

    scatter = plt.scatter(target[:, 0], target[:, 1], c=c, cmap='tab10')
    plt.legend(*scatter.legend_elements(), loc="best", title="Classes")
    plt.savefig(".\\AI\\AI_in_chem\\homework4\\1-3-" + name + ".png")

    plt.close('All')


# KMeans clustering (No Dim Red)
kmeans_before = cluster.KMeans(n_clusters=10,
                               random_state=0).fit(digits['data'])
kmeans_after_pca = cluster.KMeans(n_clusters=10, random_state=0).fit(x_pca_2)
kmeans_after_tsne = cluster.KMeans(n_clusters=10, random_state=0).fit(x_tsne_2)

vistualization(x_pca_2, name="PCA")
vistualization(x_pca_2, c=kmeans_before.labels_, name="KMEANS-before-PCA")
vistualization(x_pca_2, c=kmeans_after_pca.labels_, name="KMEANS-after-PCA")
vistualization(x_tsne_2, name="TSNE")
vistualization(x_tsne_2, c=kmeans_before.labels_, name="KMEANS-before-TSNE")
vistualization(x_tsne_2, c=kmeans_after_tsne.labels_, name="KMEANS-after-TSNE")