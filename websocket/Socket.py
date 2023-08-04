from binance.client import Client
import config 
import pandas as pd 
import time 
import talib
from binance.exceptions import BinanceAPIException
from binance.enums import HistoricalKlinesType
from binance import BinanceSocketManager
import asyncio
from enum import Enum
from binance.enums import FuturesType, ContractType

pd.options.mode.chained_assignment = None
client = Client(config.api_key,config.secret)
def klines(symbol):
    try:
        df=pd.DataFrame(client.get_historical_klines(symbol, Client.KLINE_INTERVAL_15MINUTE, "5 days ago UTC","15 minutes ago UTC"  ,klines_type=HistoricalKlinesType.FUTURES))
    except BinanceAPIException as e:
        print("не сработало")
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
    print(df)
    return df

def createframe(msg):
    df=pd.DataFrame([msg])
    df=df.loc[:,['k'][0]]
    #df.to_excel('df.xlsx')
    df=df.loc[0]['c']
    #print(df)
    #print(df)
    #dft=dfk.loc[:,['t']]
    #df=df.loc[:,['t']]
    #df.columns=['Symbol','Time','Now']
    #df = df.set_index('Time')
    #df.index = pd.to_datetime(df.index, unit='ms')
    #df = df.astype(float)
    return df

async def st (symbol):
    bm=BinanceSocketManager(client)
    ts = bm.kline_futures_socket(symbol = symbol, interval = Client.KLINE_INTERVAL_15MINUTE,futures_type = FuturesType.USD_M, contract_type = ContractType.PERPETUAL)
    #print("до цикла")
    async with ts as tscm:
        print("за циклом")
        while True:
            print("в цикле")
            res = await tscm.recv()
            if res:
                #print("в условии")
                frame=createframe(res)
                print(frame)

if __name__=='__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(st('BTCUSDT'))