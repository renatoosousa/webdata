from bs4 import BeautifulSoup
import requests
import sys
import time
import validators
import pandas as pd
sys.path.insert(0,'../general')
from getRobot import getRobot
from textblob.classifiers import NaiveBayesClassifier
import nltk
nltk.download('punkt')
import pickle

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

def getKey(item):
	return item[0]

class heuristic_crawler(object):
	"""docstring for bfs_crawler"""

	def __init__(self, url):
		# super(bfs_crawler, self).__init__()
		self.url = url
		self.links_list_check = getRobot(url)
		self.border = []
		self.links_list = []
		self.general_links=[]
		self.it_time_sleep = 100
		with open('classifier_fitted.pkl', 'rb') as f:
			self.clf_test = pickle.load(f)
		# self.init_search(url)
	
	def heuristic_func(self, link):
		prob_dist = self.clf_test.prob_classify(link)
		return round(prob_dist.prob(0),2)

	def check_url(self,url):
		try:
			req = requests.head(url)
			if req.status_code < 400:
				return True
			else:
				return False
		except Exception:
			return False

	def isValid_url(self,url):
		if(not validators.url(url)):
			return False
		else:
			return True

	def search_links(self,url):
		try:
			if 'http' not in url:
				url = 'http://'+url
			r = requests.get(url, headers=headers)
			soup = BeautifulSoup(r.text)
			for a in soup.findAll('a',href = True):
				link = a['href']

				if(len(link)!=0):
					if(link[0]=='/'):
						link = self.url + link
				# and (self.url in link)

				if(('http' in link) or ('https' in link)) and (' ' not in link)and (len(self.links_list)<1000) and (self.url in link) and (link not in self.general_links):
					if self.isValid_url(link):
						prob = self.heuristic_func(link)
						if prob < 0.9:
							self.general_links.append(link)
							self.border.append((prob,link))
							self.border = sorted(self.border, key=getKey)
			print len(self.links_list)
			# print self.border[0][1]
			# print self.border

			# while self.border[0][0]<0.3:
			# 	# self.links_list.append(self.border[0][1])
			# 	# if self.border[0][1] not in self.links_list:
			# 	self.links_list.append(self.border[0][1])	
			# 	print "insert"
			# 	self.border.pop(0)
			
			# Verificando robot.txt 
			for check_elem in self.links_list_check:
				self.links_list = [elem for elem in self.links_list if elem != check_elem]

			# if self.border[0][0]<=0.4:
			if self.border[0][1] not in self.links_list:
				self.links_list.append(self.border[0][1])	
				print "Insert"

			if(len(self.links_list)>=1000):
				# print self.border
				print "Finished"
				return
			# Filtering based on the robots.txt
			# for check_elem in self.links_list_check:
				# self.links_list = [elem for elem in self.links_list if elem != check_elem]

			next_url = self.border.pop(0)
			next_url = next_url[1]
			if(len(self.links_list)==self.it_time_sleep):
				# time.sleep(1)
				self.saveLinksCSV("heuristic_imovelweb")
				self.it_time_sleep+=100
			self.search_links(next_url)
		except Exception:
			print 
			print "Error"
			if(len(self.border)==0):
				return
			next_url = self.border.pop(0)
			next_url = next_url[1]
			if(len(self.links_list)==self.it_time_sleep):
				time.sleep(1)
				self.it_time_sleep+=100
			self.search_links(next_url)

	def init_search(self):
		self.search_links(self.url)

	def getLinks(self):
		return self.links_list

	def saveLinksCSV(self, name):
		df = pd.DataFrame(self.links_list, columns=["column"])
		df.to_csv(name +'.csv',header=True, index=False, encoding='utf-8')

test = heuristic_crawler("http://www.imovelweb.com.br")
test.init_search()
# test.saveLinksCSV("heuristic_expoimovel")
