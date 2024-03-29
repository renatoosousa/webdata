# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup
import time
from results import ExtractorDB



agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

class Olx_crawler:

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
            preco = soup.find("span", {"class": "actual-price"})
            self.data["Valor de Venda"] = preco.get_text()
        except:
            pass

        try:
            estado = self.start_url[7] + self.start_url[8]
            self.data["Estado:"] = estado.upper()
            address = soup.find_all("ul", {"class": "list square-gray"})
            for info in address:
                ps = info.find_all("p")
                for p in ps:
                    self.data[p(text=True)[1]] = p(text=True)[3].strip()
        except:
            pass
        
        try:
            self.title = self.data["Tipo:"]
        except:
            pass
            
        for key in self.data:
			print key.encode("utf-8") + " " + self.data[key].encode("utf-8")

db = ExtractorDB()
for item in db.get_domain("olx"):
	print item
	olx = Olx_crawler(item)
	olx.crawl()
	print "\n\n"