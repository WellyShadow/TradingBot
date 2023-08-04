import bot
from threading import Thread
import websocket


#task1 = Thread(target = bot.start_websocket, args = ('',44))
task2 = Thread(target = bot.start_websocket, args = ('linkusdt',1.5))
task3 = Thread(target = bot.start_websocket, args = ('xrpusdt',28))
    
#task1.start()
task2.start()
task3.start()




