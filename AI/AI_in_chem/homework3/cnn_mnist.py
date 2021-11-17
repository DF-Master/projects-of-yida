import torch
import torchvision
from torch.autograd import Variable
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import cv2
import os
import matplotlib.pyplot as plt
from torch.utils.data import random_split
from torch import nn
import torch.nn.functional as F
from torch.optim import Adam
import numpy as np

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

# Build DataLoader Object
trainloader = DataLoader(trainset, batch_size, shuffle=True, drop_last=True)
valloader = DataLoader(valset, batch_size, shuffle=True, drop_last=True)
testloader = DataLoader(testset, batch_size, shuffle=True, drop_last=True)

# Image Visualizing Using CV2
# images, lables = next(iter(trainloader))
# img = torchvision.utils.make_grid(images, nrow=10)
# img = img.numpy().transpose(1, 2, 0)
# cv2.imshow('img', img)
# cv2.waitKey(0)


class CNNModel(nn.Module):
    def __init__(self, conv1c, conv2c, conv1k, conv2k, fc1, fc2, batchnorm,
                 dropout):
        super(CNNModel, self).__init__()

        self.conv1 = nn.Conv2d(1, conv1c, kernel_size=(conv1k, conv1k))
        self.conv2 = nn.Conv2d(conv1c, conv2c, kernel_size=(conv2k, conv2k))

        self.pool = nn.MaxPool2d(kernel_size=2)
        self.dropout = nn.Dropout(p=dropout)

        self.batchnorm = batchnorm
        if batchnorm:
            self.bn1 = nn.BatchNorm2d(conv1c)
            self.bn2 = nn.BatchNorm2d(conv2c)

        final_size = ((28 - conv1k + 1) // 2 - conv2k + 1) // 2
        self.fc1 = nn.Linear(conv2c * final_size * final_size, fc1)
        self.fc2 = nn.Linear(fc1, fc2)

    def forward(self, x):
        # x: [batch_size, 1, 28, 28], assume conv1k=5 and conv2k=3
        out = self.conv1(x)  # [batch_size, conv1c, 24, 24]
        out = F.relu(self.pool(out))  # [batch_size, conv1c, 12, 12]
        if self.batchnorm:
            out = self.bn1(out)  # [batch_size, conv1c, 12, 12]
        out = self.conv2(out)  # [batch_size, conv2c, 10, 10]
        out = F.relu(self.pool(out))  # [batch_size, conv2c, 5, 5]

        if self.batchnorm:
            out = self.bn2(out)  # [batch_size, conv2c, 5, 5]
        out = out.reshape(out.shape[0], -1)  # [batch_size, conv2c*25]
        out = F.relu(self.fc1(out))  # [batch_size, fc1]
        out = self.dropout(out)
        out = F.log_softmax(self.fc2(out), dim=1)  # [batch_size, fc2]
        return out


model_cnn = CNNModel(conv1c, conv2c, conv1k, conv2k, fc1, fc2, batchnorm,
                     dropout)


# Model training and evaluation
@torch.no_grad()
def evaluation(model, evalloader):
    conf_mat = np.zeros((10, 10))
    model.eval()
    misclassified = []
    predicts = []
    numT = 0
    numF = 0
    for i, x in enumerate(evalloader):
        image, label = x
        pred = torch.argmax(model(image), dim=1)
        _T = torch.sum(pred == label).item()
        numT += _T
        numF += len(label) - _T
        for j in range(len(label)):
            conf_mat[label[j], pred[j]] += 1
            if label[j] != pred[j]:
                misclassified.append((image[j], label[j], pred[j]))
            predicts.append(pred[j])

    model.train()
    return numT / (numT + numF), conf_mat, misclassified, predicts


def fit(model, trainloader, valloader, lr, weight_decay, max_epoch=10):
    train_batch_losses = []
    val_acc = []

    loss_fn = nn.NLLLoss(reduction="mean")
    optimizer = Adam(model.parameters(), lr=lr,
                     weight_decay=weight_decay)  # Using Adam optimizer
    batches_per_epoch = len(trainloader)

    for epoch in range(max_epoch):
        epoch_loss = 0
        for i, x in enumerate(trainloader):
            optimizer.zero_grad()
            image, label = x
            pred = model(image)
            loss = loss_fn(pred, label)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
            train_batch_losses.append(
                (epoch * batches_per_epoch + i, loss.item()))

            if (i % 200 == 0):
                print("Epoch %d, Batch %d loss: %f" % (epoch, i, loss.item()))
                acc, _cm, _mis, _pred = evaluation(model, valloader)
                val_acc.append((epoch * batches_per_epoch + i, acc))
                print("   Accuracy after epoch %d batch %d: %f" %
                      (epoch, i, acc))
        print("\n##### Epoch %d average loss: " % epoch,
              epoch_loss / batches_per_epoch, ' #####\n')
    return train_batch_losses, val_acc


print("Training CNN Model.")
model_cnn.train()
train_losses_cnn, val_acc_cnn = fit(model_cnn,
                                    trainloader,
                                    valloader,
                                    lr=lr,
                                    weight_decay=weight_decay,
                                    max_epoch=3)
