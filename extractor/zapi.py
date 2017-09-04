# -*- coding: utf-8 -*-

import requests
from lxml import html
import os



agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

class Crawler:

	def __init__(self, start_url, depth):
		self.start_url = start_url
		self.depth = depth

	def crawl(self):
		self.get_data(self.start_url)
		return

	def get_data(self, link):
		start_page = requests.get(link, headers = agent)
		tree = html.fromstring(start_page.text)

		#empreedimento = tree.xpath('//span[@class="nome-empreendimento"]/text()')
		#print empreedimento
		endereco = tree.xpath('//span[@class="logradouro"]/text()')
		print "endereco: " + endereco[0]
		preco = tree.xpath('//span[@class="value-ficha"]/text()')[1]
		#preco = tree.xpath('//span[@class="dados-ficha no-show"]/text()')[0]
		print "preco: " + preco
		descricao = tree.xpath('//div[@id="descricaoOferta"]/p/text()')
		print "descricao: " + str(descricao)
		info = tree.xpath('//ul[@class="unstyled"]/li/text()')
		#print info
		quartos = info[0]
		print "quartos: " + quartos
		suite = info[1]
		print "suites: " + suite
		area_util = info[2]
		area_total = info[3]
		vagas = info[4]
		print "vagas: " + vagas
		valor_do_m2 = info[5]
		condominio = info[6]
		print "condominio: " + condominio
		iptu = info[7]
		print "iptu: " + iptu


		#print start_page.text
		return



url = 'https://www.zapimoveis.com.br/superdestaque/venda+apartamento+2-quartos+centro+torres+rs+71m2+RS425000/ID-11323353/'
ri = Crawler(url, 0)
ri.crawl()