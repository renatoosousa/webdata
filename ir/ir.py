#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 16:56:53 2017

@author: renato
"""
from collections import Counter
import itertools
import math
import pickle
import scipy.stats

class IR(object):
    
    def __init__(self):
        self.rank = []
        self.rank_tdidf = []
        self.allPostings = self.getPostings()
        self.docs_vect = self.termAtTime()
        self.request = {}
        
    def setRequest(self, dic):
        self.request = dic
        
    def tfidf(self):
        return 5

    def parser(self):
        # quartos 1 2 3 4 5 6
        rangeqts = [1,2,3,4,5,6]
        # banheiro 1 2 3 4 5 6
        rangebanheiro = [0,1,2,3,4,5,6]
        # vaga 1 2 3 4 5
        rangevaga = [1,2,3,4,5]
        # valor
        # 480-10k 10k-135k 135k-225.5k 225.5k-330k 330k-480k 480k-650k 650k-850k 850k-980k
        #980k-1.6kk 1.6kk-2.2kk 2.2kk-3.8kk 3.8kk+
        rangevalor = [(480,10000), (10000,135000), (135000,225500), (225500,330000),
                      (330000,480000), (480000,650000), (650000,850000), (850000,980000),
                      (980000,1600000), (1600000,2200000), (2200000,3800000), (3800000,3800000*5)]
        # cidade
        rangecidade = ['pe','novo hamburgo','canoas','df','joão pessoa','sp','natal',
                       'rio de janeiro','itapevi','goiana','praia do pai',
                       'jaboatão dos guararapes','belo horizonte','são paulo','porto alegre',
                       'barueri','recife','avenida vice','manoel ribeiro,maricá']
        qry = []
        
        # Banheiros
        for value in rangebanheiro:
            if(self.request.get('banheiros') == value):
                qry.append(1)
            else:
                qry.append(0)
                
        # Cidadde
        for value in rangecidade:
            if(self.request.get('cidade') == value):
                qry.append(1)
            else:
                qry.append(0)
        
        # Quartos
        for value in rangeqts:
            if(self.request.get('quartos') == value):
                qry.append(1)
            else:
                qry.append(0)
                
        # Vagas
        for value in rangevaga:
            if(self.request.get('vaga') == value):
                qry.append(1)
            else:
                qry.append(0)
                
        # Valor
        for value in rangevalor:
            if(self.request.get('valor') >= value[0] and self.request.get('valor') < value[1]):
                qry.append(1)
            else:
                qry.append(0)
        
        return qry

    def parser2(self):
        # quartos 1 2 3 4 5 6
        rangeqts = [1,2,3,4,5,6]
        # banheiro 1 2 3 4 5 6
        rangebanheiro = [0,1,2,3,4,5,6]
        # vaga 1 2 3 4 5
        rangevaga = [1,2,3,4,5]
        # valor
        # 480-10k 10k-135k 135k-225.5k 225.5k-330k 330k-480k 480k-650k 650k-850k 850k-980k
        #980k-1.6kk 1.6kk-2.2kk 2.2kk-3.8kk 3.8kk+
        rangevalor = [(480,10000), (10000,135000), (135000,225500), (225500,330000),
                      (330000,480000), (480000,650000), (650000,850000), (850000,980000),
                      (980000,1600000), (1600000,2200000), (2200000,3800000), (3800000,3800000*5)]
        # cidade
        rangecidade = ['pe','novo hamburgo','canoas','df','joão pessoa','sp','natal',
                       'rio de janeiro','itapevi','goiana','praia do pai',
                       'jaboatão dos guararapes','belo horizonte','são paulo','porto alegre',
                       'barueri','recife','avenida vice','manoel ribeiro,maricá']
        qry = []
        
        # Banheiros
        for value in rangebanheiro:
            if(self.request.get('banheiros') == value):
                qry.append(1)
            else:
                qry.append(0)
                
        # Cidadde
        for value in rangecidade:
            if(self.request.get('cidade') == value):
                qry.append(self.tfidf())
            else:
                qry.append(0)
        
        # Quartos
        for value in rangeqts:
            if(self.request.get('quartos') == value):
                qry.append(1)
            else:
                qry.append(0)
                
        # Vagas
        for value in rangevaga:
            if(self.request.get('vaga') == value):
                qry.append(1)
            else:
                qry.append(0)
                
        # Valor
        for value in rangevalor:
            if(self.request.get('valor') >= value[0] and self.request.get('valor') < value[1]):
                qry.append(1)
            else:
                qry.append(0)
        
        return qry
    
    def getPostings(self):
        '''
        BANHEIROS
        0:  [316]
        1:  [257, 258, 259, 260, 261, 262, 265, 266, 268, 271, 274, 275, 278, 293, 315, 317, 325, 326, 328, 329, 331, 334, 335, 338, 347, 350, 351, 352, 353, 354]
        2:  [255, 264, 276, 277, 294, 295, 298, 300, 303, 304, 321, 339, 344, 345]
        3:  [263, 267, 279, 281, 282, 283, 286, 296, 297, 318, 336, 340, 342, 343]
        4:  [269, 270, 333]
        5:  [280, 291, 292, 319, 324, 337, 341]
        6:  [284, 290, 320, 323]
        CIDADE
        pe:  [344]
        novo hamburgo:  [348]
        canoas:  [308]
        df:  [341]
        joão pessoa:  [267, 269]
        sp:  [335]
        natal:  [310]
        rio de janeiro:  [270, 293, 294, 303, 337]
        itapevi:  [309]
        goiana:  [322]
        praia do pai:  [259]
        jaboatão dos guararapes:  [266, 307]
        belo horizonte:  [298, 300, 340]
        são paulo:  [281, 282, 283, 284, 287, 288, 289, 290, 291, 292, 295, 296, 336]
        porto alegre:  [277, 278, 279, 280, 313, 345]
        barueri:  [305]
        recife:  [255, 257, 258, 260, 261, 262, 263, 264, 274, 275, 276, 297, 311, 319, 320, 321, 343, 352, 353, 354]
        avenida vice:  [304]
        manoel ribeiro, maricá:  [312]
        QUARTOS
        1:  [262, 312, 327, 329] 
        2:  [255, 265, 272, 273, 278, 286, 293, 300, 303, 305, 308, 311, 313, 316, 321, 330, 331, 332, 334, 335, 338, 339, 345, 348, 350, 352, 353]
        3:  [258, 259, 260, 261, 264, 266, 267, 268, 271, 274, 275, 276, 277, 279, 281, 282, 283, 285, 288, 292, 294, 295, 296, 297, 304, 307, 309, 310, 315, 318, 326, 328, 336, 341, 342, 343, 344, 347, 354]
        4:  [263, 269, 270, 280, 284, 290, 291, 298, 317, 319, 325, 333, 337, 340]
        5:  [320, 324]
        6:  [323]
        VAGAS
        1:  [260, 262, 265, 271, 275, 278, 295, 307, 308, 316, 317, 321, 324, 326, 327, 328, 329, 330, 331, 334, 335, 342, 344, 350, 352, 353]
        2:  [255, 258, 259, 261, 263, 264, 268, 274, 276, 277, 279, 282, 291, 296, 297, 298, 300, 310, 315, 318, 319, 336, 340, 341, 343, 345, 347, 351, 354]
        3:  [266, 270, 281, 283, 284, 320, 333, 339]
        4:  [280, 290, 337]
        5:  [257, 267, 269, 323, 325]
        VALOR
        330k-480k:  [260, 274, 277, 278, 303, 316, 317, 331]
        135k-225.5k:  [272, 273, 275, 307, 313, 328, 335, 348]
        2.2kk-3.8kk:  [270, 280, 295, 320]
        1.6kk-2.2kk:  [267, 294, 296]
        480-10k:  [257, 262, 263, 298, 309, 310, 311, 312, 329, 330, 333, 339, 340, 345, 352, 353, 354]
        650k-850k:  [259, 264, 266, 271, 282, 292, 304, 315, 336, 343]
        980k-1.6kk:  [279, 285, 291, 342, 347]
        480k-650k:  [255, 276, 286, 297, 300, 318, 332]
        3.8kk+:  [269, 290, 323, 324, 337]
        10k-135k:  [305, 338]
        225.5k-330k:  [258, 265, 308, 321, 326, 327, 334, 344]
        850k-980k:  [261, 268, 281, 283, 284, 293, 319, 325]
        '''
        full = []
        
        f = open("../extractor/study_codes/reverse_index.txt", "r")
        for i in range(0,49):
            full.append(pickle.load(f))
        return full
        
    # Transform docs to vector
    def termAtTime(self):
        alldict = []
        for posting in self.allPostings:
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
    
    def vectorSpace(self, doc, qry):
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
    
    def ranking(self):
        query = self.parser()
        result = {}    
        for key in self.docs_vect:
            result.setdefault(key,self.vectorSpace(self.docs_vect[key],query))
        self.rank = sorted(result.items(), key=lambda x:x[1], reverse=True)

    def ranking_tfidf(self):
        query = self.parser2()
        result = {}    
        for key in self.docs_vect:
            result.setdefault(key,self.vectorSpace(self.docs_vect[key],query))
        self.rank_tfidf = sorted(result.items(), key=lambda x:x[1], reverse=True)
        
    def getInfo(self, n = 10, tfidf = True):
        path = '../extractor/study_codes/results/docs/doc_'
        return_docs = []
        temp = []
        if(tfidf):
            temp = self.rank_tfidf
        else:
            temp = self.rank
        for tp in temp:
            file = open(path + str(tp[0]) +'.txt', 'r')
            return_docs.append(file.read())
            if(len(return_docs) >= n):
                break
        return return_docs
    
    def spearman(self):
        r1 = [int(i[0]) for i in self.rank]
        r2 = [int(i[0]) for i in self.rank_tfidf]
        _sum = 0
        if(len(r1) == len(r2)):
            for doc in r1:
                _sum += math.pow((r1.index(doc) - r2.index(doc)),2)
            _sum *= 6.0 / (math.pow(len(r1),3) - math.pow(len(r1),2))
        else:
            print("sizes dont match")
            
#        return 1 - _sum
        return scipy.stats.stats.spearmanr(r1,r2)[0]
    
    def combinations(self,l):
        return list(itertools.combinations(l,2))

    def kendalTau(self):
        r1 = [int(i[0]) for i in self.rank]
        r2 = [int(i[0]) for i in self.rank_tfidf]
        delta = len(list(set(self.combinations(r1)).difference(self.combinations(r2))))
#        return 1 - (2.0 * delta)/(len(r1) * (len(r1)-1)) 
        return scipy.stats.stats.kendalltau(r1,r2)[0]
    