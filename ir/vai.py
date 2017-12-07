#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 21:21:01 2017

@author: renato
"""

from ir import IR

score = IR()
request = {"cidade": "recife", "quartos": 4, "banheiros": 2, "valor": 1000, "vaga": 3}

score.setRequest(request)

score.ranking()
score.ranking_tfidf()

print score.spearman()
print score.kendalTau()
# print score.rank

renato = score.getInfo()