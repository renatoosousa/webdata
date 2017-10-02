# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup




agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
          'Accept-Language': 'pt-BR'}

class Imovelweb_crawler:

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

        infos = soup.find("div", {"class": "card aviso-datos"})
        lis = infos.find_all("li")

        self.data["Tipo"] = lis[0].text.strip()
        valores = lis[1].find_all("span")
        modalidade = valores[0].text.split(' ')
        self.data["Modalidade"] = modalidade[1].strip()

        for i in range(1, len(lis)-1):
            span = lis[i].find_all("span")
            if len(span) == 1:
                span = span[0].text.split(' ')
                self.data[span[1].strip()] = span[0].strip()
            else:
                self.data[span[0].text.strip()] = span[1].text.strip()
            
        try:
            local = soup.find("a", {"href": "#map"})
            local = local.text.split(',')
            self.data["Bairro"] = local[-2].strip()
            self.data["Cidade"] = local[-1].strip()
        except:
            pass

        for key in self.data:
            print key + ": " + self.data[key]


url = 'http://www.imovelweb.com.br/propriedades/apartamento-residencial-para-locacao-boa-viagem-2932218008.html'
url2 = 'http://www.imovelweb.com.br/propriedades/apartamento-a-venda-em-moema-2933751732.html'
ri = Imovelweb_crawler(url2)
ri.crawl()