# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup
import re




agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
          'Accept-Language': 'pt-BR'}

class Regex_scrapper:

    def __init__(self, start_url):
        self.start_url = start_url
        self.data = {}
        self.title = ""


    def crawl(self):
        html = self.get_rawHtml()

        try:
            quartos = re.search("\d+\squartos?", html)
            valor = re.search("R\$\s\d+[,.]\d+", html)
            vagas = re.search("\d+\svagas?",html)
            area = re.search("\d+\sarea", html)
            tipo = re.search("locacao|aluguel", html)

        except:
            pass

        try:
            print "valor: " + valor.group()
            print "quartos: " + quartos.group()
            print "vagas: " + vagas.group()
            print "area: " + area.group() 
            print "tipo: "+ tipo.group()
        except:
            pass

        return

    def get_rawHtml(self):
        start_page = requests.get(self.start_url, headers = agent)
        soup = BeautifulSoup(start_page.content, "html.parser")

        for js in soup(["script", "style"]):
            js.extract()

        return soup.get_text().encode("utf-8")

url = 'https://www.zapimoveis.com.br/lancamento/apartamento+venda+socorro+jaboatao-dos-guararapes+pe+reserva-villa-natal--goiabeiras+mrv-engenharia-s-a+49m2/ID-9704/?oti=1'
url2 = 'https://www.expoimovel.com/imovel/apartamentos-comprar-vender-imbui-salvador-bahia/389449/pt/BR'
url3 = 'http://pe.olx.com.br/grande-recife/imoveis/excelente-locacao-engenho-do-meio-397980090'
ri = Regex_scrapper(url3)
ri.crawl()