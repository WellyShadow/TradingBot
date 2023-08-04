from binance.client import Client
from binance.error import ClientError
import pandas as pd 
from pandas import DataFrame
import time

import config 

pd.set_option('display.max_row',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)

if __name__ == '__main__':
    cl = Client (
        config.api_key,
        config.secret
    )
    symbol = 'ETHUSDT'
    while True:
        try:
            r=cl.create_order (
                symbol=symbol,
                side ='BUY',
                type = 'MARKET',
                quoteOrderQty = 10   
            )
            print(r)
        except: 
            time.sleep(15)
            print("err")
            cl.create_order (
                symbol=symbol,
                side ='BUY',
                type = 'MARKET',
                quoteOrderQty = 10   
            )
            print(r)
