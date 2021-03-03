import matplotlib.pyplot as plt
import matplotlib.collections as mcol
from matplotlib.legend_handler import HandlerLineCollection, HandlerTuple
from matplotlib.lines import Line2D
import numpy as np
import csv

def make_plot(datafile, num=10):
    global datalineplot
    if len(datafile) > num:
        dataset = datafile[-(num+1):]
    elif len(datafile) > 1 and len(datafile[0]) == 3:
        dataset = datafile[1:]
    else:
        dataset = [['22.2', '60.0', '42:23']]
    datasetT = transpose(dataset)
    tempchangelist = datasetT[0]
    tempsetlist = datasetT[1]
    timelist = datasetT[2]
    fig = plt.figure()
    # fig.title("实时数据变化图")
    ax = fig.add_subplot()
    linetemprev = ax.plot(timelist, tempchangelist, '-g', label='Temp. Rev.')
    linetempset = ax.plot(timelist, tempsetlist, ':b')
    ax.legend((linetemprev, linetempset), ('Temp. Rev.', 'Temp. Set.'), loc='upper right', shadow=True,fancybox=True)
    ax.set_xlabel('Time')
    ax.set_ylabel('Data')
    ax.set_title('Data Live LinePlot')

    return fig


def transpose(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        matrix1 = []
        for j in range(len(matrix)):
            matrix1.append(matrix[j][i])
        new_matrix.append(matrix1)
    return new_matrix

# 制造数据表

# 形成网页UI
# 加载数据
def load_data():
    with open("C:/Users/jiang/Documents/GitHub/projects-of-yida/temp control/datalog.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        csv_data = [row for row in reader]
        return csv_data
# 形成UI

csvdata= load_data()
make_plot(csvdata)


# 列表转置
