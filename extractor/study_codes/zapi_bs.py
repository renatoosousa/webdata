# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup
from results import ExtractorDB



agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

class Zapi_crawler:

	def __init__(self, start_url):
		self.start_url = start_url
		self.data = {}
		self.title = ""


	def crawl(self):
		self.get_data(self.start_url)
		return

	def get_rawHtml(self):
		start_page = requests.get(self.start_url, headers = agent)
		soup = BeautifulSoup(start_page.content, "html.parser")

		for js in soup(["script", "style"]):
			js.extract()

		return soup.get_text().encode("utf-8")
		#return str(soup(text=True))

	def get_data(self, link):
		start_page = requests.get(link, headers = agent)
		soup = BeautifulSoup(start_page.content, "html.parser")

		annoucer = soup.find("input", {"id": "hdnNomeAnunciante"})
		try:
			annoucer = annoucer["value"]
			#print annoucer
			self.title = annoucer
		except:
			print "inexistent site?"

		
		if annoucer == "Moura Dubeux":
			self.extract_data_mb(soup)
		elif annoucer == "MRV Engenharia S/A":
			self.extract_data_mb(soup)
		elif annoucer == "Bolognesi":
			self.extract_data_mb(soup)
		else:
			self.extract_data_normal(soup)

	def extract_data_normal(self, soup):
		try:
			price = soup.find("span",  {"class": "value-ficha"})
			self.data[ price(text=True)[1] ] = (price(text=True)[2].strip())

			prop = soup.find("h1", {"class": "pull-left"})
			prop = prop.find("span")
			self.title = self.title + " - " + prop.text
			print self.title
		except:
			pass

		try:
			address = soup.find("span", {"class": "logradouro"})
			address = address.text.split(',')
			self.data["Bairro"] = address[0].strip()
			address = address[1].split('-')
			self.data["Cidade"] = address[0].strip()
			self.data["Estado"] = address[1].strip()
		except:
			pass


		uls = soup.find_all("ul", {"class": "unstyled"})
		for ul in uls:
			for li in ul.find_all('li'):
				spans = li.find_all("span", {"class": "text-info"})
				if li.find("span", {"class": "text-info"}):
					self.data[ li(text=True)[1].strip() ] = li(text=True)[0].strip()

		for key in self.data:
			print key + ": " + self.data[key]

	def extract_data_mb(self, soup):
		prop_addr = soup.find_all("span", {"class": "info-imovel"})
		prop = prop_addr[0].text
		self.title = self.title + " - " + prop
		print self.title

		valor = soup.find("span", {"class": "dados-ficha no-show"})
		self.data["Valor de Venda"] = valor.text
		address = prop_addr[1].text
		address = address.split(',')
		self.data["Bairro"] = address[0]
		address = address[1].split('-')
		self.data["Cidade"] = address[0]
		self.data["Estado"] = address[1]

		ul = soup.find("ul", {"class": "unstyled container"})
		h3 = ul.find_all("h3")
		for item in h3:
			val = ""
			for i in range(0, len(item(text=True)) -1 ):
				val = val + str(item(text=True)[i])
			self.data[ item(text=True)[-1]] = val

		for key in self.data:
			print key + ": " + self.data[key]



db = ExtractorDB()
for item in db.get_domain("zapi"):
	print item
	zapi = Zapi_crawler(item)
	zapi.crawl()
	print "\n\n"