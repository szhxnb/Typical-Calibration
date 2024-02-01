import numpy as np 
import pandas as pd
from datetime import time 

# Assist the calculation to convert the time
def milliseconds_to_time(milliseconds):
    hours = milliseconds // (1000 * 60 * 60)
    minutes = (milliseconds % (1000 * 60 * 60)) // (1000 * 60)
    seconds = (milliseconds % (1000 * 60)) // 1000
    return f'{hours}:{minutes}:{seconds}'

# Perform a first round data cleaning before concat data into one table
def dataClean(df, date): 
    temp = df.copy() 
    date_new = pd.to_datetime(date, format='%Y%m%d') 
    temp['time'] = temp['time'].apply(milliseconds_to_time) 
    temp['time'] = date + ' ' + temp['time'] 
    temp['time'] = pd.to_datetime(temp['time'], format='%Y%m%d %H:%M:%S') 
    to_drop = temp[(temp['Q1'] < 0.9999) | (temp['Q2'] < 0.9999)].index 
    temp = temp.drop(to_drop) 
    temp.replace(999999, np.nan, inplace=True) 
    threshold = 0.5 
    percent_na = temp.isnull().mean(axis=1) 
    temp = temp[percent_na <= threshold] 
    return temp 
