#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 22:17:02 2017

@author: renato
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv('../dataframe/db6.csv', sep='\t')
X = df.ix[:,:df.shape[1]-2]
y = df.ix[:,df.shape[1]-1]

X = X.values
y = y.values
    
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    
forest = RandomForestClassifier(n_estimators=500, random_state=0)

forest.fit(X, y)

print("accuracy on training set: %f" % forest.score(X_train, y_train))
print("accuracy on test set: %f" % forest.score(X_test, y_test))

with open('Trained.pkl', 'wb') as f:
    pickle.dump(forest, f)