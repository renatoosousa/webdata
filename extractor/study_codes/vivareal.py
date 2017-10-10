# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup
from results import ExtractorDB



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
        try:
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
        except:
            pass


        try:
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
        except:
            pass

        for key in self.data:
            print key + ": " + self.data[key]

    def extract_data2(self, soup):
        try: 
            infos = soup.find("div", {"class": "pZ"})
            for item in infos:
                self.data[item(text=True)[0].strip()] = item(text=True)[1].strip()
            infos = soup.find("div", {"class": "pZ pY"})
            infos = infos.find_all("dl")
            for item in infos:
                self.data[item(text=True)[0].strip()] = item(text=True)[1].strip()
        except:
            pass

        
        try:
            address = soup.find("span", {"class": "touch-nav__address"})
            self.data["ENDERECO"] = address.text.strip()
        except:
            pass

        for key in self.data:
                print key + ": " + self.data[key]



db = ExtractorDB()
for item in db.get_domain("vivareal"):
	print item
	vivareal = Vivareal_crawler(item)
	vivareal.crawl()
	print "\n\n"