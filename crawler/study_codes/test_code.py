from bs4 import BeautifulSoup
import requests
import sys

def buscar_links(url,link_list):
	if 'http' not in url:
		url = 'http://'+url

	lista = link_list
	i = 0
	r = requests.get(url)
	soup = BeautifulSoup(r.text)
	for a in soup.findAll('a',href = True):
		link = a['href']
		i += 1
		if(('http' in link) or ('https' in link)) and (len(lista)<1000):
			lista.append(link)
	print len(lista)
	if(len(lista)==1000):
		print lista
		sys.exit()
	next_url = lista.pop(0)
	buscar_links(next_url,lista)

url = raw_input("url: ")
buscar_links(url,[])