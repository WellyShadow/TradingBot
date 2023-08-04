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

def start_websocket(symbol,qnty): 
    lock = Lock()
    TrigtonotUpper1 = False
    TrigtonotLower1 = False
    open_posL1 = False
    open_posL2 = False
    open_posL3 = False
    open_posU1 = False
    open_posU2 = False
    open_posU3 = False
    #with lock:
    #    open_posL1, open_posL2, open_posL3, open_posU1, open_posU2, open_posU3  = getOpenPositions_Future(qnty)
    histdf = pd.DataFrame()
    ifclose = True
    trig = 1
    def on_message(ws,message,symbol):
            nonlocal open_posL1 
            nonlocal open_posL2 
            nonlocal open_posL3 
            nonlocal open_posU1
            nonlocal open_posU2 
            nonlocal open_posU3 
            nonlocal TrigtonotUpper1 
            nonlocal TrigtonotLower1 
            nonlocal histdf
            nonlocal ifclose
            nonlocal trig
            with lock:
                json_message=json.loads(message)
                print("ifclose",ifclose)
                if trig == 1:
                    histdf=klines(symbol)
                    print(symbol)
                    trig = 0
                ifclose,livedf = createframe(json_message) 
                #print(livedf)
                if ifclose:
                    trig = 1
                histdf.update(livedf)
                #print(histdf)
                df = createIndicator(histdf)
                print(df.Close)
                open_posL1,open_posL2,open_posL3,open_posU1,open_posU2,open_posU3,TrigtonotLower1,TrigtonotUpper1 = strategy(symbol,qnty,df,open_posL1,open_posL2,open_posL3,open_posU1,open_posU2,open_posU3,TrigtonotLower1,TrigtonotUpper1)
    socket= f'wss://fstream.binance.com/ws/{symbol}_perpetual@continuousKline_15m'
    ws = websocket.WebSocketApp(socket,on_message=lambda ws,msg:on_message(ws,msg,symbol),on_close=on_close)
    ws.run_forever()

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
    df = pd.DataFrame(index=[time_open])
    df.index.rename('Time',inplace= True)
    df.index = pd.to_datetime(df.index, unit='ms')
    df['Open'] = open
    df['High'] = high
    df['Low'] = low
    df['Close'] = close  
    df = df.astype(float) 
    print(df.Close[-1])
    return ifclose,df

def createIndicator(df):
        length = 10
        koef1 = 2.4
        koef2 = 4.05
        koef3 = 5.7
        e = talib.EMA(df.Close,length)
        s = talib.SMA(df.Close,length)
        w = talib.WMA(df.Close,length)
        _,_,hist = talib.MACD(df.Close,fastperiod=12, slowperiod=26, signalperiod=9)
        atr100 = talib.ATR(df.High,df.Low,df.Close,100)
        atr2000 = talib.SMA(atr100,200)
        ma = (e + s + w)/3
        df['MA'] = ma
        df['ATR100'] = atr100
        df['ATR'] = atr2000
        df['HIST'] = hist
        print('ATR100',df.ATR100[-1])
        print('atr',df.ATR[-1])
        print('hist',df.HIST[-1])
        rangema=talib.ATR(df.High,df.Low,df.Close,length) 
        upper1=ma+rangema*koef1
        lower1=ma-rangema*koef1
        upper2=ma+rangema*koef2
        lower2=ma-rangema*koef2
        upper3=ma+rangema*koef3
        lower3=ma-rangema*koef3
        df['Upper1'] = upper1
        df['Lower1'] = lower1
        df['Upper2'] = upper2
        df['Lower2'] = lower2
        df['Upper3'] = upper3
        df['Lower3'] = lower3
        
        return df

def klines(symbol):
    try:
        df=pd.DataFrame(client.get_historical_klines(symbol, Client.KLINE_INTERVAL_15MINUTE, limit= 480 ,klines_type=HistoricalKlinesType.FUTURES))
    except BinanceAPIException as e:
        print(e)
        time.sleep(15)
        df=pd.DataFrame(client.get_historical_klines(symbol, Client.KLINE_INTERVAL_15MINUTE, limit= 480 ,klines_type=HistoricalKlinesType.FUTURES))
    df=df.iloc[:,:5]
    df.columns=['Time','Open','High','Low','Close']
    df = df.set_index('Time')
    df.index = pd.to_datetime(df.index, unit='ms')
    df = df.astype(float)
    
    return df

