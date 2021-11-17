import torch
from torch.nn.modules import module
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
import pandas as pd
import csv

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
            predicts.append([int(label[j]), int(pred[j])])

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


def Model_Evaluation(model):
    CNN_val_acc, CNN_val_cm, CNN_val_mis, CNN_val_pred = evaluation(
        model, valloader)
    CNN_val_cm = pd.DataFrame(CNN_val_cm, dtype=int)
    print("CNN Validation Accuracy: ", CNN_val_acc)
    print("CNN Validation Confusion Matrix: \n", CNN_val_cm)
    return CNN_val_acc, CNN_val_cm, CNN_val_mis, CNN_val_pred


if __name__ == '__main__':
    # Train-Validation-Test split
    SEED = 114514
    valid_size = 10000
    train_size = len(trainset_all) - valid_size
    trainset, valset = random_split(
        trainset_all, [train_size, valid_size],
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
    max_epoch = 3

    # Build DataLoader Object
    trainloader = DataLoader(trainset,
                             batch_size,
                             shuffle=True,
                             drop_last=True)
    valloader = DataLoader(valset, batch_size, shuffle=True, drop_last=True)
    testloader = DataLoader(testset, batch_size, shuffle=True, drop_last=True)

    # Train Model
    ## Save header of constant
    # with open("./AI/AI_in_chem/homework3/data_modify.csv", "w") as csv_file:
    #     writer = csv.writer(csv_file)
    #     writer.writerow([
    #         "conv1c", "conv2c", "conv1k", "conv2k", "fc1", "fc2", "batchnorm",
    #         "dropout", "lr", "weight_decay", "max_epoch", "Accuracy", "Loss"
    #     ])

    print("Training CNN Model.")

    model_cnn = CNNModel(conv1c, conv2c, conv1k, conv2k, fc1, fc2, batchnorm,
                         dropout)

    model_cnn.train()
    train_losses_cnn, val_acc_cnn = fit(model_cnn,
                                        trainloader,
                                        valloader,
                                        lr=lr,
                                        weight_decay=weight_decay,
                                        max_epoch=max_epoch)
    CNN_val_acc_save, CNN_val_cm_save, CNN_val_mis_save, CNN_val_pred_save = Model_Evaluation(
        model_cnn)

    print("*** Use Model on Test Data ***")
    acc_test, conf_mat_test, misclassified_test, predicts_test = evaluation(
        model_cnn, testloader)
    print("Accuracy: " + str(acc_test))
    print("Misclassified_test\n", pd.DataFrame(conf_mat_test, dtype=int))
    print(predicts_test)
    with open("./AI/AI_in_chem/homework3/mnist_test_prediction.csv",
              "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(predicts_test)

    # Save Models
    os.makedirs("./AI/AI_in_chem/homework3/checkpoints", exist_ok=True)
    # save parameters only
    torch.save(model_cnn.state_dict(),
               "./AI/AI_in_chem/homework3/checkpoints/model_cnn.pt")

# Save Constant
# with open("./AI/AI_in_chem/homework3/data_modify.csv",
#             "a") as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow([
#         float(i) for i in [
#             conv1c, conv2c, conv1k, conv2k, fc1, fc2,
#             batchnorm, dropout, lr, weight_decay,
#             max_epoch, CNN_val_acc_save,
#             train_losses_cnn[-1][-1]
#         ]
#     ])

# input
path = "./AI\AI_in_chem\homework3\handwritten"
images_path = os.listdir(path)
images = []

for i in images_path:
    label = int(i.split('_')[1].split('.')[0])
    image = torchvision.io.read_image(os.path.join(path, i)).float()[0:3, :, :]
    image = image.mean(dim=0).unsqueeze(0)
    images.append((image, label))

_values = torch.concat([i for i, j in images]).reshape(-1)
_mean = _values.mean().item()
_sd = _values.std().item()
print("Mean: ", _mean, "  Std:", _sd)
mytransform = torchvision.transforms.Normalize((_mean), (_sd))
# mytransform = torchvision.transforms.Normalize((0.1307,), (0.3081,))

for i in range(len(images)):
    img = mytransform(images[i][0])
    images[i] = (img, images[i][1])

from torch.utils.data import Dataset


class mySet(Dataset):
    def __init__(self, images):
        super(mySet, self).__init__()
        self.data = images

    def __getitem__(self, x):
        return self.data[x]

    def __len__(self):
        return len(self.data)


myevalset = mySet(images)
print("My dataset size: ", len(myevalset))

myloader = DataLoader(mySet(images),
                      shuffle=False,
                      drop_last=False,
                      batch_size=batch_size)
myacc, mycm, mymis, mypred = evaluation(model_cnn, myloader)

print("Accuracy on custom dataset: ", myacc)

print("Visualizing custom samples")
plt.figure()
for i in range(len(myevalset)):
    img, label = myevalset[i]
    pred = mypred[i][-1]
    img = img.squeeze()
    plt.subplot(2, 5, i + 1)
    plt.imshow(img, cmap='gray', interpolation='none')
    plt.title("Label: " + str(label) + "\nPredict: " + str(pred))
    plt.axis('off')
plt.show()