import logicversions.botfortest as botfortest
import numpy as np
import bot
import talib
import matplotlib.pyplot as plt
import pandas as pd 
pd.options.mode.chained_assignment = None

open_pos = False
def history(symbol,datestart,dateend,tableafterrequest=0):
    sizep = 10
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
   # buyorder = []
   # sellorder = []
    signals = 0
    open_posL1 = False
    open_posL2 = False
    open_posL3 = False
    open_posU1 = False
    open_posU2 = False
    open_posU3 = False
    if tableafterrequest.empty:
        table600 = botfortest.klinestest(symbol,datestart,dateend)
        print("зашло")
    table600 = tableafterrequest   
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
            if table600.Lower1.iloc[i]>table600.Low.iloc[i]:
                table600.Buy_Signal1.iloc[i] = True
                open_posL1=True
                buys1.append(i)
                signals=signals+1
        elif open_posL1 == True:
            if table600.MA.iloc[i]*0.999<table600.High.iloc[i]:
                table600.Buy_Signal1.iloc[i] = False
                table600.Take_Signal.iloc[i] = True
                open_posL1=False
                #buyorder.append([[buys1[-1]],[i]])
                takeL1.append(i)
        
        if open_posL2 == False:
            if table600.Lower2.iloc[i]>table600.Low.iloc[i]:
                table600.Buy_Signal2.iloc[i] = True
                open_posL2=True
                buys2.append(i)
                signals=signals+1
        elif open_posL2 == True:
            if table600.MA.iloc[i]*0.999<table600.High.iloc[i]:
                table600.Buy_Signal2.iloc[i] = False
                table600.Take_Signal.iloc[i] = True
                open_posL2=False
                #buyorder.append([[buys2[-1]],[i]])
                takeL2.append(i)

        if open_posL3 == False:
            if table600.Lower3.iloc[i]>table600.Low.iloc[i]:
                table600.Buy_Signal3.iloc[i] = True
                open_posL3=True
                buys3.append(i)
                signals=signals+1
        elif open_posL3 == True:
            if table600.MA.iloc[i]*0.999<table600.High.iloc[i]:
                table600.Buy_Signal3.iloc[i] = False
                table600.Take_Signal.iloc[i] = True
                open_posL3=False
                #buyorder.append([[buys3[-1]],[i]])
                takeL3.append(i)
