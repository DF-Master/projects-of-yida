import matplotlib.pyplot as plt
import matplotlib.collections as mcol
from matplotlib.legend_handler import HandlerLineCollection, HandlerTuple
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd
import csv

def load_data(max=30):
    reader = pd.read_csv("C:/Users/jiang/Documents/GitHub/projects-of-yida/temp control/datalog.csv")
    readerlist = reader.values.tolist()
    if len(readerlist)> max:
        readerlist= reader.tail(max).values.tolist()
    return readerlist

print(type(load_data()))





        self.texttempset.setText(DetectSet())
       # self.KP.setText(DetectSet('0004'))