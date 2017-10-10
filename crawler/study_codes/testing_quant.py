import pandas as pd
import sys
sys.path.append('/home/cristiano/Documentos/Programming/webdata/classifier/study_codes')
from textblob.classifiers import NaiveBayesClassifier
from classify import Classify
import nltk
nltk.download('punkt')
import pickle

path_heuristic = '/home/cristiano/Documentos/Programming/webdata/crawler/heuristic_crawler/'
path_bfs = '/home/cristiano/Documentos/Programming/webdata/crawler/bfs_crawler/'

bfs_crawler_csv = [
	'bfs_buscaimoveis',
	'bfs_diariodepernambuco',
	'bfs_directimoveis',
	'bfs_expoimovel',
	'bfs_imovelweb',
	'bfs_olx',
	'bfs_redeimobiliariasecovi',
	'bfs_teuimovel',
	'bfs_vivareal',
	'bfs_zap',
	'bfs_zipanuncios'
	]
	
heuristic_crawler_csv =[
	'heuristic_buscaimoveis',
	'heuristic_diariodepernambuco',
	'heuristic_directimoveis',
	'heuristic_expoimovel',
	'heuristic_imovelweb',
	'heuristic_olx',
	'heuristic_redeimobiliariasecovi',
	'heuristic_teuimovel',
	'heuristic_vivareal',
	'heuristic_zap',
	'heuristic_zipanuncios'
] 


# print df.column.tolist()
with open('/home/cristiano/Documentos/Programming/webdata/crawler/study_codes/trained_count.pkl', 'rb') as f:
	clf_test = pickle.load(f)

def prob_func(link):
	prob_dist = clf_test.prob_classify(link)
	return round(prob_dist.prob(0),2)

# data_bfs = []
# data_heuristic = []
# for csv_arqui in bfs_crawler_csv:
# 	df = pd.read_csv(path_bfs+csv_arqui+'.csv')
# 	count = 0
# 	print csv_arqui
# 	for elem in df.column.tolist():
# 		classif = Classify()
# 		label = classif.setWebpage(elem)
# 		if classif.pred() == 1:
# 			count +=1
# 		# print(classif.pred())
# 	data_bfs.append((csv_arqui,count))
# 	df = pd.DataFrame(data_bfs)
# 	df.to_csv('/home/cristiano/Documentos/Programming/webdata/crawler/result_bfs.csv', index=False, header=False)

# for csv_arqui in heuristic_crawler_csv:
# 	df = pd.read_csv(path_heuristic+csv_arqui+'.csv')
# 	count = 0
# 	for elem in df.column.tolist():
# 		classif = Classify()
# 		label = classif.setWebpage(elem)
# 		if classif.pred() == 1:
# 			count +=1
# 	data_heuristic.append((csv_arqui,count))
# 	df = pd.DataFrame(data_heuristic)
# 	df.to_csv('/home/cristiano/Documentos/Programming/webdata/crawler/result_heuristic.csv', index=False, header=False)


# data_bfs_naive = []
# data_heuristic_naive = []
# for csv_arqui in bfs_crawler_csv:
# 	df = pd.read_csv(path_bfs+csv_arqui+'.csv')
# 	count = 0
# 	print csv_arqui
# 	for elem in df.column.tolist():
# 		if prob_func(elem) <= 0.4:
# 			count +=1
# 		# print(classif.pred())
# 	data_bfs_naive.append((csv_arqui,count))
# 	df = pd.DataFrame(data_bfs_naive)
# 	df.to_csv('/home/cristiano/Documentos/Programming/webdata/crawler/result_naive_3_bfs.csv', index=False, header=False)

# for csv_arqui in heuristic_crawler_csv:
# 	df = pd.read_csv(path_heuristic+csv_arqui+'.csv')
# 	count = 0
# 	print csv_arqui
# 	for elem in df.column.tolist():
# 		if prob_func(elem) <= 0.4:
# 			count +=1
# 	data_heuristic_naive.append((csv_arqui,count))
# 	df = pd.DataFrame(data_heuristic_naive)
# 	df.to_csv('/home/cristiano/Documentos/Programming/webdata/crawler/result_naive_3_heuristic.csv', index=False, header=False)
