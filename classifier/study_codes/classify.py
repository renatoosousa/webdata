#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 22:12:10 2017

@author: renato
"""

import pandas as pd
import numpy as np
import sys
sys.path.append('../../extractor/study_codes/')
from zapi_bs import Zapi_crawler
from nltk.stem import RSLPStemmer
import pickle
# list(my_dataframe.columns.values)
 
class Classify(object):
    def __init__(self,):
            self.words = self.getHeaders()
            self.txt ='init'
            self.forest = self.openclassify()
    
    def getHeaders(self):
        headers = list((pd.read_csv('../dataframe/db6.csv', sep='\t', encoding = 'utf8')).columns.values)
        headers.remove('Unnamed: 0')
        headers.remove('label')
#        headers = [x.encode('utf-8') for x in headers]
        return headers
    
    def openclassify(self):
        with open('../classifiers/Trained.pkl', 'rb') as f:
            rf = pickle.load(f)
        return rf
    
    def filter_txt(self,txt):
        stopw = (open('../study_codes/stopwords.txt', 'r')).read()
        for word in stopw.split():
            txt = txt.replace(" "+word+" "," ")
        txt = txt.decode('utf-8')
   
   
        splits = [',', '(', ')', '[', ']', '.', '!', '?', ';', ':', '/', '|', '"',
              '+', '-', '_', '#', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
              '\'', '\\', '\t', '\n', '>', '<', '*']
 
        for split in splits:
            txt = txt.replace(split, ' ')
   
        st = RSLPStemmer()
        txt2 = ""
        for token in txt.split():
            txt2 = txt2 + ' ' + (st.stem(token))
       
        return txt2
 
    def setWebpage(self, webpage):
        wrapper = Zapi_crawler(webpage)
        self.txt = self.filter_txt(wrapper.get_rawHtml().lower())
 
    def countWord(self, key):
        count = 0      
        for word in (self.txt).split():
            if(key == word):
                count += 1
            else:
                count += 0
        return count
 
    def pred(self,):
        X = []
        for header in self.words:
            X.append(self.countWord(header))
        X = np.array(X)
        resp = self.forest.predict(X.reshape(1, -1))
        return (resp.astype(np.int64))[0]