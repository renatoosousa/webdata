# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup
from results import ExtractorDB




agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
          'Accept-Language': 'pt-BR'}

class Imovelweb_crawler:

    def __init__(self, start_url):
        self.start_url = start_url
        self.data = {}
        self.title = ""


    def crawl(self):
        self.get_data(self.start_url)
        print len(self.data)
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
        except:
            pass
            
        try:
            local = soup.find("a", {"href": "#map"})
            local = local.text.split(',')
            self.data["Bairro"] = local[-2].strip()
            self.data["Cidade"] = local[-1].strip()
        except:
            pass

        for key in self.data:
            print key.encode("utf-8") + ": " + self.data[key].encode("utf-8")


db = ExtractorDB()
for item in db.get_domain("imovelweb"):
	print item
	imovelweb = Imovelweb_crawler(item)
	imovelweb.crawl()
	print "\n\n"