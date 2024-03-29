#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 23:18:11 2017

@author: renato
"""

import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
import time

dfs = ['../../dataframe/db2.csv', '../../dataframe/db3.csv', '../../dataframe/db4.csv', '../../dataframe/db6.csv', '../../dataframe/db7.csv', '../../dataframe/db8.csv']
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000] }
clft = GridSearchCV(linear_model.LogisticRegression(penalty='l2'), param_grid)


for path in dfs:
    print('\n\n' + path)
    df = pd.read_csv(path, sep='\t')
    X = df.ix[:,:df.shape[1]-2]
    y = df.ix[:,df.shape[1]-1]
    
    X = X.values
    y = y.values
    
    print("Tuning...")
    clft.fit(X,y)
    print(clft.best_params_)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    
    clf = linear_model.LogisticRegression(C=(clft.best_params_)['C'])
    folders = 10
    scores = cross_val_score(clf, X, y, cv=folders)
    #print(scores)
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    
    scores = cross_val_score(clf, X, y, cv=folders, scoring='precision')
    #print(scores)
    print("Precision: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    
    scores = cross_val_score(clf, X, y, cv=folders, scoring='recall')
    #print(scores)
    print("Recall: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    
    start_time = time.time()
    clf.fit(X_train, y_train)
    end_time = time.time()
    print("fit time %g seconds" % (end_time - start_time))
    
