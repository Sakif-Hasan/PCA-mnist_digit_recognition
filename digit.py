# lib
import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn import svm

# read and split data

path = r"X:/Datasets/mnist_784.csv"
dataframe = pd.read_csv(path)

print(dataframe.head(5))
