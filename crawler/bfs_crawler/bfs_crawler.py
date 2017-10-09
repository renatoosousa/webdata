from bs4 import BeautifulSoup
import requests
import sys
import time
import validators
import pandas as pd
sys.path.insert(0,'../general')
from getRobot import getRobot

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

class bfs_crawler(object):
	"""docstring for bfs_crawler"""

	def __init__(self, url):
		# super(bfs_crawler, self).__init__()
		self.url = url
		self.links_list_check = getRobot(url)
		self.links_list = []
		# self.init_search(url)

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
				 
					# print "yes" and (self.url in link)
				if(('http' in link) or ('https' in link)) and (' ' not in link)and (len(self.links_list)<1000) and (self.url in link):
					if self.isValid_url(link):
						self.links_list.append(link)
			print len(self.links_list)
			if(len(self.links_list)>=1000):
				# print self.links_list
				print "Finished"
				return

			# Filtering based on the robots.txt
			for check_elem in self.links_list_check:
				self.links_list = [elem for elem in self.links_list if elem != check_elem]

			next_url = self.links_list.pop(0)
			time.sleep(1)
			self.search_links(next_url)
		except Exception:
			print "Error"
			if(len(self.links_list)==0):
				return
			next_url = self.links_list.pop(0)
			time.sleep(1)
			self.search_links(next_url)

	def init_search(self):
		self.search_links(self.url)

	def getLinks(self):
		return self.links_list

	def saveLinksCSV(self, name):
		df = pd.DataFrame(self.links_list, columns=["column"])
		df.to_csv(name +'.csv',header=True, index=False, encoding='utf-8')

test = bfs_crawler("http://www.redeimobiliariasecovi.com.br")
test.init_search()
test.saveLinksCSV("bfs_redeimobilidaria")

