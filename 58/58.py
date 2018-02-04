# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 16:41:30 2018

@author: snall
"""
import matplotlib
matplotlib.rcParams['font.family']=['SimHei']
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dfnew = pd.read_csv('1_29.csv')
dfold = pd.read_csv('12_29.csv')

def avg(df):
    
    df['avg_price'].astype('int64')
    df = df[df['avg_price']<100000]
    grouped = df.groupby('area_name').avg_price
    avg_price = grouped.mean()
    return avg_price

#print(avg_price)
avgold = avg(dfold)
avgnew = avg(dfnew)
print(avgold)
avg = pd.DataFrame(dict(avg_old = avgold,avg_new = avgnew ))
avg.plot.bar()
plt.xlabel('横轴：地区',fontproperties='simHei',fontsize=20)


plt.show()