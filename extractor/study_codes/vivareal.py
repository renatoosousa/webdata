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

        #por que diabos nao itera ate -1
        infos = soup.find_all("ul", {"class": "bw"})
        lis = infos[0].find_all("li")
        line_val = ""
        for i in range(1, len(lis)):
            line = lis[i](text=True)
            for j in range(1, len(line)):
                line_val = line_val + line[j]
            self.data[line[0]] = line_val
            line_val = ""

        lis = infos[1].find_all("li")
        for li in lis:
            self.data[ li(text=True)[1] ] = li(text=True)[0]

        for key in self.data:
            print key + ": " + self.data[key]

    def extract_data2(self, soup):
        infos = soup.find_all("div", {"class": "oX"})
        info = infos[3].find_all("dl")
        for item in info:
            line = item(text=True)
            line_val = ""
            for i in range(1, len(line)):
                line_val = line_val + line[i]
            self.data[line[0]] = line_val.strip()
            line_val = ""


        address = soup.find("cite", {"class": "pk"})
        address = address.text.split(',')
        self.data["BAIRRO"] = address[0].strip()
        self.data["CIDADE"] = address[1].strip()
        self.data["ESTADO"] = address[2].strip()

        for key in self.data:
                print key + ": " + self.data[key]


url = 'https://www.vivareal.com.br/imovel/apartamento-3-quartos-butanta-zona-oeste-sao-paulo-com-garagem-70m2-venda-RS369000-id-84167740/?__vt=map:b'
url2 = 'https://www.vivareal.com.br/imoveis-lancamento/voxy-ipiranga-8793/?__vt=map:b'
ri = Vivareal_crawler(url2)
ri.crawl()