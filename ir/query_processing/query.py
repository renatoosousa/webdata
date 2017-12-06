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

def parser(request):
    # quartos 1 2 3 4 5 6
    rangeqts = [1,2,3,4,5,6]
    # banheiro 1 2 3 4 5 6
    rangebanheiro = [1,2,3,4,5,6]
    # vaga 1 2 3 4 5
    rangevaga = [1,2,3,4,5]
    # valor
    # cidade
    qry = []
    # Quartos
    for value in rangeqts:
        if(request.get('quartos') == value):
            qry.append(1)
        else:
            qry.append(0)
    
    # Banheiros
    for value in rangebanheiro:
        if(request.get('banheiros') == value):
            qry.append(1)
        else:
            qry.append(0)
            
    # vagas
    for value in rangevaga:
        if(request.get('vaga') == value):
            qry.append(1)
        else:
            qry.append(0)
    return qry

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
qts5 = random.sample(range(20), 14)
qts6 = random.sample(range(20), 12)
area1 = random.sample(range(20), 5)
area2 = random.sample(range(20), 17)
area3 = random.sample(range(20), 3)
area4 = random.sample(range(20), 5)
area5 = random.sample(range(20), 3)
area6 = random.sample(range(20), 5)
local1 = random.sample(range(20), 15)
local2 = random.sample(range(20), 15)
local3 = random.sample(range(20), 10)
local4 = random.sample(range(20), 15)
local5 = random.sample(range(20), 10)

qts1.sort()
qts2.sort()
qts3.sort()
qts4.sort()
qts5.sort()
qts6.sort()
area1.sort()
area2.sort()
area3.sort()
area4.sort()
area5.sort()
area6.sort()
local1.sort()
local2.sort()
local3.sort()
local4.sort()
local5.sort()


request = {"cidade": "Recife", "quartos": 4, "banheiros": 2, "valor": 1000, "vaga": 3}

allPostings = [qts1,qts2,qts3,qts4,qts5,qts6,area1,area2,area3,area4,area5,area6,local1,local2,local3,local4,local5]

query = parser(request)

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
#print(parser(request))
