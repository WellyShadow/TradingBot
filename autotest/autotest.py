
import pandas as pd
from autotest import requestfromautotest

def autotest(symbol):
    profitv1 = {}
    profitv2_001 = {}
    profitv2_003 = {}
    #profitv4 = {}
    #profitv5_001 = {} #1_003
    #profitv5_003 = {}
    df = pd.DataFrame(columns=['month'])
    #profitv1,profitv2_001,profitv2_003,profitv4,profitv5_001,profitv5_003 = requestfromautotest.logics(symbol)
    print(symbol)
    profitv1 = requestfromautotest.logics(symbol)
    #df = pd.DataFrame(profitv1.items(), columns=['month', 'version1'])
    df = df.set_index('month')
    df['version1'] = profitv1
    #df['version2_001'] = profitv2_001
    #df['version2_003'] = profitv2_003
    #df['version4'] = profitv4
    #df['version5_001'] = profitv5_001
    #df['version5_003'] = profitv5_003
    df.to_excel('tables/55_98_735_45/logicv1ATRMACD/PERPUSDT/'+symbol+'.xlsx')
   