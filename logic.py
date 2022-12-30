import bot
import numpy as np
import bot
import talib
import matplotlib.pyplot as plt
import pandas as pd 


open_pos = False
def history():
    buys1 = []
    buys2 = []
    buys3 = []
    sells1 = []
    sells2 = []
    sells3 = []
    takeL1 = []
    takeL2 = []
    takeL3 = []
    takeU1 = []
    takeU2 = []
    takeU3 = []
    buyorder = []
    sellorder = []
    open_posL1 = False
    open_posL2 = False
    open_posL3 = False
    open_posU1 = False
    open_posU2 = False
    open_posU3 = False
    table600 = bot.klines('BTCUSDT')
    #print(table600)
    table600['Buy_Signal1'] = False
    table600['Sell_Signal1'] = False
    table600['Buy_Signal2'] = False
    table600['Sell_Signal2'] = False
    table600['Buy_Signal3'] = False
    table600['Sell_Signal3'] = False
    table600['Take_Signal'] = False

    for i in range(len(table600)):
        if open_posL1 == False:
            if table600.Lower1[i]>table600.Low[i]:
                table600.Buy_Signal1[i] = True
                open_posL1=True
                buys1.append(i)
        elif open_posL1 == True:
            if table600.MA[i]<table600.High[i]:
                table600.Buy_Signal1[i] = False
                table600.Take_Signal[i] = True
                open_posL1=False
                buyorder.append([[buys1[-1]],[i]])
                takeL1.append(i)
        
        if open_posL2 == False:
            if table600.Lower2[i]>table600.Low[i]:
                table600.Buy_Signal2[i] = True
                open_posL2=True
                buys2.append(i)
        elif open_posL2 == True:
            if table600.MA[i]<table600.High[i]:
                table600.Buy_Signal2[i] = False
                table600.Take_Signal[i] = True
                open_posL2=False
                buyorder.append([[buys2[-1]],[i]])
                takeL2.append(i)

        if open_posL3 == False:
            if table600.Lower3[i]>table600.Low[i]:
                table600.Buy_Signal3[i] = True
                open_posL3=True
                buys3.append(i)
        elif open_posL3 == True:
            if table600.MA[i]<table600.High[i]:
                table600.Buy_Signal3[i] = False
                table600.Take_Signal[i] = True
                open_posL3=False
                buyorder.append([[buys3[-1]],[i]])
                takeL3.append(i)
#--------------------------------------------------------------------------------------#
        if open_posU1 == False:
            if table600.Upper1[i]<table600.High[i]:
                table600.Sell_Signal1[i] = True
                open_posU1=True
                sells1.append(i)
        elif open_posU1 == True:
            if table600.MA[i]>table600.Low[i]:
                table600.Sell_Signal1[i] = False
                table600.Take_Signal[i] = True
                open_posU1=False
                sellorder.append([[sells1[-1]],[i]])
                takeU1.append(i)

        if open_posU2 == False:
            if table600.Upper2[i]<table600.High[i]:
                table600.Sell_Signal2[i] = True
                open_posU2=True
                sells2.append(i)
        elif open_posU2 == True:
            if table600.MA[i]>table600.Low[i]:
                table600.Sell_Signal2[i] = False
                table600.Take_Signal[i] = True
                open_posU2=False
                sellorder.append([[sells2[-1]],[i]])
                takeU2.append(i)

        if open_posU3 == False:
            if table600.Upper3[i]<table600.High[i]:
                table600.Sell_Signal3[i] = True
                open_posU3=True
                sells3.append(i)
        elif open_posU3 == True:
            if table600.MA[i]>table600.Low[i]:
                table600.Sell_Signal3[i] = False
                table600.Take_Signal[i] = True
                open_posU3=False
                sellorder.append([[sells3[-1]],[i]])
                takeU3.append(i)
    
   
    print("buyorders:", buyorder)  
    print("sellorders:", sellorder)  

    print("Расчет..")
    profit1 = pd.concat([table600.Lower1[buys1], table600.MA[takeL1]],axis=1)
    profit2 = pd.concat([table600.Lower2[buys2], table600.MA[takeL2]],axis=1)
    profit3 = pd.concat([table600.Lower3[buys3], table600.MA[takeL3]],axis=1)
    profit4 = pd.concat([table600.Upper1[sells1], table600.MA[takeU1]],axis=1)
    profit5 = pd.concat([table600.Upper2[sells2], table600.MA[takeU2]],axis=1)
    profit6 = pd.concat([table600.Upper3[sells3], table600.MA[takeU3]],axis=1)
    
    profit = pd.concat([profit1,profit2,profit3,profit4,profit5,profit6])
    profit = profit.sort_index()
    #profit.columns = ['Buys','Sells']
    print(profit)
    #totalprofit = profit.shift(-1).Lower1 - profit.MA
    #print(totalprofit)
    #print(totalprofit.sum())

        #if open_pos == False :
          #  table600['Buy_Signal1'] = np.where(table600.Lower1>table600.Low,True,False)
         #   table600['Sell_Signal1'] = np.where(table600.Upper1<table600.High,True,False)

           # table600['Buy_Signal2'] = np.where(table600.Lower2>table600.Low,True,False)
          #  table600['Sell_Signal2'] = np.where(table600.Upper2<table600.High,True,False)

           # table600['Buy_Signal3'] = np.where(table600.Lower3>table600.Low,True,False)
           # table600['Sell_Signal3'] = np.where(table600.Upper3<table600.High,True,False)

    #if open_pos == True 
    #print(table600['Buy_Signal1'])

    plt.figure(figsize=(20,10))

    plt.plot(table600[['Close','MA','Upper1','Lower1','Upper2','Lower2','Upper3','Lower3']])

    plt.scatter(table600.index[table600.Take_Signal],table600[table600.Take_Signal].MA,marker='o',color='#d62728')

    plt.scatter(table600.index[table600.Buy_Signal1],table600[table600.Buy_Signal1].Lower1,marker='^',color='g')
    plt.scatter(table600.index[table600.Sell_Signal1],table600[table600.Sell_Signal1].Upper1,marker='v',color='r')

    plt.scatter(table600.index[table600.Buy_Signal2],table600[table600.Buy_Signal2].Lower2,marker='^',color='g')
    plt.scatter(table600.index[table600.Sell_Signal2],table600[table600.Sell_Signal2].Upper2,marker='v',color='r')

    plt.scatter(table600.index[table600.Buy_Signal3],table600[table600.Buy_Signal3].Lower3,marker='^',color='g')
    plt.scatter(table600.index[table600.Sell_Signal3],table600[table600.Sell_Signal3].Upper3,marker='v',color='r')
    plt.legend(['Close', 'MA','Upper1','Lower1','Upper2','Lower2','Upper3','Lower3'])
    plt.show()

