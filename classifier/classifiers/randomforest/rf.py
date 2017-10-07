#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 21:57:09 2017

@author: renato
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import time

dfs = ['../../dataframe/db2.csv', '../../dataframe/db3.csv', '../../dataframe/db4.csv', '../../dataframe/db6.csv']

for path in dfs:
    print('\n\n' + path)
    df = pd.read_csv(path, sep='\t')
    X = df.ix[:,:df.shape[1]-2]
    y = df.ix[:,df.shape[1]-1]
    
    X = X.values
    y = y.values
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    
    forest = RandomForestClassifier(n_estimators=100, random_state=0)
    folders = 2
    scores = cross_val_score(forest, X, y, cv=folders)
    print(scores)
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    
    scores = cross_val_score(forest, X, y, cv=folders, scoring='precision_micro')
    print(scores)
    print("Precision: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    
    scores = cross_val_score(forest, X, y, cv=folders, scoring='recall_micro')
    print(scores)
    print("Recall: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    
    start_time = time.time()
    forest.fit(X_train, y_train)
    end_time = time.time()
    print("fit time %g seconds" % (end_time - start_time))
    