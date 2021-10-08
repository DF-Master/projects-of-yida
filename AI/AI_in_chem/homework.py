# Imports
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
import pandas as pd

# Open data
train_data = pd.read_table('./AI/AI_in_chem/train.dat',sep=" ").values.tolist()
test_data = pd.read_table('./AI/AI_in_chem/test.dat',sep=" ").values.tolist() # type - list

x = np.array([row[0] for row in train_data] )
y = np.array([row[1] for row in train_data] )