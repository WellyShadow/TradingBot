from binance.client import Client
import config 
import pandas as pd 
import time 
import talib                                                                                #"6 Sep 2020","16 Mar 2021"
from binance.exceptions import BinanceAPIException                                          #"15 Apr 2021","25 May 2021"
from binance.enums import HistoricalKlinesType                                              #"16 Jul 2021","10 Oct 2021"
pd.options.mode.chained_assignment = None                                                   #"10 Oct 2021","15 Jun 2022"
client = Client(config.api_key,config.secret)                                               #"15 Jun 2022","1 Jan 2023"
def klinestest(symbol,datestart,dateend):
    try:
        df=pd.DataFrame(client.get_historical_klines(symbol, Client.KLINE_INTERVAL_15MINUTE,datestart,dateend,klines_type=HistoricalKlinesType.FUTURES))#,klines_type=HistoricalKlinesType.FUTURES
    except BinanceAPIException as e:
        print("error")
        #time.sleep(60)
        #df=pd.DataFrame(client.get_historical_klines(symbol, Client.KLINE_INTERVAL_15MINUTE,"1 Jan 2023",klines_type=HistoricalKlinesType.FUTURES))#
    if df.empty: 
        print("err")
    df=df.iloc[:,:5]
    df.columns=['Time','Open','High','Low','Close']
    df = df.set_index('Time')
    df.index = pd.to_datetime(df.index, unit='ms')
    df = df.astype(float)
    return df

def indicator(df,length,koef1,koef2,koef3):
    e = talib.EMA(df.Close,length)
    s = talib.SMA(df.Close,length)
    w = talib.WMA(df.Close,length)
    _,_,hist = talib.MACD(df.Close,fastperiod=12, slowperiod=26, signalperiod=9)
    atr100 = talib.ATR(df.High,df.Low,df.Close,100)
    atr2000 = talib.SMA(atr100,200)
    
    #print('atr2000',atr2000)
    #atr2000dil3= atr2000 / 3
    #print('atr2000dil3',atr2000dil3)
    df['ATR100'] = atr100
    df['ATR'] = atr2000
    df['HIST'] = hist
    ma = (e + s + w)/3
    df['MA'] = ma
    rangema=talib.ATR(df.High,df.Low,df.Close,length) 
    upper1=ma+rangema*koef1
    lower1=ma-rangema*koef1
    upper2=ma+rangema*koef2
    lower2=ma-rangema*koef2
    upper3=ma+rangema*koef3
    lower3=ma-rangema*koef3
    step = koef3 - koef2
    upperStop=ma+rangema*(koef3 + step)
    lowerStop=ma-rangema*(koef3 + step)
    df['Upper1'] = upper1
    df['Lower1'] = lower1
    df['Upper2'] = upper2
    df['Lower2'] = lower2
    df['Upper3'] = upper3
    df['Lower3'] = lower3
    df['UpperStop'] = upperStop
    df['LowerStop'] = lowerStop
    return df


    
    
