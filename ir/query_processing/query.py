#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

@author: renato
"""
import random
from collections import Counter
import math
import itertools

# Transform docs to vector
def termAtTime(allPostings):
    alldict = []
    for posting in allPostings:
        alldict.append(Counter(posting))
    
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
    else:
        print("size of vectors dont match")
    return score

def ranking(dic, query):
    result = {}    
    for key in dic:
        result.setdefault(key,vectorSpace(dic[key],query))
    return sorted(result.items(), key=lambda x:x[1], reverse=True)    

def term_frequency(term, tokenized_document):
    return tokenized_document.count(term)

def inverse_document_frequencies(tokenized_documents):
    idf_values = {}
    all_tokens_set = set([item for sublist in tokenized_documents for item in sublist])
    for tkn in all_tokens_set:
        contains_token = map(lambda doc: tkn in doc, tokenized_documents)
        idf_values[tkn] = 1 + math.log(len(tokenized_documents)/(sum(contains_token)))
    return idf_values

def ranking_tfidf(vec,qry,post):
    
    return vec

def spearman(r1,r2):
    _sum = 0
    if(len(r1) == len(r2)):
        for doc in r1:
            _sum += math.pow((r1.index(doc) - r2.index(doc)),2)
        _sum *= 6.0 / (math.pow(len(r1),3) - math.pow(len(r1),2))
    else:
        print("sizes dont match")
        
    return 1 - _sum

def combinations(l):
    return list(itertools.combinations(l,2))
    

def kendalTau(r1,r2):
#    print len(combinations(r1))
    delta = len(list(set(combinations(r1)).difference(combinations(r2))))
    print delta
    return 1 - (2.0 * delta)/(len(r1) * (len(r1)-1)) 
        


qts1 = random.sample(range(20), 6)
qts2 = random.sample(range(20), 8)
qts3 = random.sample(range(20), 14)
qts4 = random.sample(range(20), 12)
area1 = random.sample(range(20), 5)
area2 = random.sample(range(20), 17)
area3 = random.sample(range(20), 3)
area4 = random.sample(range(20), 5)
local1 = random.sample(range(20), 15)
local2 = random.sample(range(20), 15)
local3 = random.sample(range(20), 10)

qts1.sort()
qts2.sort()
qts3.sort()
qts4.sort()
area1.sort()
area2.sort()
area3.sort()
area4.sort()
local1.sort()
local2.sort()

allPostings = [qts1,qts2,qts3,qts4,area1,area2,area3,area4,local1,local2]

query = [1,0,1,0,1,0,0,0,1,1]

# Reading Postings
vectorized = termAtTime(allPostings)
#
# Ranking all docs without tf-idf
rank = ranking(vectorized,query)

# Ranking all docs with tf-idf
#rank_tfidf = ranking_tfidf(vectorized,query,allPostings)

rank_tfidf = rank

spm = spearman([int(i[0]) for i in rank], [int(i[0]) for i in rank_tfidf])
kt = kendalTau([int(i[0]) for i in rank], [int(i[0]) for i in rank_tfidf])
