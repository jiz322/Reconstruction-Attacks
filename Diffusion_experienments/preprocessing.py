# To use this file, just import the data and target
import numpy as np
import matplotlib.pyplot as plt
import torch
# data from https://www.kaggle.com/code/serkanpeldek/face-recognition-on-olivetti-dataset/notebook
data=np.load("./data/olivetti_faces.npy")
target=np.load("./data/olivetti_faces_target.npy")

avg=0.5470424729887565
std=0.17251527
# normalize data
data = (data-avg)/std

from collections import Counter
# Counter(target)
def show_picture_and_label(data, targets, i):
    f = plt.figure()
    plt.imshow(data[i],cmap='gray')
    plt.show()
    print("label is: ", targets[i])

tup = np.array(list(zip(data, target)),dtype=object)
np.random.seed(10)
np.random.shuffle(tup)
train_data, train_target = zip(*tup)

# train_data: tuple of length 400, each is a matrix represents a picture
# train_target: tuple of length 400, each is a label


train_data = torch.tensor(train_data)
train_target = torch.tensor(train_target)

# Since the dataset is small, we assumed batch size = 1
train_data = train_data.reshape(400,1,1,64,64).detach()

# input tensor, output picture
def tensor_to_picture(data):
    f = plt.figure()
    plt.imshow(data,cmap='gray')
    plt.show()
    
# input target, output picture
def label_to_picture(target):
    f = plt.figure()
    for i in range(400):
        if train_target[i] == target:           
            plt.imshow(train_data[i][0][0],cmap='gray')
            plt.show()
            break

    