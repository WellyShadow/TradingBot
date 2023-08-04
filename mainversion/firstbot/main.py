import bot

from threading import Thread



#task1 = Thread(target = bot.strategy, args = ('DODOBUSD',44))
#task2 = Thread(target = bot.strategy, args = ('LINKUSDT',1.5))
task3 = Thread(target = bot.strategy, args = ('XRPUSDT',28))
    
#task1.start()
#task2.start()
task3.start()

