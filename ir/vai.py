#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 21:21:01 2017

@author: renato
"""

from ir import IR

score = IR()
request1 = {'banheiros': 3, 'cidade': 'sp', 'vaga': 1, 'quartos': 1, 'valor': 160000}
request2 = {'banheiros': 1, 'cidade': 'belo horizonte', 'vaga': 2, 'quartos': 4, 'valor': 500}
score.setRequest(request1)
score.ranking()
a = score.rank
score.setRequest(request2)
score.ranking()
score.rank_tfidf = a
print score.spearman()
print score.kendalTau()
# print score.rank

renato = score.getInfo()