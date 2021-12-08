import matplotlib.pyplot as plt
import numpy as np
from sklearn import cluster, datasets, manifold, metrics, random_projection
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from matplotlib.axes._axes import _log as matplotlib_axes_logger
from sklearn.metrics import silhouette_score


def tanimoto_similarity(x, y):
    return np.dot(x, y) / (np.linalg.norm(x, ord=2)**2 +
                           np.linalg.norm(y, ord=2)**2 - np.dot(x, y))


def cosine_similarity(x, y):
    return np.dot(x, y) / (np.linalg.norm(x, ord=2) * np.linalg.norm(y, ord=2))


def dice_similarity(x, y):
    return 2 * np.dot(
        x, y) / (np.linalg.norm(x, ord=1) + np.linalg.norm(y, ord=1))


# Read Data
zinc_fp = np.array(
    pd.read_csv("AI\AI_in_chem\homework4\zinc_fp.csv", index_col=0))
zinc_SMILES = np.array(
    pd.read_csv("AI\AI_in_chem\homework4\zinc_SMILES.csv", index_col=0))


def tsne(metric='euclidean', dim=2):
    global x_tsne_2, kmeans_before, kmeans_after_tsne
    # tSNE to 2D
    tsne = manifold.TSNE(n_components=dim, metric=metric)
    x_tsne_2 = tsne.fit_transform(zinc_fp)
    print("x_tsne_2 Shape:", x_tsne_2.shape)

    # KMeans clustering (No Dim Red)
    kmeans_before = cluster.KMeans(n_clusters=10, random_state=0).fit(zinc_fp)
    # kmeans_after_pca = cluster.KMeans(n_clusters=10, random_state=0).fit(x_pca_2)
    kmeans_after_tsne = cluster.KMeans(n_clusters=10,
                                       random_state=0).fit(x_tsne_2)


# Visualization (using pyplot)
def vistualization(target, c=zinc_fp, name=''):
    category_colors = plt.get_cmap('tab10')(np.linspace(0., 1., 10))

    plt.figure(figsize=(6, 6), dpi=120)
    plt.xlabel('PC1')
    plt.xlabel('PC2')
    plt.title("2- " + name + "-Result")

    scatter = plt.scatter(target[:, 0], target[:, 1], c=c, cmap='tab10')
    plt.legend(*scatter.legend_elements(), loc="best", title="Classes")
    plt.savefig(".\\AI\\AI_in_chem\\homework4\\2-" + name + ".png")

    plt.close('All')
    print("silhouette_score After" + name,
          silhouette_score(x_pca_2, kmeans_after_tsne.labels_))
    print('Center Position: ', "\n", kmeans_after_tsne.cluster_centers_)
    print("Labels: ", kmeans_after_tsne.labels_)


tsne(metric=cosine_similarity, dim=2)
vistualization(x_tsne_2,
               c=kmeans_after_tsne.labels_,
               name='cosine_similarity_2Dim')
tsne(metric=cosine_similarity, dim=3)
vistualization(x_tsne_2,
               c=kmeans_after_tsne.labels_,
               name='cosine_similarity_3Dim')
tsne(metric=cosine_similarity, dim=4)
vistualization(x_tsne_2,
               c=kmeans_after_tsne.labels_,
               name='cosine_similarity_4Dim')
