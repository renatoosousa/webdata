# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup



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

    def remove_whitespaces(self, string):
        string = string.replace('\r', '')
        string = string.replace('\n', '')

        return string

    def get_data(self, link):
        start_page = requests.get(link, headers = agent)
        soup = BeautifulSoup(start_page.content, "html.parser")

        preco = soup.find("span", {"class": "actual-price"})
        self.data["Valor de Venda"] = preco.get_text()

        tipo = soup.find("strong", {"class": "description"})
        self.title = tipo.get_text()
        print self.title

        count = 0
        address = soup.find("div", {"class": "OLXad-location mb20px"})
        for item in address(text=True):
            print item + str(count)
            count = count + 1
            
        print address(text=True)[7]
        cidade = self.remove_whitespaces(address(text=True)[9])
        self.data[address(text=True)[7]] = cidade

        bairro = self.remove_whitespaces(address(text=True)[25])
        self.data["Bairro"] = bairro

        estado = self.start_url[7] + self.start_url[8]
        self.data["Estado"] = estado.upper()


        info = soup.find("div",  {"class": "OLXad-details mb30px"})

        for key in self.data:
			print key + ": " + self.data[key]

url = 'http://sp.olx.com.br/regiao-de-sao-jose-do-rio-preto/imoveis/ate-0-de-entrada-parcelamos-doc-e-entrada-389296288'
olx = Olx_crawler(url)
olx.crawl()