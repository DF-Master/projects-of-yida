import torch
import torchvision
from torch.autograd import Variable
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import cv2
import os
import matplotlib.pyplot as plt
from torch.utils.data import random_split

# Download MNIST dataset (or load the directly if you have already downloaded them previously)
if os.path.exists("./AI/AI_in_chem/homework3/data/MNIST"):
    _dl = False
else:
    _dl = True

transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize((0.1307, ), (0.3081, ))
])

trainset_all = torchvision.datasets.MNIST('./AI/AI_in_chem/homework3/data',
                                          train=True,
                                          download=_dl,
                                          transform=transform)
testset = torchvision.datasets.MNIST('./AI/AI_in_chem/homework3/data',
                                     train=False,
                                     download=_dl,
                                     transform=transform)

samples = []
print("trainset size: ", len(trainset_all))
print("testset size: ", len(testset))

# show information of the first 10 samples in the training dataset
# for i, x in enumerate(trainset_all):
#     if len(samples) >= 20:
#         break
#     print("Shape (Channel, X, Y): ", x[0].shape, "    Label: ", x[1])
#     samples.append((x[0].squeeze(), x[1]))

# Visualizing the first 20 samples
# plt.figure(figsize=(10, 3))
# for i in range(20):
#     plt.subplot(2, 10, i + 1)
#     plt.imshow(samples[i][0], cmap='gray', interpolation='none')
#     plt.title("Label: " + str(samples[i][1]))
#     plt.axis('off')
# plt.show()

# Train-Validation-Test split
SEED = 114514
valid_size = 10000
train_size = len(trainset_all) - valid_size
trainset, valset = random_split(trainset_all, [train_size, valid_size],
                                generator=torch.Generator().manual_seed(SEED))

print("Trainset size: ", len(trainset))
print("Validation set size: ", len(valset))

# hyperparameters
batch_size = 32

# for CNN model (conv2d x2 + fc x2)
conv1c = 16
conv2c = 32
conv1k = 5
conv2k = 3
fc1 = 128
fc2 = 10
batchnorm = True
dropout = 0.1

# for training
lr = 0.001
weight_decay = 1e-5