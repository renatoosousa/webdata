import requests
import BeautifulSoup

def bfs_list_links(url_init,depth):
	if 'http' not in url_init:
		url_init = 'http://'+url_init
	
	links_tree = [[url_init]]
	# links = []

	# r = requests.get(url)
	# if not (r.status_code == requests.codes.ok):
	# 	return None
	# soup = BeautifulSoup.BeautifulSoup(r.content)
	
	i = 0
	while i <= depth:
		for url in links_tree[i]:
			links = []
			print url
			print "Tree level %d" % i
			r = requests.get(url)
			if (r.status_code == requests.codes.ok):
				soup = BeautifulSoup.BeautifulSoup(r.content)
				for a in soup.findAll('a'):
					if a.get('href') and 'imoveis' in a.get('href'):
						links.append(a.get('href'))
				links_tree.append(links) 	
		i+=1

	# for a in soup.findAll('a'):
	# 	if 'imoveis' in a.get('href'):
	# 		links.append((a.text, a.get('href')))
	

	# return links

	# soup = BeautifulSoup.BeautifulSoup(r.content)

bfs_list_links("http://pe.olx.com.br/",2)


