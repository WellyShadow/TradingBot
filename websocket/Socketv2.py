import websocket, json
import pandas as pd
cc='dodobusd_perpetual'
interval = '15m'
socket= f'wss://fstream.binance.com/ws/{cc}@continuousKline_{interval}'
print(socket)

def on_message(ws,message):
    json_message=json.loads(message)
    candle=json_message['k']
    time_open = candle['t']
    close = candle['c']
    open = candle['o']
    high = candle['h']
    low = candle['l']
    ifclose = candle['x']
    print(close)
    print(ifclose)
    df = pd.DataFrame(index=[time_open])
    df.index.rename('Time',inplace= True)
    df.index = pd.to_datetime(df.index, unit='ms')
    df['Open'] = open
    df['High'] = high
    df['Low'] = low
    df['Close'] = close
    
    #print(df)
    #df.to_excel('df.xlsx')
def on_close(ws):
    print("Conection Closed")
ws = websocket.WebSocketApp(socket,on_message=on_message,on_close=on_close)
ws.run_forever()
