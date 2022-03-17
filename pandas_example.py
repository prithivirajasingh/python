#!/usr/bin/env python
import pandas

data= pandas.read_csv("products.csv")     # stores the csv as dataframe
print(type(data))
print(data)
print(data.iat[0, 0])   # returns 0,0 element
print(data.shape[0])    # returns row count
print(data.shape[0])    # returns column count
exit()

