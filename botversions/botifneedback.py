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
    try:
        df=pd.DataFrame(client.get_historical_klines(symbol, Client.KLINE_INTERVAL_15MINUTE, limit = 480 ,klines_type=HistoricalKlinesType.FUTURES))
    except BinanceAPIException as e:
        print(e)
        time.sleep(15)
        df=pd.DataFrame(client.get_historical_klines(symbol, Client.KLINE_INTERVAL_15MINUTE, limit = 480 ,klines_type=HistoricalKlinesType.FUTURES))
    df=df.iloc[:,:5]
    df.columns=['Time','Open','High','Low','Close']
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
    return df

def strategy(symbol,qty) :
    Lower1, Lower2, Lower3, Upper1, Upper2, Upper3 = getOpenPositions_Future(qty)
    open_posL1 = Lower1
    open_posL2 = Lower2
    open_posL3 = Lower3
    open_posU1 = Upper1
    open_posU2 = Upper2
    open_posU3 = Upper3
    trigL1 = False
    trigL2 = False
    trigL3 = False
    trigU1 = False
    trigU2 = False
    trigU3 = False
    while True:
        time.sleep(1) 
        df = klines(symbol)
        
        if df.Lower1[-1]>df.Low[-1]:
            trigL1=True
        if df.Lower2[-1]>df.Low[-1]:
            trigL2=True
        if df.Lower3[-1]>df.Low[-1]:
            trigL3=True

        if df.Upper1[-1]<df.High[-1]:
            trigU1=True
        if df.Upper2[-1]<df.High[-1]:
            trigU2=True
        if df.Upper3[-1]<df.High[-1]:
            trigU3=True
 
        if open_posL1 == False:
            if (df.Lower1[-1]<df.Close[-1]) and (trigL1):
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
                    trigL1 = False
        
        if open_posL2 == False:
            if (df.Lower2[-1]<df.Close[-1]) and (trigL2):
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
                    trigL2 = False

        if open_posL3 == False:
            if (df.Lower3[-1]>df.Close[-1]) and (trigL3):
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
                    trigL3 = False
#--------------------------------------------------------------------------------------#
        if open_posU1 == False:
            if (df.Upper1[-1]>df.Close[-1]) and (trigU1):
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
                    trigU1 = False

        if open_posU2 == False:
            if (df.Upper2[-1]>df.Close[-1]) and (trigU2):
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
                    trigU2 = False

        if open_posU3 == False:
            if (df.Upper3[-1]>df.Close[-1]) and (trigU3):
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
                    trigU3=False  

        

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

    
    
