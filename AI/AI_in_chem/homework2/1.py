import numpy as np
import matplotlib as plt
import pandas as pd


# Open data
train_data = pd.read_csv('./AI/AI_in_chem/homework2/train.csv',header = 0,sep=',')
test_data = pd.read_csv('./AI/AI_in_chem/homework2/test.csv',header = 0,sep=',')

print(set(train_data["Response"].values.tolist()))
# print(train_data)
# print(type[train_data])

# Draw data bar chart and pie chart 
def draw_data_bar_pie(str_header):
    data = train_data["Gender"].values.tolist()
    data_class = set(data)
    response = train_data["Response"].values.tolist()
    response_class = set(response)