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
		self.data = {}
		self.title = ""

	def crawl(self):
		self.get_data(self.start_url)
		return

	def get_data(self, link):
		start_page = requests.get(link, headers = agent)
		soup = BeautifulSoup(start_page.content, "html.parser")

		annoucer = soup.find("input", {"id": "hdnNomeAnunciante"})
		annoucer = annoucer["value"]
		print annoucer
		self.title = annoucer

		if annoucer == "Moura Dubeux":
			self.extract_data_mb(soup)
		elif annoucer == "MRV Engenharia S/A":
			self.extract_data_mb(soup)
		else:
			self.extract_data_normal(soup)

	def extract_data_normal(self, soup):
		price = soup.find("span",  {"class": "value-ficha"})
		self.data[ price(text=True)[1] ] = price(text=True)[2]

		prop = soup.find("h1", {"class": "pull-left"})
		prop = prop.findChildren()[0](text=True)

		self.title = self.title + " - " + str(prop)
		print self.title


		address = soup.find("span", {"class": "logradouro"})
		address = address.text.split(',')
		self.data["Bairro"] = address[0]
		address = address[1].split('-')
		self.data["Cidade"] = address[0]
		self.data["Estado"] = address[1]


		uls = soup.find_all("ul", {"class": "unstyled"})
		for ul in uls:
			for li in ul.find_all('li'):
				spans = li.find_all("span", {"class": "text-info"})
				if li.find("span", {"class": "text-info"}):
					self.data[ li(text=True)[1] ] = li(text=True)[0]

		for key in self.data:
			print key + ": " + self.data[key]

	def extract_data_mb(self, soup):
		print "todo"



url = 'https://www.zapimoveis.com.br/lancamento/apartamento+venda+boa-viagem+recife+pe+jardim-das-orquideas+moura-dubeux+95m2-124m2/ID-13235/?contato=0&oti=4'
ri = Zapi_crawler(url)
ri.crawl()