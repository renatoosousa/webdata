import requests
import BeautifulSoup
 
def get_links_from():
	links = []
	r = requests.get('http://pe.olx.com.br/')
	if r.status_code != 200:
		return None
	soup = BeautifulSoup.BeautifulSoup(r.content)
	# print r.content
	for a in soup.findAll('a'):
		if 'imoveis' in a.get('href'):
			links.append((a.text, a.get('href')))
	return links


for link_name, link_url in get_links_from():
    print "%s - %s" % (link_name, link_url)