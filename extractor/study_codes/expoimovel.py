# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup
from results import ExtractorDB



agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
          'Accept-Language': 'pt-BR'}

class Expoimovel_crawler:

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

    def get_data(self, link):
        start_page = requests.get(link, headers = agent)
        soup = BeautifulSoup(start_page.content, "html.parser")
        self.extract_data(soup)

    def extract_data(self, soup):
        for js in soup(["script", "style"]):
            js.extract()

        try:
            infos = soup.find_all("div", {"id": "boxCaracJan"})
            infos = infos[0].find_all("div", {"class": "detTitBox"})
            for i in range(0, len(infos), 2):
                self.data[infos[i].text.strip()] = infos[i+1].text.strip().replace('\n', '').replace('\t', '')
        except:
            pass

        try:
            tipo = soup.find_all("font", {"class": "color-detalhe-orange"})
            self.data["Tipo"] = tipo[1].text.strip()
        except:
            pass

        try:
            preco = soup.find("div", {"id": "boxPrecoImo"})
            self.data["Valor"] = preco.text.strip()
        except:
            pass

        try:
            condominio = soup.find("div", {"id": "noxSubValCond"})
            self.data["Condominio"] = condominio.text.strip()
        except:
            pass
            
        local = soup.find("div", {"class": "prentesaoTopDet"})
        try:
            local = local.text.split('-')
            cidade = local[-1].split('/')[0].strip()
            estado = local[-1].split('/')[1].strip()
            self.data["Estado"] = estado
            self.data["Cidade"] = cidade
            bairro = local[0].split(',')[-1].strip()
            self.data["Bairro"] = bairro
        except:
            pass
            #sem endereco

        for key in self.data:
            print key + ": " + self.data[key]


db = ExtractorDB()
for item in db.get_domain("expoimovel"):
	print item
	expo = Expoimovel_crawler(item)
	expo.crawl()
	print "\n\n"