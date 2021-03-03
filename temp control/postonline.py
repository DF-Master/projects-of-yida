import streamlit as st
import numpy as np
import csv
import pandas as pd
from time import sleep
import matplotlib.pyplot as plt


# 设置默认变量^
waittimedefault = 10


# 定义列表转置


def transpose(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        matrix1 = []
        for j in range(len(matrix)):
            matrix1.append(matrix[j][i])
        new_matrix.append(matrix1)
    return new_matrix

# 制造数据表


def make_plot(datafile, num=35):
    global datalineplot
    if len(datafile) > num:
        dataset = datafile[-(num):]
    elif len(datafile) > 1 and len(datafile[0]) == 3:
        dataset = datafile[1:]
    else:
        dataset = [['22.2', '60.0', '42:23']]
    datasetT = transpose(dataset)
    tempchangelist = list(map(float,datasetT[0]))
    tempsetlist = list(map(float,datasetT[1]))
    timelist = datasetT[2]
    plt.close('all')
    fig = plt.figure()
    # fig.title("实时数据变化图")
    ax = fig.add_subplot()
    plt.xticks(rotation=90)

    linetemprev = ax.plot(timelist, tempchangelist, '-g', label='Temp. Rev.')
    linetempset = ax.plot(timelist, tempsetlist, ':b', label='Temp. Set.')
    ax.grid(linestyle='--', alpha=0.5)
    ax.legend(loc='upper left', shadow=True, fancybox=True)
    ax.set_xlabel('Time')
    ax.set_ylabel('Data')
    ax.set_title('Data Live LinePlot')

    return fig


# 形成网页UI
# 加载数据
def load_data(max=30):
    reader = pd.read_csv("C:/Users/jiang/Documents/GitHub/projects-of-yida/temp control/datalog.csv")
    readerlist = reader.values.tolist()
    if len(readerlist)> max:
        readerlist= reader.tail(max).values.tolist()
    return readerlist
# 形成UI


def st_generate():
    global csvshow

    datanow = st.empty()
    datanow.table(pd.DataFrame(
        csvshow[-1:], columns=['当前温度', '设置温度', '时间戳']))
    datalineplottitle = st.empty()
    datalineplottitle = st.header('近期温度变化图 Data LinePlot')
    datalineplot = st.empty()
    datalineplot.write(make_plot(csvshow))

    titletemplog = st.empty()
    titletemplog.header('数据记录 Temp. Log')
    datalog = st.empty()
    datalog.table(pd.DataFrame(csvshow[:], columns=['测得温度', '设置温度', '时间戳']))
    sleep(waittimedefault)
    datanow.empty()
    datalog.empty()
    titletemplog.empty()
    datalineplottitle.empty()
    csvshow = load_data()
    datalineplot.empty()


st.title("温控器网页UI")
st.markdown('> made by [Yida](https://github.com/DF-Master) --210303 update')
st.header('当前数据 Data Now')


csvshow = load_data()


while True:

    st_generate()
