# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup



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

        valor = soup.find("div", {"class": "valorImovel"})
        self.data["Tipo"] = valor(text=True)[0].strip()
        self.data["Valor"] = valor(text=True)[1].strip()

        infos = soup.find("div", {"class": "importante"})
        print infos(text=True)


      

        for key in self.data:
            print key + ": " + self.data[key]



url = 'http://www.redeimoveispe.com.br/imovel-detalhes.aspx?refRede=AP1253-DZQ'
url2 = 'http://www.redeimoveispe.com.br/imovel-detalhes.aspx?refRede=AP1712-D3O'
ri = Redeimoveispe_crawler(url2)
ri.crawl()