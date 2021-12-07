import matplotlib.pyplot as plt
import numpy as np
from matplotlib import offsetbox
from sklearn import cluster, datasets, manifold, metrics, random_projection
from sklearn.preprocessing import MinMaxScaler

NCLASS = 10
# Color for each category
category_colors = plt.get_cmap('tab10')(np.linspace(0., 1., NCLASS))
digit_styles = {'weight': 'bold', 'size': 8}


def plot2D(X,
           labels,
           images,
           title="",
           save="./AI/AI_in_chem/homework4/2D-plot.png"):

    fig = plt.figure(figsize=(6, 6), dpi=120)
    ax = fig.add_subplot(1, 1, 1)
    X_std = MinMaxScaler().fit_transform(X)
    for xy, l in zip(X_std, labels):
        ax.text(*xy, str(l), color=category_colors[l], **digit_styles)
    image_locs = np.ones((1, 2), dtype=float)
    image_locs = np.ones((1, 2), dtype=float)
    for xy, img in zip(X_std, images):
        dist = np.sqrt(np.sum(np.power(image_locs - xy, 2), axis=1))
        if np.min(dist) < .05:
            continue
        thumbnail = offsetbox.OffsetImage(img, zoom=.8, cmap=plt.cm.gray_r)
        imagebox = offsetbox.AnnotationBbox(thumbnail, xy)
        ax.add_artist(imagebox)
        image_locs = np.vstack([image_locs, xy])

    ax.set_xticks([])
    ax.set_yticks([])
    plt.title(title)
    plt.tight_layout()
    plt.savefig(save)


def plot3D(X, labels, title="", save="./3D-plot.png"):
    fig = plt.figure(figsize=(6, 6), dpi=120)
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    X_std = MinMaxScaler().fit_transform(X)
    for xy, l in zip(X_std, labels):
        ax.text(*xy, str(l), color=category_colors[l], **digit_styles)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(save)


# Load digits dataset from scikit-learn
digits = datasets.load_digits(n_class=NCLASS)
# Pixel data from dataset
X = digits.data
# Project X to 2 random components
RP = random_projection.SparseRandomProjection(n_components=2,
                                              random_state=114514)
X_projected = RP.fit_transform(X)
# Labels: digits.target
# Images: digits.images
plot2D(X_projected, digits.target, digits.images, title="Random Projection")