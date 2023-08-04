from binance.client import Client
import config 
import pandas as pd 
import time 
import talib
from binance.exceptions import BinanceAPIException
from binance.enums import HistoricalKlinesType
pd.options.mode.chained_assignment = None
client = Client(config.api_key,config.secret)
def klines(symbol):
    length = 55
    koef1 = 4.9
    koef2 = 7.35
    koef3 = 9.8
    try:
        df=pd.DataFrame(client.get_historical_klines(symbol, Client.KLINE_INTERVAL_15MINUTE, '21 days ago' ,klines_type=HistoricalKlinesType.FUTURES))
    except BinanceAPIException as e:
        print(e)
        time.sleep(15)
        df=pd.DataFrame(client.get_historical_klines(symbol, Client.KLINE_INTERVAL_15MINUTE, limit = 480 ,klines_type=HistoricalKlinesType.FUTURES))
    df=df.iloc[:,:5]
    df.columns=['Time','Open','High','Low','Close']
    df = df.set_index('Time')
    df.index = pd.to_datetime(df.index, unit='ms')
    df = df.astype(float)
    e = talib.EMA(df.Close,length)
    s = talib.SMA(df.Close,length)
    w = talib.WMA(df.Close,length)
    _,_,hist = talib.MACD(df.Close,fastperiod=12, slowperiod=26, signalperiod=9)
    atr2000 = talib.ATR(df.High,df.Low,df.Close,2000)
    ma = (e + s + w)/3
    df['MA'] = ma
    df['ATR'] = atr2000
    df['HIST'] = hist
    #print(df.HIST[-1])
    #print(df.ATR[-1])
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

def strategy(symbol,qty) :
    Lower1, Lower2, Lower3, Upper1, Upper2, Upper3 = getOpenPositions_Future(qty)
    open_posL1 = Lower1
    open_posL2 = Lower2
    open_posL3 = Lower3
    open_posU1 = Upper1
    open_posU2 = Upper2
    open_posU3 = Upper3
    TrigtonotUpper1 = False
    TrigtonotLower1 = False
    while True:
        time.sleep(1) 
        df = klines(symbol)
        
 
        if open_posL1 == False:
            if (df.Lower1[-1]>df.Close[-1]) and (TrigtonotLower1 == False):
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
            if (df.Upper1[-1]<df.Close[-1]) and (TrigtonotUpper1 == False):
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

    
    
