# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import math 
import pandas_datareader as web
import numpy as np
import pandas as pd 
from sklearn.preprocessing import MinMaxScaler as MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

df=web.DataReader('AAPL', data_source='yahoo', start='2019-01-01', end= '2021-12-17')
df


# %%
df.shape


# %%
plt.figure(figsize=(16,8))
plt.title('Close price history')
plt.plot(df['Close'])
plt.xlabel('Date')
plt.ylabel('Close Price USD')


# %%
data = df.filter(['close'])
#convert dataframe to numpy array
dataset = data.values
training_data_len = math.ceil(len(dataset)*.8)

training_data_len


# %%
#scale data
scaler = MinMaxScaler(feature_range=(0,1))

scaled_data = scaler.fit_transform(dataset)

scaled_data


# %%
train_data = scaled_data[0:training_data_len, :]
x_train = []
y_train = [] #target
for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i,0])
    y_train.append(train_data[i,0])
    if i<=60:
        print(x_train)
        print(y_train)
        print()


