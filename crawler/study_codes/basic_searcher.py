from bs4 import BeautifulSoup
import requests
import sys

def buscar_links(url):
	if 'http' not in url:
		url = 'http://'+url

	lista = []
	i = 0
	r = requests.get(url)
	soup = BeautifulSoup(r.text)
	for a in soup.findAll('a',href = True):
		link = a['href']
		i += 1
		if('http' in link) or ('https' in link):
			print link
		lista.append(link)
		links = str(link).strip('[]').replace("u","").replace("'","")
		# print str(i)+") "+str(link)
	# print "\n>> Total = %d \n" % i
	# print lista
	sys.exit()

url = raw_input("url: ")
buscar_links(url)