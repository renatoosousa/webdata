from bs4 import BeautifulSoup
import requests
import sys
import time
import validators

sys.path.insert(0,'../general')

from getRobot import getRobot

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

lista_check = []

def check_url(url):
	try:
		req = requests.head(url)
		if req.status_code < 400:
			return True
		else:
			return False
	except Exception:
		return False

def isValid_url(url):
	if(not validators.url(url)):
		return False
	else:
		return True

def buscar_links(url,link_list):
	if 'http' not in url:
		url = 'http://'+url

	lista = link_list
	i = 0
	r = requests.get(url, headers=headers)
	soup = BeautifulSoup(r.text)
	for a in soup.findAll('a',href = True):
		link = a['href']
		i += 1
		if(('http' in link) or ('https' in link)) and (' ' not in link)and (len(lista)<200):
			if isValid_url(link):
				lista.append(link)
	print len(lista)
	if(len(lista)==200):
		print lista
		sys.exit()

	# Filtering based on the robots.txt
	for check_elem in lista_check:
		lista = [elem for elem in lista if elem != check_elem]

	next_url = lista.pop(0)
	time.sleep(1)
	buscar_links(next_url,lista)

url = raw_input("url: ")
lista_check = getRobot(url)
buscar_links(url,[])
# print check_url(url)

# (('http' in link) or ('https' in link)) and 