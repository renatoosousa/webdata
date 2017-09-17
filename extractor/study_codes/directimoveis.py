# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup
import re



agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

class Directimoveis_crawler:

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

        tipo = soup.find('span', {'class': 'small'})
        self.data["Tipo"] = tipo.text.strip()

        address = soup.find("address")
        address = address.text.split('-')
        bairro = address[1]
        estado = address[2][-2] + address[2][-1]
        cidade = address[2].split(' ')
        cidade = cidade[1]

        self.data["Bairro"] = bairro.strip()
        self.data["Cidade"] = cidade.strip()
        self.data["Estado"] = estado.strip()

        valor = soup.find("li", {"class": "boxValue"})
        self.data[valor(text=True)[0]] = valor(text=True)[1].strip()

        infos = soup.find_all("li", {"class": "boxTextList"})
        info = infos[1].find("p")
        info = info.text.split('-')

        self.data["Area Total"] = info[1].strip()
        for i in range(2, len(info)):
            val = info[i].split(':')
            self.data[val[0].strip()] = val[1].strip()

        for key in self.data:
            print key + ": " + self.data[key]



url = 'http://www.directimoveis.com.br/imovel-V0373/morada-da-peninsula'
ri = Directimoveis_crawler(url)
ri.crawl()