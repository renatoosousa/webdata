# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup
from results import ExtractorDB
import re




agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
          'Accept-Language': 'pt-BR'}

class Redeimoveispe_crawler:

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

        html2 = soup.find("section", {"id": "fichaEmpreendimento01"})
        if html2:
            self.get_data2(soup)
            return

        try:
            valor = soup.find("div", {"class": "valorImovel"})
            self.data["Tipo"] = valor(text=True)[0].strip()
            self.data["Valor"] = valor(text=True)[1].strip()
        except:
            pass


        try:            
            valores = soup.find("div", {"class": "valoresInfo"})
            valores = valores.find_all("div")
            for i in range(1, len(valores) -2 ):
                self.data[ valores[i](text=True)[-2].replace(':', '').strip() ] = valores[i](text=True)[-1].strip()
        except:
            pass

        
        try:
            infos = soup.find_all("div", {"class": "importante"})
            for i in range(1, len(infos)):
                self.data[ infos[i](text=True)[-1].strip() ] = infos[i](text=True)[-2].strip()
            self.data[ infos[0](text=True)[-2].replace(':', '').strip() ] = infos[0](text=True)[-1].strip()
        except:
            pass


        for key in self.data:
            print key + ": " + self.data[key]

    def get_data2(self, soup):

        try:
            infos = soup.find_all("div", {"class": "importantes"})
            if re.search(r"\d+", infos[0].text).group():
                self.data[infos[0](text=True)[1].strip()] = infos[0](text=True)[2].strip()
            
            infos = infos[1].find_all("span")
            self.data["Area"] = infos[0].text.strip()
            for i in range(1, len(infos)):
                x = infos[i].text.split(' ')
                self.data[x[-1].strip()] = x[-2].strip()
        except:
            pass

        try:
            address = soup.find("div", {"id": "mapaCond"})
            self.data["Endereco"] = address.text.strip()
        except:
            pass

        for key in self.data:
            print key + ": " + self.data[key]


# ri = Redeimoveispe_crawler('http://www.redeimoveispe.com.br/empreendimento-detalhes.aspx?id_empreendimento=7759469')
# ri.crawl()

db = ExtractorDB()
for item in db.get_domain("redeimoveispe"):
	print item
	redeimoveispe = Redeimoveispe_crawler(item)
	redeimoveispe.crawl()
	print "\n\n"