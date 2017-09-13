# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup
import time



agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

class Olx_crawler:

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

        preco = soup.find("span", {"class": "actual-price"})
        self.data["Valor de Venda"] = preco.get_text()


        estado = self.start_url[7] + self.start_url[8]
        self.data["Estado:"] = estado.upper()
        address = soup.find_all("ul", {"class": "list square-gray"})
        for info in address:
            ps = info.find_all("p")
            for p in ps:
                self.data[p(text=True)[1]] = p(text=True)[3].strip()

        
        self.title = self.data["Tipo:"]
        for key in self.data:
			print key + " " + self.data[key]

url = 'http://pa.olx.com.br/regiao-de-belem/imoveis/eco-parque-mobiliado-389595562'
olx = Olx_crawler(url)
olx.crawl()