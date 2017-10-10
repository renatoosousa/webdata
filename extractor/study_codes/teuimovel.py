# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup
from results import ExtractorDB




agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
          'Accept-Language': 'pt-BR'}

class Teuimovel_crawler:

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
            infos = soup.find_all("div", {"class": "col-lg-6"})
            infos = infos[1]

            valor = infos.find("div", {"class": "titulo faixa"})
            valor = valor.text.split('-')
            self.data["Tipo"] = valor[0].strip()
            self.data["Valor"] = valor[1].strip()

            local = infos.find("strong")
            local = local.previous.previous.previous.strip()
            local = local.split(' ')
            estado = local[-1].strip()
            self.data["Estado"] = estado


            for info in infos.find_all("strong"):
                self.data[info.text.strip()] = info.previous.strip()
        except:
            pass
        

        for key in self.data:
            print key.encode("utf-8") + ": " + self.data[key].encode("utf-8")


db = ExtractorDB()
for item in db.get_domain("teuimovel"):
	print item
	teuimovel = Teuimovel_crawler(item)
	teuimovel.crawl()
	print "\n\n"