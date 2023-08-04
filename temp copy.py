import logicv1forbasictest
import pandas as pd
import BasicKoefTest.basicbacktest as basicbacktest
import numpy as np
import itertools

def calculate_profit(df):
    i_values = np.arange(10, 200)
    koef1_values = np.arange(2, 12)
    koef3_values = np.arange(4, 14)
    combinations = itertools.product(i_values, koef1_values, koef3_values)
    results = []
    for i, koef1, koef3 in combinations:
        koef2 = (koef1 + koef3) / 2
        profit, _ = logicv1forbasictest.history(i, koef1, koef2, koef3, df)
        print(profit, i, koef1, koef2, koef3)
        results.append({'profit': profit, 'length': i, 'koef1': koef1, 'koef2': koef2, 'koef3': koef3})
    print('за циклом')
    profittable = pd.DataFrame(results)
    return profittable


def main(): 
    df = basicbacktest.klinestest('BTCUSDT', "1 Jan 2020", "1 Feb 2023")
    profittable = calculate_profit(df)
    profittable.to_excel("1.xlsx")


if __name__ == '__main__':
    main()
