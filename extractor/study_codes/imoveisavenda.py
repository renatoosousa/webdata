# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup



agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
          'Accept-Language': 'pt-BR'}

class Imoveisavenda_crawler:

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

        infos = soup.find("div", {"id": "basicInfo"})
        for div in infos.find_all("div"):
            print div.text

url = 'http://imovelavenda.com.br/Boa_Viagem_Casa_2_Dorm_Protasio_Alves_Porto_Alegre_14069_RS__WMV55'
ri = Imoveisavenda_crawler(url)
ri.crawl()