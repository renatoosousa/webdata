#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:56:18 2017

@author: renato
"""
import random
from collections import Counter
import math
import operator

def termAtTime(l1, l2, l3):
    d1 = Counter(l1)
    d2 = Counter(l2)
    d3 = Counter(l3)
    alldict = [d1,d2,d3]
    
    result = {}
    allkey = reduce(lambda x, y: x.union(y.keys()), alldict, set())
    
    for dic in alldict:
        for key in (result.viewkeys() | allkey):
            if key in dic:
                result.setdefault(key, []).append(dic[key])
            else: 
                result.setdefault(key, []).append(0)
    
    return result

def vectorSpace(doc,qry):
    score = 0
    num = 0
    denA = 0
    denB = 0
    if(len(doc) == len(qry)):
        for i in range(0,len(doc)):
            num += doc[i]*qry[i]
            denA += doc[i]**2
            denB += qry[i]**2
        score = float(num)/math.sqrt(denA*denB)
    return score

def ranking(dic, query):
    result = {}
    
    for key in dic:
        result.setdefault(key,vectorSpace(dic[key],query))
        
    return result

qts = random.sample(range(20), 10)
area = random.sample(range(20), 10)
local = random.sample(range(20), 10)
qts.sort()
area.sort()
local.sort()
query = [1,0,1]

# Reading Postings
vectorized = termAtTime(qts,area,local)

#ranking all docs
rank = ranking(vectorized,query)