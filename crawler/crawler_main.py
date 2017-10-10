import pandas as pd
import sys
sys.path.append('../classifier/study_codes')
from classify import Classify

classif = Classify()
label = classif.setWebpage('https://www.zapimoveis.com.br/')
print label
print (classif.pred())