import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#create a series
s=pd.Series([1,3,5,np.nan,6,8,])
print(s)

#create a DataFrame
datas=pd.date_range('20130101', periods=6)
print(datas)


#create a dataframe by passing dictionary of obj
df=pd.DataFrame({
"A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
})
print(df)

#get the type of df (obj)
print(df.dtypes)

#buttom rows
print(df.head())

#top rows
print(df.tail())

#index
print(df.index)

#column
print(df.columns)

#convert to nmpy array
print(df.to_numpy())

#static of data
print(df.describe())

#sort by axis(asse)
print(df.sort_index(axis=1, ascending=False)) #asceding = ascendente

#sort by value
print(df.sort_values(by="B"))











