#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 22:30:49 2017

@author: renato
"""

import sys
sys.path.append('/home/renato/Desktop/code/webdata/classifier/study_codes')
from classify import Classify

classif = Classify()
label = classif.setWebpage('https://www.zapimoveis.com.br/')
print(classif.pred())