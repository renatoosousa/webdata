# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup



agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

class Vivareal_crawler:

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
        if soup.find("div", {"class": "lT"}):
            self.extract_data2(soup)
        else:
            self.extract_data(soup)

    def extract_data(self, soup):
        address = soup.find("p",  {"class": "bZ"} ).get_text()
        address = address.split(',')
        bairro = address[1].split('-')
        bairro = bairro[1].strip()
        cidade = address[2].split('-')
        estado = cidade[1].strip()
        cidade = cidade[0].strip()

        self.data["Estado"] = estado
        self.data["Cidade"] = cidade
        self.data["Bairro"] = bairro

        infos = soup.find_all("ul", {"class": "bw"})
        for info in infos:
            lis = info.find_all("li")
            spans = info.find_all("span")
            
        '''for key in self.data:
            print key + ": " + self.data[key]'''

    def extract_data2(self, soup):
        print "todo"


url = 'https://www.vivareal.com.br/imovel/apartamento-2-quartos-cidade-baixa-bairros-porto-alegre-78m2-venda-RS300000-id-84817060/'
url2 = 'https://www.vivareal.com.br/imoveis-lancamento/reserva-ecoville-8636/?__vt=map:b'
ri = Vivareal_crawler(url)
ri.crawl()