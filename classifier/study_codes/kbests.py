#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 21:13:42 2017

@author: renato
"""

import pandas as pd
import numpy as np
import operator
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

def row2col(a):
    aux = np.zeros(shape=(a.shape[0],1))
    for i in range(a.shape[0]):
        aux[i,0] = a[i]
    return aux

def select_kbest(dfx, dfy):
    columns = dfx.columns
    selector = SelectKBest(chi2, k=1000)
    selector.fit_transform(dfx,dfy)
    labels = [columns[x] for x in selector.get_support(indices=True) if x]
    return pd.DataFrame(selector.fit_transform(dfx, dfy), columns=labels)


df6 = pd.read_csv('../dataframe/db6.csv', sep = '\t')

'''
make df7 dataframe
'''
#headers = list(df6.columns.values)
#headers.remove('label')
#headers.remove('Unnamed: 0')
#
#df6x = df6[headers]
#df6y = df6['label']
#
#df7 = select_kbest(df6x,df6y)
#df7['label'] = df6y
#df7.to_csv('../dataframe/db7.csv', sep='\t', encoding = 'utf-8')


'''
make df8 dataframe
'''
headers = list(df6.columns.values)
headers.remove('label')
headers.remove('Unnamed: 0')

freq = dict((el,int(df6[el].sum())) for el in headers)
sorted_freq = sorted(freq.items(), key=operator.itemgetter(1))
k_freq = sorted_freq[-1000:]

new_headers = [i[0] for i in k_freq]

df8 = df6[new_headers]
df8['label'] = df6['label']
df8.to_csv('../dataframe/db8.csv', sep='\t', encoding = 'utf-8')


#df6 = df6.drop('Unnamed: 0', axis=1)
#labels = row2col(df6['label'].values)
#df6 = df6.drop('label', axis=1)
#
#a = df6.values
#b = np.sum(a, axis=0)
#idx = b.argsort()
#r = np.take(a,idx,axis=1)
#s = r[:,r.shape[1]-1001:r.shape[1]-1]
#s = np.append(s,labels, axis=1)
#df8 = pd.DataFrame(s)
#df8.to_csv('../dataframe/db8.csv', sep='\t', encoding = 'utf-8')
