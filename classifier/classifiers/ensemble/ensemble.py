#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 14:00:31 2017

@author: renato
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn import linear_model
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import time

dfs = ['../../dataframe/db2.csv', '../../dataframe/db3.csv', '../../dataframe/db4.csv', '../../dataframe/db6.csv', '../../dataframe/db7.csv', '../../dataframe/db8.csv']

for path in dfs:
    print('\n\n' + path)
    df = pd.read_csv(path, sep='\t')
    X = df.ix[:,:df.shape[1]-2]
    y = df.ix[:,df.shape[1]-1]
    
    X = X.values
    y = y.values
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    
    clf1 = RandomForestClassifier(n_estimators=500, random_state=0)
    clf2 = linear_model.LogisticRegression(C=1e5)
    clf3 = svm.SVC()
    clf4 = GaussianNB()
    clf5 = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 10), random_state=1)
    
    eclf = VotingClassifier(estimators=[('rf', clf1),('mlp', clf5), ('svm', clf3)], voting='hard')
    
    folders = 10
    scores = cross_val_score(eclf, X, y, cv=folders)
#    print(scores)
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    
    scores = cross_val_score(eclf, X, y, cv=folders, scoring='precision')
#    print(scores)
    print("Precision: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    
    scores = cross_val_score(eclf, X, y, cv=folders, scoring='recall')
#    print(scores)
    print("Recall: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    
    start_time = time.time()
    eclf.fit(X_train, y_train)
    end_time = time.time()
    print("fit time %g seconds" % (end_time - start_time))
    