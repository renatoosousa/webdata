import pandas as pd 

data = pd.read_csv("/home/cso/Documents/webdata/classifier/dataframe/urls2.csv", delimiter = ',')
data_tuple = [tuple(x) for x in data.values]
# dicts = data.to_dict().values()
# print tuples
# print dicts


