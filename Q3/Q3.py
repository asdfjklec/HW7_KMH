import numpy as np
import pandas as pd
from pandas import DataFrame as DF  

def main():
    data = {
        'unit price' : [1000, 280 , 900],
        'number' : [ 25, 120, 30]
    }
    df =DF(data, index=['store1', 'store2', 'store3'])
    display(df)
    df['total price']=df['unit price']*df['number']
    display(df)
    df = df.sort_values(by='total price', ascending=False)
    display(df[0:2])
    
    
    
if __name__ == '__main__':
    main()
