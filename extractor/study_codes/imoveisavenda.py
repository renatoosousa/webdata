# -*- coding: utf-8 -*-

from __future__ import print_function
import requests
import os
import bs4
from bs4 import BeautifulSoup




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

        valor = soup.find("div", {"class": "price"})
        self.data["Modalidade"] = valor(text=True)[0].strip()
        self.data["Preco por m2"] = valor(text=True)[-1].strip()
         
        preco = ""
        for i in range(1, len(valor(text=True)) - 1):
            preco = valor(text=True)[i].strip() + " " + preco 
        self.data["Valor"] = preco.strip()

        infos = soup.find("div", {"id": "basicInfo"})
        for b in infos.find_all("b"):
            campo = b.text.replace(':', '')
            valor = b.next_element.next_element.text
            if campo == "Cidade":
                valor = valor.split('-')
                self.data["Estado"] = valor[1].strip()
                valor = valor[0]
            self.data[campo] = valor

        for key in self.data:
            print (key, end='')
            print (": ", end='')
            print (self.data[key])


url = 'http://imovelavenda.com.br/Fiateci_Apto_2_Dorm_Sao_Geraldo_Porto_Alegre_10066_RS__YWQ10'
ri = Imoveisavenda_crawler(url)
ri.crawl()