import pandas as pd
import numpy as np
df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=['Row1','Row2','Row3','Row4','Row5'],columns=["Column1","Column2","Column3","Coumn4"])
print(df.head())
print(df.loc['Row2'])
print(type(df.loc['Row1']))
print(type(df))
print(df.iloc[:,2:])
print(df.iloc[:,1:].values)
df1=pd.read_csv('TST.csv')
print(df1.iloc[:,1:])