#--------------------------------------------------------------------------------------#
        
        if open_posU1 == False:
            if table600.Upper1.iloc[i]<table600.High.iloc[i]:
                table600.Sell_Signal1.iloc[i] = True
                open_posU1=True
                sells1.append(i)
                signals=signals+1
        elif open_posU1 == True:
            if table600.MA.iloc[i]*1.001>table600.Low.iloc[i]:
                table600.Sell_Signal1.iloc[i] = False
                table600.Take_Signal.iloc[i] = True
                open_posU1=False
                #sellorder.append([[sells1[-1]],[i]])
                takeU1.append(i)

        if open_posU2 == False:
            if table600.Upper2.iloc[i]<table600.High.iloc[i]:
                table600.Sell_Signal2.iloc[i] = True
                open_posU2=True
                sells2.append(i)
                signals=signals+1
        elif open_posU2 == True:
            if table600.MA.iloc[i]*1.001>table600.Low.iloc[i]:
                table600.Sell_Signal2.iloc[i] = False
                table600.Take_Signal.iloc[i] = True
                open_posU2=False
                #sellorder.append([[sells2[-1]],[i]])
                takeU2.append(i)

        if open_posU3 == False:
            if table600.Upper3.iloc[i]<table600.High.iloc[i]:
                table600.Sell_Signal3.iloc[i] = True
                open_posU3=True
                sells3.append(i)
                signals=signals+1
        elif open_posU3 == True:
            if table600.MA.iloc[i]*1.001>table600.Low.iloc[i]:
                table600.Sell_Signal3.iloc[i] = False
                table600.Take_Signal.iloc[i] = True
                open_posU3=False
                #sellorder.append([[sells3[-1]],[i]])
                takeU3.append(i)
    
         
   # print("buyorders:", buyorder)  
   # print("sellorders:", sellorder)  
    #print("Всего сигналов")
    #print(signals)
    #print("Расчет..")
    profit1 = pd.concat([table600.Lower1[buys1], 0.999*table600.MA[takeL1]],axis=1)
    #profit1.to_excel("Lower1.xlsx")
    profit2 = pd.concat([table600.Lower2[buys2], 0.999*table600.MA[takeL2]],axis=1)
    #profit2.to_excel("Lower2.xlsx")
    profit3 = pd.concat([table600.Lower3[buys3], 0.999*table600.MA[takeL3]],axis=1)
    #profit3.to_excel("Lower3.xlsx")
    profit4 = pd.concat([table600.Upper1[sells1], 1.001*table600.MA[takeU1]],axis=1)
    #profit4.to_excel("Upper1.xlsx")
    profit5 = pd.concat([table600.Upper2[sells2], 1.001*table600.MA[takeU2]],axis=1)
    #profit5.to_excel("Upper2.xlsx")
    profit6 = pd.concat([table600.Upper3[sells3], 1.001*table600.MA[takeU3]],axis=1)
    #profit6.to_excel("Upper3.xlsx")

    avarage = table600.Close.mean()
    #print ("Средняя цена")
   # print (avarage)       #средняя цена
    koef = sizep/avarage           
    
    #profit = pd.concat([profit1,profit2,profit3,profit4,profit5,profit6])
    #profit = profit.sort_index()
    #profit.columns = ['Buys','Sells']
    #print("Profit1")
    #print(profit1)
    #print("Profit2")
   # print(profit2)
   # print("Profit3")
   # print(profit3)
  #  print("Profit4")
   # print(profit4)
  #  print("Profit5")
   # print(profit5)
   # print("Profit6")
    #print(profit6)

    totalprofit1 = profit1.shift(-1).MA - profit1.Lower1
    
    totalprofit2 = profit2.shift(-1).MA - profit2.Lower2
   
    totalprofit3 = profit3.shift(-1).MA- profit3.Lower3
    

    totalprofit4 = profit4.Upper1 - profit4.shift(-1).MA
   
    totalprofit5 = profit5.Upper2 - profit5.shift(-1).MA
    
    totalprofit6 = profit6.Upper3 - profit6.shift(-1).MA
    #print("Lower1")
    #print(totalprofit1)
    #print("Lower2")
    #print(totalprofit2)
    #print("Lower3")
    #print(totalprofit3)
    #print("Upper1")
    #print(totalprofit4)
    #print("Upper2")
    #print(totalprofit5)
    #print("Upper3")
    #print(totalprofit6)

    totalprofitall = totalprofit1.sum() + totalprofit2.sum() + totalprofit3.sum() + totalprofit4.sum() + totalprofit5.sum() + totalprofit6.sum() 

    #print(totalprofitall)

        #if open_pos == False :
          #  table600['Buy_Signal1'] = np.where(table600.Lower1>table600.Low,True,False)
         #   table600['Sell_Signal1'] = np.where(table600.Upper1<table600.High,True,False)

           # table600['Buy_Signal2'] = np.where(table600.Lower2>table600.Low,True,False)
          #  table600['Sell_Signal2'] = np.where(table600.Upper2<table600.High,True,False)

           # table600['Buy_Signal3'] = np.where(table600.Lower3>table600.Low,True,False)
           # table600['Sell_Signal3'] = np.where(table600.Upper3<table600.High,True,False)

    #if open_pos == True 
    #print(table600['Buy_Signal1'])
    totalprofitallwithkoef = totalprofitall*koef
    print("Профит")
    print(totalprofitallwithkoef)
    '''
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
    '''
    return totalprofitallwithkoef