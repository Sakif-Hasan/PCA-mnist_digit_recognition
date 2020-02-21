import sklearn
import pandas as pd
import matplotlib as plot

from sklearn import svm

digits = pd.read_csv('X:\Datasets\mnist_784.csv')

#train the first 2000 images
train_x = images[:2000]
train_y = labels[:2000]