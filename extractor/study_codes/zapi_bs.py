# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup
import re



agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

class Crawler:

	def __init__(self, start_url):
		self.start_url = start_url

	def crawl(self):
		self.get_data(self.start_url)
		return

	def get_data(self, link):
		start_page = requests.get(link, headers = agent)
		soup = BeautifulSoup(start_page.content, "html.parser")

		price = soup.find_all("span",  {"class": "value-ficha"})
		for item in price:
			print item.text

		uls = soup.find_all("ul", {"class": "unstyled"})
		for ul in uls:
			for li in ul.find_all('li'):
				if li.find("span", {"class": "text-info"}):
					print li.text

		return



url = 'https://www.zapimoveis.com.br/oferta/venda+apartamento+1-quarto+centro+torres+rs+79m2+RS569000/ID-12495910/?oti=1'
ri = Crawler(url)
ri.crawl()