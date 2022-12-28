import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = yf.download('BTC',start='2021-01-01')

df['SMA'] = df.Close.rolling(window=20).mean()
df['stddev'] = df.Close.rolling(window=20).std()

df['Upper'] = df.SMA + 2*df.stddev
df['Lower'] = df.SMA - 2*df.stddev

df['Buy_Signal'] = np.where(df.Lower > df.Close,True,False)
df['Sell_Signal'] = np.where(df.Upper < df.Close,True,False)
df=df.dropna()
print(df)
plt.figure(figsize=(20,10))
plt.plot(df[['Close','SMA','Upper','Lower']])
plt.scatter(df.index[df.Buy_Signal],df[df.Buy_Signal].Close,marker='^',color='g')
plt.scatter(df.index[df.Sell_Signal],df[df.Sell_Signal].Close,marker='v',color='r')
plt.fill_between(df.index, df.Upper, df.Lower, color='grey', alpha=0.3)
plt.legend(['Close', 'SMA', 'Upper', 'Lower'])
plt.show()