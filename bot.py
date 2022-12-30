from binance.client import Client
import config 
import pandas as pd 
from time import sleep
import talib
from binance.exceptions import BinanceAPIException

client = Client(config.api_key,config.secret)

def klines(symbol):
    try:
        df=pd.DataFrame(client.get_historical_klines(symbol, Client.KLINE_INTERVAL_15MINUTE, "58 day ago"))
    except BinanceAPIException as e:
        print(e)
        sleep(60)
        df=pd.DataFrame(client.get_historical_klines(symbol, Client.KLINE_INTERVAL_15MINUTE, "58 day ago"))
    df=df.iloc[:,:6]
    df.columns=['Time','Open','High','Low','Close','Volume']
    df = df.set_index('Time')
    df.index = pd.to_datetime(df.index, unit='ms')
    df = df.astype(float)

    e = talib.EMA(df.Close,55)
    s = talib.SMA(df.Close,55)
    w = talib.WMA(df.Close,55)

    ma = (e + s + w)/3

    df['MA'] = ma

    rangema=talib.ATR(df.High,df.Low,df.Close,55) 


    upper1=ma+rangema*4.9
    lower1=ma-rangema*4.9

    upper2=ma+rangema*7.35
    lower2=ma-rangema*7.35

    upper3=ma+rangema*9.8
    lower3=ma-rangema*9.8

    df['Upper1'] = upper1
    df['Lower1'] = lower1

    df['Upper2'] = upper2
    df['Lower2'] = lower2

    df['Upper3'] = upper3
    df['Lower3'] = lower3

    table600 = df[5000:]
    return table600

def strategy(symbol,qty,open_pos = False) :
    
    while True:
        df = klines('BTCUSDT')
        print(df)
        print(df.High.iloc[1])
        if not open_pos:
            if df.High.iloc[-1] > df.Upper1.iloc[-1]: 
                order = client.create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
                print(order)
                open_pos=True
                buyprice=float(order['fills'][0]['price'])
                break
        if open_pos:
             while True:
                df = klines('BTCUSDT')
                if df.Low.iloc[-1] < df.MA.iloc[-1]:
                    order = client.create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
                    print(order)
                    sellprice = float(order['fills'][0]['price'])
                    print(f'profit = {(sellprice - buyprice)/buyprice}')
                    open_pos=False
                    break


def futures():
    balance = client.futures_account_balance()[6]['balance']
    print(balance)