def strategy(symbol,qty,df,open_posL1,open_posL2,open_posL3,open_posU1,open_posU2,open_posU3,TrigtonotLower1,TrigtonotUpper1) :
    
   
    print(symbol)
    #print('open_posL1',open_posL1)
    #print('open_posL2',open_posL2)
    #print('open_posL3',open_posL3)
    #print('open_posU1',open_posU1)
    #print('open_posU2',open_posU2)
    #print('open_posU3',open_posU3) 
    #print('TrigtonotUpper1',TrigtonotUpper1)
    #print('TrigtonotLower1',TrigtonotLower1)
    if ((df.ATR[-1])/2)<df.HIST[-1]:
        TrigtonotUpper1 = True
    else:
        TrigtonotUpper1 = False
    if ((-(df.ATR[-1])/2))>df.HIST[-1]:
        TrigtonotLower1 = True
    else:
        TrigtonotLower1 = False
    
    if open_posL1 == False:
        if (df.Lower1[-1]>df.Close[-1]) and (TrigtonotLower1 == False):
            try:
                print('OPEN POSITION')
                client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
            except: 
                time.sleep(3)
                client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
            open_posL1=True
    elif open_posL1 == True :
            if df.MA[-1]<df.Close[-1]:
                try:
                    print('CLOSE POSITION')
                    client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
                except: 
                    time.sleep(3)
                    client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
                open_posL1=False
                
        
    if open_posL2 == False:
        if (df.Lower2[-1]>df.Close[-1]):
            try:
                print('OPEN POSITION')
                client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
            except: 
                time.sleep(3)    
                client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
            open_posL2=True
    elif open_posL2 == True:
            if df.MA[-1]*0.997<df.Close[-1]:
                try:
                    print('CLOSE POSITION')
                    client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
                except: 
                    time.sleep(3) 
                    client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
                open_posL2=False
                

    if open_posL3 == False:
        if (df.Lower3[-1]>df.Close[-1]):
            try:
                print('OPEN POSITION')
                client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
            except: 
                time.sleep(3) 
                client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
            open_posL3=True
    elif open_posL3 == True:
            if df.MA[-1]*0.997<df.Close[-1]:
                try:
                    print('CLOSE POSITION')
                    client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
                except: 
                    time.sleep(3)    
                    client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
                open_posL3=False
                
#--------------------------------------------------------------------------------------#
    if open_posU1 == False:
        if (df.Upper1[-1]<df.Close[-1]) and (TrigtonotUpper1 == False):
            try:
                print('OPEN POSITION')
                client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
            except: 
                time.sleep(3) 
                client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
            open_posU1=True
    elif open_posU1 == True:
            if df.MA[-1]>df.Close[-1]:
                try:
                    print('CLOSE POSITION')
                    client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
                except: 
                    time.sleep(3) 
                    client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
                open_posU1=False
                

    if open_posU2 == False:
        if (df.Upper2[-1]<df.Close[-1]):
            try:
                print('OPEN POSITION')
                client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
            except: 
                time.sleep(3) 
                client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
            open_posU2=True
    elif open_posU2 == True:
            if df.MA[-1]*1.003>df.Close[-1]:
                try:
                    print('CLOSE POSITION')
                    client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
                except: 
                    time.sleep(3) 
                    client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
                open_posU2=False
                

    if open_posU3 == False:
        if (df.Upper3[-1]<df.Close[-1]):
            try:
                print('OPEN POSITION')
                client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
            except: 
                time.sleep(3) 
                client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
            open_posU3=True
    elif open_posU3 == True:
            if df.MA[-1]*1.003>df.Close[-1]:
                try:
                    print('CLOSE POSITION')
                    client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
                except: 
                    time.sleep(3) 
                    client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
                open_posU3=False 
    if open_posU1 and (df.ATR100[-1]<df.HIST[-1]):
        try:
            print('STOP POSITION')
            client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
        except: 
            time.sleep(3) 
            client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=qty)
        open_posU1=False             
    if open_posL1 and (-(df.ATR100[-1])>df.HIST[-1]):
        try:
            print('CLOSE POSITION')
            client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
        except: 
            time.sleep(3)
            client.futures_create_order(symbol=symbol,side='SELL',type='MARKET',quantity=qty)
        open_posL1=False               
    return open_posL1,open_posL2,open_posL3,open_posU1,open_posU2,open_posU3,TrigtonotLower1,TrigtonotUpper1


def getOpenPositions_Future(qty):
    Lower1 = Lower2 = Lower3 = Upper1 = Upper2 = Upper3 = False
    positions = client.futures_account()['positions']
    positions = pd.DataFrame.from_dict(positions)
    positions = positions.loc[positions['maintMargin']!='0']
    for i in range (len(positions['positionAmt'].values)):
        if positions.empty:
            Lower1 = Lower2 = Lower3 = Upper1 = Upper2 = Upper3 = False
        elif (positions['positionAmt'].values[i] == str(qty)):
            Lower1 = True
        elif (positions['positionAmt'].values[i] ==str(qty*2)):
            Lower1 = True 
            Lower2 = True   
        elif (positions['positionAmt'].values[i] ==str(qty*3)):
            Lower1 = True 
            Lower2 = True  
            Lower3 = True
        elif (positions['positionAmt'].values[i] ==str(-qty)):
            Upper1 = True
        elif (positions['positionAmt'].values[i] ==str(-qty*2)):
            Upper1 = True
            Upper2 = True    
        elif (positions['positionAmt'].values[i] ==str(-qty*3)):
            Upper1 = True
            Upper2 = True 
            Upper3 = True    
    return Lower1, Lower2, Lower3, Upper1, Upper2, Upper3   
                

