from bs4 import BeautifulSoup
import requests
import sys

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

def check_url(url):
	try:
		req = requests.head(url)
		if req.status_code < 400:
			return True
		else:
			return False
	except Exception:
		return False


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
		if(('http' in link) or ('https' in link)) and (len(lista)<200):
			if check_url(link):
				lista.append(link)
	print len(lista)
	if(len(lista)==200):
		print lista
		sys.exit()
	next_url = lista.pop(0)
	buscar_links(next_url,lista)

url = raw_input("url: ")
buscar_links(url,[])
# print check_url(url)

# (('http' in link) or ('https' in link)) and 