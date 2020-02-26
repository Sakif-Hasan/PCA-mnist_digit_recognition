import pandas as pd
import matplotlib as plot

from sklearn import svm
from sklearn.metrics import accuracy_score

dataframe = pd.read_csv('X:\Datasets\mnist_784.csv')

print(len(dataframe) #70,000

classifier = svm.SVC(gamma = 'scale' , C = 100)

# equally divide into test data and train data (35000 each)

x,y = dataframe[],dataframe