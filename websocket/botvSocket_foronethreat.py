import websocket, json
import pandas as pd
import talib
import time 
import config
from binance.client import Client
from binance.exceptions import BinanceAPIException
from binance.enums import HistoricalKlinesType
from threading import Thread, Lock
pd.options.mode.chained_assignment = None
client = Client(config.api_key,config.secret)

#lock = Lock()
ifclose = True
open_posL1 = False
open_posL2 = False
open_posL3 = False
open_posU1 = False
open_posU2 = False
open_posU3 = False
histdf = pd.DataFrame()
#livedf = pd.DataFrame()
symbol = ''
qty = 0
def start_websocket(token,qnty): 
    global symbol 
    global qty
    symbol = token
    qty = qnty
    socket= f'wss://fstream.binance.com/ws/{symbol}_perpetual@continuousKline_15m'
    ws = websocket.WebSocketApp(socket,on_message=on_message,on_close=on_close)
    ws.run_forever()

def on_message(ws,message):
    print('1')
    global symbol 
    global qty
    global ifclose
    global histdf
    json_message=json.loads(message)
    print(ifclose)
    if ifclose:
        histdf=klines(symbol)
    ifclose,livedf = createframe(json_message)   
    histdf.update(livedf)
    df = createIndicator(histdf)
    #strategy(symbol,qty,df)
    print(df)
def on_close(ws):
    print("Conection Closed")

def createframe(json_message):
    candle=json_message['k']
    time_open = candle['t']
    close = candle['c']
    open = candle['o']
    high = candle['h']
    low = candle['l']
    ifclose = candle['x']
    print(close)
    df = pd.DataFrame(index=[time_open])
    df.index.rename('Time',inplace= True)
    df.index = pd.to_datetime(df.index, unit='ms')
    df['Open'] = open
    df['High'] = high
    df['Low'] = low
    df['Close'] = close  
    df = df.astype(float) 
    return ifclose,df

def createIndicator(df):
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
        return df

def klines(symbol):
    try:
        df=pd.DataFrame(client.get_historical_klines(symbol, Client.KLINE_INTERVAL_15MINUTE, limit = 288 ,klines_type=HistoricalKlinesType.FUTURES))
    except BinanceAPIException as e:
        print(e)
        time.sleep(15)
        df=pd.DataFrame(client.get_historical_klines(symbol, Client.KLINE_INTERVAL_15MINUTE, limit = 288 ,klines_type=HistoricalKlinesType.FUTURES))
    df=df.iloc[:,:5]
    df.columns=['Time','Open','High','Low','Close']
    df = df.set_index('Time')
    df.index = pd.to_datetime(df.index, unit='ms')
    df = df.astype(float)
    return df

def strategy(symbol,qty,df) :
    global open_posL1
    global open_posL2
    global open_posL3
    global open_posU1
    global open_posU2
    global open_posU3
 
    if open_posL1 == False:
        if (df.Lower1[-1]>df.Close[-1]):
            try:
                client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
            except: 
                time.sleep(3)
                client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
            open_posL1=True
    elif open_posL1 == True :
            if df.MA[-1]*0.997<df.Close[-1]:
                try:
                    client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
                except: 
                    time.sleep(3)
                    client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
                open_posL1=False
        
    if open_posL2 == False:
        if (df.Lower2[-1]>df.Close[-1]):
            try:
                client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
            except: 
                time.sleep(3)    
                client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
            open_posL2=True
    elif open_posL2 == True:
            if df.MA[-1]*0.997<df.Close[-1]:
                try:
                    client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
                except: 
                    time.sleep(3) 
                    client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
                open_posL2=False

    if open_posL3 == False:
        if (df.Lower3[-1]>df.Close[-1]):
            try:
                client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
            except: 
                time.sleep(3) 
                client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
            open_posL3=True
    elif open_posL3 == True:
            if df.MA[-1]*0.997<df.Close[-1]:
                try:
                    client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
                except: 
                    time.sleep(3)    
                    client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
                open_posL3=False
#--------------------------------------------------------------------------------------#
    if open_posU1 == False:
        if (df.Upper1[-1]<df.Close[-1]):
            try:
                client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
            except: 
                time.sleep(3) 
                client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
            open_posU1=True
    elif open_posU1 == True:
            if df.MA[-1]*1.003>df.Close[-1]:
                try:
                    client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
                except: 
                    time.sleep(3) 
                    client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
                open_posU1=False

    if open_posU2 == False:
        if (df.Upper2[-1]<df.Close[-1]):
            try:
                client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
            except: 
                time.sleep(3) 
                client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
            open_posU2=True
    elif open_posU2 == True:
            if df.MA[-1]*1.003>df.Close[-1]:
                try:
                    client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
                except: 
                    time.sleep(3) 
                    client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
                open_posU2=False

    if open_posU3 == False:
        if (df.Upper3[-1]<df.Close[-1]):
            try:
                client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
            except: 
                time.sleep(3) 
                client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
            open_posU3=True
    elif open_posU3 == True:
            if df.MA[-1]*1.003>df.Close[-1]:
                try:
                    client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
                except: 
                    time.sleep(3) 
                    client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
                open_posU3=False  

if __name__ == '__main__':
    start_websocket('xrpusdt',28)