# -*- coding: utf-8 -*-

from __future__ import print_function
import requests
import os
import bs4
from bs4 import BeautifulSoup
from results import ExtractorDB




agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
          'Accept-Language': 'pt-BR'}

class Imoveisavenda_crawler:

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

        try:
            valor = soup.find("div", {"class": "price"})
            self.data["Modalidade"] = valor(text=True)[0].strip()
            self.data["Preco por m2"] = valor(text=True)[-1].strip()
        except:
            pass

        try:
            preco = ""
            for i in range(1, len(valor(text=True)) - 1):
                preco = valor(text=True)[i].strip() + " " + preco 
            self.data["Valor"] = preco.strip()
        except:
            pass

        try:
            infos = soup.find("div", {"id": "basicInfo"})
            for b in infos.find_all("b"):
                campo = b.text.replace(':', '')
                valor = b.next_element.next_element.text
                if campo == "Cidade":
                    valor = valor.split('-')
                    self.data["Estado"] = valor[1].strip()
                    valor = valor[0]
                self.data[campo] = valor
        except:
            pass

            
        for key in self.data:
            try:
                print (key, end='').encode("utf-8")
                print (": ", end='')
                print (self.data[key]).encode("utf-8")
            except:
                pass

db = ExtractorDB()
for item in db.get_domain("imovelavenda"):
    print (item)
    imoveisavenda = Imoveisavenda_crawler(item)
    imoveisavenda.crawl()
    print ("\n\n")