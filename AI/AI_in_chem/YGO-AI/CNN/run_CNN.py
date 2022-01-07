import torch
import torchvision
import numpy as np
import pandas as pd
from torch.utils.data import random_split
from torch.utils.data import DataLoader
import os
from torch.optim import Adam
from torch.utils.data import Dataset, DataLoader
from torch import nn
import torch.nn.functional as F
import cv2

# 模型参数
# hyperparameters
batch_size = 32

# for CNN model (conv2d x10 + fc x2)
conv1c = 16
conv2c = 32
conv3c = 64
conv4c = 128
conv5c = 256
conv6c = 128
conv7c = 64
conv8c = 32

conv1k = 3
conv2k = 3
conv3k = 3
conv4k = 3
conv5k = 3
conv6k = 3
conv7k = 3
conv8k = 3

fc1 = 2048
fc2 = 512
fc3 = 100
batchnorm = True
dropout = 0.1

# for training
lr = 0.001
weight_decay = 1e-5

# input dir
inputpath = ''

# Input Img


class CNN(nn.Module):
    def __init__(self, batchnorm=True, dropout=0.1):
        super(CNN, self).__init__()
        # layers
        self.conv1 = nn.Conv2d(3, 16, kernel_size=(3, 3), padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=(3, 3), padding=1)
        self.conv3 = nn.Conv2d(32, 64, kernel_size=(3, 3), padding=0)
        self.conv4 = nn.Conv2d(64, 128, kernel_size=(3, 3), padding=1)
        self.conv5 = nn.Conv2d(128, 256, kernel_size=(3, 3), padding=0)
        self.conv6 = nn.Conv2d(256, 128, kernel_size=(3, 3), padding=1)
        self.conv7 = nn.Conv2d(128, 64, kernel_size=(3, 3), padding=1)
        self.conv8 = nn.Conv2d(64, 32, kernel_size=(3, 3), padding=0)

        self.pool = nn.MaxPool2d(kernel_size=2)
        self.dropout = nn.Dropout(p=dropout)

        self.batchnorm = batchnorm
        if batchnorm:
            self.bn1 = nn.BatchNorm2d(16)
            self.bn2 = nn.BatchNorm2d(32)
            self.bn3 = nn.BatchNorm2d(64)
            self.bn4 = nn.BatchNorm2d(128)
            self.bn5 = nn.BatchNorm2d(256)
            self.bn6 = nn.BatchNorm2d(128)
            self.bn7 = nn.BatchNorm2d(64)
            self.bn8 = nn.BatchNorm2d(32)

        self.fc1 = nn.Linear(32 * 15 * 15, 2048)
        self.fc2 = nn.Linear(2048, 512)
        self.fc3 = nn.Linear(512, 100)

    def forward(self, x):
        # x: [batch_size, 3, 134, 134]
        # out = LAYERS(x)
        out = self.conv1(x)  # [batch_size, 16, 134, 134]
        out = F.relu(out)  # [batch_size, 16, 134, 134]
        if self.batchnorm:
            out = self.bn1(out)  # [batch_size, 16, 134, 134]

        out = self.conv2(out)  # [batch_size, 32, 134, 134]
        out = F.relu(out)  # [batch_size, 32, 134, 134]
        if self.batchnorm:
            out = self.bn2(out)  # [batch_size, 32, 134, 134]

        out = self.conv3(out)  # [batch_size, 64, 132, 132]
        out = F.relu(self.pool(out))  # [batch_size, 64, 66, 66]
        if self.batchnorm:
            out = self.bn3(out)  # [batch_size, 64, 66, 66]

        out = self.conv4(out)  # [batch_size, 128, 66, 66]
        out = F.relu(out)  # [batch_size, 128, 66, 66]
        if self.batchnorm:
            out = self.bn4(out)  # [batch_size, 128, 66, 66]

        out = self.conv5(out)  # [batch_size, 256, 64, 64]
        out = F.relu(self.pool(out))  # [batch_size, 256, 32, 32]
        if self.batchnorm:
            out = self.bn5(out)  # [batch_size, 256, 32, 32]

        out = self.conv6(out)  # [batch_size, 128, 32, 32]
        out = F.relu(out)  # [batch_size, 128, 32, 32]
        if self.batchnorm:
            out = self.bn6(out)  # [batch_size, 128, 32, 32]

        out = self.conv7(out)  # [batch_size, 64, 32, 32]
        out = F.relu(out)  # [batch_size, 64, 32, 32]
        if self.batchnorm:
            out = self.bn7(out)  # [batch_size, 64, 32, 32]

        out = self.conv8(out)  # [batch_size, 32, 30, 30]
        out = F.relu(self.pool(out))  # [batch_size, 32, 15, 15]
        if self.batchnorm:
            out = self.bn8(out)  # [batch_size, 32, 15, 15]

        out = out.reshape(out.shape[0], -1)  # [batch_size, 32*15*15]
        out = F.relu(self.fc1(out))  # [batch_size, fc1]
        out = self.dropout(out)
        out = F.relu(self.fc2(out))  # [batch_size, fc2]
        out = self.dropout(out)
        out = F.log_softmax(self.fc3(out), dim=1)  # [batch_size, fc3]
        return out

    def fit(self,
            trainloader,
            valloader,
            lr=0.001,
            weight_decay=1e-5,
            max_epoch=1,
            checkpoints_path='./checkpoints'):
        # Training Procedure
        train_batch_losses = []
        val_acc = []

        loss_fn = nn.NLLLoss(reduction='mean')
        optimizer = Adam(self.parameters(), lr=lr,
                         weight_decay=weight_decay)  # Using Adam optimizer
        batches_per_epoch = len(trainloader)

        for epoch in range(max_epoch):
            epoch_loss = 0
            for i, x in enumerate(trainloader):
                optimizer.zero_grad()
                image, label = x
                pred = self(image)
                loss = loss_fn(pred, label)
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item()
                train_batch_losses.append(
                    (epoch * batches_per_epoch + i, loss.item()))

                if (i % 200 == 0):
                    print('Epoch %d, Batch %d loss: %f' %
                          (epoch, i, loss.item()))
                    acc, _cm = self.evaluation(valloader)
                    val_acc.append((epoch * batches_per_epoch + i, acc))
                    print('   Accuracy after epoch %d batch %d: %f' %
                          (epoch, i, acc))
            print("\n##### Epoch %d average loss: " % epoch,
                  epoch_loss / batches_per_epoch, ' #####\n')
            self.save_checkpoint(checkpoints_path + '/model_cnn.pt', epoch,
                                 epoch_loss / batches_per_epoch)
        return train_batch_losses, val_acc

    @torch.no_grad()
    def evaluation(self, evalloader):
        # Evaluation Procedure
        conf_mat = np.zeros((100, 100))
        # set to evaluate mode
        self.eval()
        numT = 0
        numF = 0
        for i, x in enumerate(evalloader):
            image, label = x
            pred = torch.argmax(self(image), dim=1)
            _T = torch.sum(pred == label).item()
            numT += _T
            numF += len(label) - _T
            for j in range(len(label)):
                conf_mat[label[j], pred[j]] += 1
        # reset to train model
        self.train()
        # return accuracy, confuse matrix
        accuracy = numT / (numT + numF)
        confusion_matrix = conf_mat
        return accuracy, confusion_matrix

    def save_checkpoint(self, path, epoch, loss):
        try:
            optim_state = optimizer.state_dict()
        except:
            optim_state = None
        checkpoint = {
            "model_state_dict": self.state_dict(),
            "epoch": epoch,
            "loss": loss,
            "optimizer_state_dict": optim_state
        }
        torch.save(checkpoint, path)

    def load_checkpoint(self, path, optimizer=Adam):
        checkpoint = torch.load(path)
        self.load_state_dict(checkpoint['model_state_dict'])
        if checkpoint['optimizer_state_dict'] is not None:
            self.optimizer = optimizer(self.parameters())
            self.optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        epoch = checkpoint['epoch']
        loss = checkpoint['loss']
        return epoch, loss