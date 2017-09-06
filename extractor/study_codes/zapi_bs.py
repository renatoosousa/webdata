# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup
import re



agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

class Zapi_crawler:

	def __init__(self, start_url):
		self.start_url = start_url

	def crawl(self):
		self.get_data(self.start_url)
		return

	def get_data(self, link):
		start_page = requests.get(link, headers = agent)
		soup = BeautifulSoup(start_page.content, "html.parser")

		annoucer = soup.find("input", {"id": "hdnNomeAnunciante"})
		annoucer = annoucer["value"]
		print annoucer

		if annoucer == "Moura Dubeux" :
			self.extract_data_mb(soup)
		else:
			self.extract_data_normal(soup)
		

	def extract_data_normal(self, soup):
		price = soup.find("span",  {"class": "value-ficha"})
		print price.text

		city = soup.find("span", {"class": "logradouro"})
		print city.text

		#address = soup.find("h1", {"class": "pull-left"})
		#for item in address:
			#print address
			#print "..."

		uls = soup.find_all("ul", {"class": "unstyled"})
		for ul in uls:
			for li in ul.find_all('li'):
				if li.find("span", {"class": "text-info"}):
					print li.text

		return

	def extract_data_mb(self, soup):
		print "todo"



url = 'https://www.zapimoveis.com.br/oferta/venda+apartamento+3-quartos+boa-viagem+recife+pe+160m2+RS980000/ID-14533109/?oti=1'
ri = Zapi_crawler(url)
ri.crawl()