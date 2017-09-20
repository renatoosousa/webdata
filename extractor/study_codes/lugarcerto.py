# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup
import re



agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

class Lugarcerto_crawler:

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

        ul_infos = soup.find("ul", {"class": "dados-item"})
        for li in ul_infos:
            self.data[ li(text=True)[0].strip() ] = li(text=True)[1].strip()

        valor = soup.find("span", {"class": "mobile_price"})
        self.data["VALOR"] = valor.text.strip()

        custos = soup.find("ul", {"class": "itenscustos__mobile"})
        for li in custos:
            self.data[ li(text=True)[0].replace(':', '').strip() ] = li(text=True)[1].strip()

        localizacao = soup.find("span", {"class": "resultados-da-busca-localizacao"})
        localizacao = localizacao.text.split('-')
        self.data["ESTADO"] = localizacao[1].strip()
        localizacao = localizacao[0].split(',')
        self.data["CIDADE"] = localizacao[-1].strip()
        self.data["BAIRRO"] = localizacao[-2].strip()

        for key in self.data:
            print key + ": " + self.data[key]



url = 'http://diariodepernambuco.lugarcerto.com.br/imovel/casa-em-condominio-2-quartos-aldeia-camaragibe-54m2-venda-rs230000-id-329299726'
url2 = 'http://estadodeminas.lugarcerto.com.br/imovel/apartamento-2-quartos-centro-belo-horizonte-com-garagem-110m2-aluguel-rs1400-id-219049719'
ri = Lugarcerto_crawler(url2)
ri.crawl()
