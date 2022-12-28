from binance.client import Client
import config 
import pandas as pd 
from time import sleep
import ta
from binance.exceptions import BinanceAPIException

client = Client(config.api_key,config.secret)

def klines(symbol):
    try:
        df=pd.DataFrame(client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1DAY, "17 Aug, 2017"))
    except BinanceAPIException as e:
        print(e)
        sleep(60)
        df=pd.DataFrame(client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1DAY, "17 Aug, 2017"))
    df=df.iloc[:,:6]
    df.columns=['Time','Open','High','Low','Close','Volume']
    df = df.set_index('Time')
    df.index = pd.to_datetime(df.index, unit='ms')
    df = df.astype(float)
    return df



