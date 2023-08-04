import logicv1forbasictestNocoefATR_MACD
import pandas as pd
import basicbacktest
import numpy as np
import pickle


def calculate_profit(df):

    #try:
    #    with open('progress.pkl', 'rb') as f:
    #        i, koef1, koef3, profittable, index = pickle.load(f)
    #except FileNotFoundError:
    profittable = pd.DataFrame(columns=['profit','length','koef1','koef2','koef3','profitfactor','signals'])
    #    i, koef1, koef3, index  = 10, 2, 4, 0 # начало цикла по умолчанию
    index = 0
    for i in range (15,20,1):
        for koef1 in np.arange (3,5,0.1):
            for koef3 in np.arange (koef1+2,10,0.1):
                koef2 = (koef1+koef3)/2
                profit,profitfactor,signals,_ = logicv1forbasictestNocoefATR_MACD.history(i,koef1,koef2,koef3,df)
                try:
                    print("Профит:",profit.values[0],' ',i,' ',koef1,' ',koef2,' ',koef3,' ',profitfactor.values[0],' ',signals)
                    profittable.loc[index] = profit.values[0],i,koef1,koef2,koef3,profitfactor.values[0],signals
                except: 
                    print("Профит:",profit.values[0],' ',i,' ',koef1,' ',koef2,' ',koef3,' ',profitfactor,' ',signals)
                    profittable.loc[index] = profit.values[0],i,koef1,koef2,koef3,profitfactor,signals
                #with open('progress.pkl', 'wb') as f:
                #    pickle.dump((i, koef1, koef3, profittable, index), f)
                index = index+1
                profittable.to_excel("15_20BTCTestMACDATRNocoef.xlsx")
                    

def main(): 
    table = basicbacktest.klinestest('BTCUSDT',"1 Jan 2021","1 Jan 2023")
    #table = pd.read_excel('BTCUSDT.xlsx')
    #table.set_index('Time', inplace=True)
    #print(table)
    calculate_profit(table)
if __name__ == '__main__':
    main()