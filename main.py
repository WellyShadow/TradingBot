import bot
import talib
import matplotlib.pyplot as plt
table = bot.klines('BTCUSDT')
print(table)
e = talib.EMA(table.Close,55)
table['EMA'] = e
plt.figure(figsize=(20,10))
plt.plot(table[['Close','EMA']])
plt.legend(['Close', 'EMA'])
plt.show()