#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 21:13:42 2017

@author: renato
"""

import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

def row2col(a):
    aux = np.zeros(shape=(a.shape[0],1))
    for i in range(a.shape[0]):
        aux[i,0] = a[i]
    return aux

df6 = pd.read_csv('../dataframe/db6.csv', sep = '\t')

#a = df6.values
#X = a[:,:a.shape[1]-1]
#y = a[:,a.shape[1]-1]
#print(X.shape)
#X_new = SelectKBest(chi2, k=1000).fit_transform(X, y)
#print(X_new.shape)
#new_df = np.append(X_new,row2col(y), axis=1)
#df7 = pd.DataFrame(new_df)
#df7.to_csv('../dataframe/db7.csv', sep='\t', encoding = 'utf-8')


df6 = df6.drop('Unnamed: 0', axis=1)
labels = row2col(df6['label'].values)
df6 = df6.drop('label', axis=1)

a = df6.values
b = np.sum(a, axis=0)
idx = b.argsort()
r = np.take(a,idx,axis=1)
s = r[:,r.shape[1]-1001:r.shape[1]-1]
s = np.append(s,labels, axis=1)
df8 = pd.DataFrame(s)
df8.to_csv('../dataframe/db8.csv', sep='\t', encoding = 'utf-8')
