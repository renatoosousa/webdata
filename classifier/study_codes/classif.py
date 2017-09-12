#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 22:18:17 2017

@author: renato
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('database.csv', sep='\t')
X = df.ix[:,:df.shape[1]-2]
y = df.ix[:,df.shape[1]-1]

X = X.values
y = y.values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

forest = RandomForestClassifier(n_estimators=500, random_state=0)
forest.fit(X_train, y_train)

score1 = forest.score(X_train, y_train)
score2 = forest.score(X_test, y_test)
print("accuracy on training set: %f" % forest.score(X_train, y_train))
print("accuracy on test set: %f" % forest.score(X_test, y_test))