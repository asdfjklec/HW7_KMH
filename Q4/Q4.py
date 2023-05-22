import numpy as np
import pandas as pd
from pandas import DataFrame as DF  

def main():
    
    

    df1 = pd.read_csv('gender2.csv', encoding='cp949', usecols=[0,1], index_col=[0])
    df2 = pd.read_csv('gender2.csv', encoding='cp949', usecols=[0,6], index_col=[0])
    df3 = pd.read_csv('gender2.csv', encoding='cp949', usecols=[0,11], index_col=[0])
    
    #ij1 = pd.merge(df1,df2, on='행정구역')
    ij1 = pd.merge(df1, df2 , on='행정구역')
    ij2 = pd.merge(ij1, df3 , on='행정구역' )
    
    ij2.rename(columns = {'2022년_계_총인구수':'Total',
                          '2022년_남_총인구수':'Male', 
                          '2022년_여_총인구수':'Female'},
              inplace=True)
    
    
    #display(df1, df2, df3)
    display(ij2)
    





if __name__ == '__main__':
    main()


