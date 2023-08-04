import botv2 
from threading import Thread
import websocket


task1 = Thread(target = botv2.start_websocket, args = ('dodobusd',44))
task2 = Thread(target = botv2.start_websocket, args = ('icpbusd',1.5))
task3 = Thread(target = botv2.start_websocket, args = ('tlmbusd',400))
    
task1.start()
task2.start()
task3.start()




