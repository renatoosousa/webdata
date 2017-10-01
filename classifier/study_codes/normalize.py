#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 11:32:29 2017

@author: renato
"""

import pandas as pd
from tqdm import tqdm

#print("begin")
df = pd.read_csv('../dataframe/db1.csv', sep = '\t')
#print("read csv sucess")
#df = pd.DataFrame({'a': [1,2,3], 'b': [2,3,4], 'c':[1,2,3], 'd':[5,9,1]})
#col_list = list(df)
#col_list.remove('d')
#sums = (df[col_list].sum(axis=1)).values
#for i in range(df.shape[0]):
#    df.loc[i,col_list] /= sums[i] 


col_list = list(df)
col_list.remove('label')
#print("remove column _label")
#col_list.remove('Unnamed: 0')
#print("remove column _index")
sums = (df[col_list].sum(axis=1)).values
for i in range(len(sums)):
    sums[i] = sums[i] - (i+1)
#print("calculate sum of each row sucess")
for i in tqdm(range(0,df.shape[0])):
    df.loc[i,col_list] /= sums[i]
#print("calculate sucess")
df.to_csv('../dataframe/db1N.csv', sep='\t', encoding = 'utf-8')
print("save db1n")    
#labels = (df['label']).values

df2 = pd.read_csv('../dataframe/db2.csv', sep = '\t')
col_list = list(df2)
col_list.remove('label')
for i in tqdm(range(0,df2.shape[0])):
    df2.loc[i,col_list] /= sums[i]
df2.to_csv('../dataframe/db2N.csv', sep='\t', encoding = 'utf-8')
print("save db2n")

df3 = pd.read_csv('../dataframe/db3.csv', sep = '\t')
col_list = list(df3)
col_list.remove('label')
for i in tqdm(range(0,df3.shape[0])):
    df3.loc[i,col_list] /= sums[i]
df3.to_csv('../dataframe/db3N.csv', sep='\t', encoding = 'utf-8')
print("save db3n")

df4 = pd.read_csv('../dataframe/db4.csv', sep = '\t')
col_list = list(df4)
col_list.remove('label')
for i in tqdm(range(0,df4.shape[0])):
    df4.loc[i,col_list] /= sums[i]
df4.to_csv('../dataframe/db4N.csv', sep='\t', encoding = 'utf-8')
print("save db4n")

df5 = pd.read_csv('../dataframe/db5.csv', sep = '\t')
col_list = list(df5)
col_list.remove('label')
for i in tqdm(range(0,df5.shape[0])):
    df5.loc[i,col_list] /= sums[i]
df5.to_csv('../dataframe/db5N.csv', sep='\t', encoding = 'utf-8')
print("save db5n")

df6 = pd.read_csv('../dataframe/db6.csv', sep = '\t')
col_list = list(df6)
col_list.remove('label')
for i in tqdm(range(0,df6.shape[0])):
    df6.loc[i,col_list] /= sums[i]
df6.to_csv('../dataframe/db6N.csv', sep='\t', encoding = 'utf-8')
print("save db6n")