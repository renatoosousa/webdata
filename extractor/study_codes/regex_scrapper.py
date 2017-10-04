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
            quartos = re.search("(\d+\s[Qq]uartos?) | ([Qq]uartos?(\s:?\s)\d+)", html)
            valor = re.search("R\$\s\d+[,.]\d+", html)
            vagas = re.search("[vV]agas? | (\d+\s?[vV]agas?)",html)
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

        return soup.body.get_text().encode("utf-8")
urls = [
        'https://www.zapimoveis.com.br/lancamento/apartamento+venda+socorro+jaboatao-dos-guararapes+pe+reserva-villa-natal--goiabeiras+mrv-engenharia-s-a+49m2/ID-9704/?oti=1',
        'https://www.expoimovel.com/imovel/apartamentos-comprar-vender-imbui-salvador-bahia/389449/pt/BR',
        'http://pe.olx.com.br/grande-recife/imoveis/excelente-locacao-engenho-do-meio-397980090',
        'http://www.directimoveis.com.br/imovel-V0373/morada-da-peninsula',
        'http://imovelavenda.com.br/Fiateci_Apto_2_Dorm_Sao_Geraldo_Porto_Alegre_10066_RS__YWQ10',
        'http://www.imovelweb.com.br/propriedades/apartamento-residencial-para-locacao-boa-viagem-2932218008.html',
        'http://diariodepernambuco.lugarcerto.com.br/imovel/casa-em-condominio-2-quartos-aldeia-camaragibe-54m2-venda-rs230000-id-329299726',
        'http://www.redeimoveispe.com.br/imovel-detalhes.aspx?refRede=AP0193-CZA',
        'http://www.teuimovel.com/index_detalheimovel_id_1783_desc_sao-paulo-sp-paraIso',
        'https://www.vivareal.com.br/imovel/apartamento-3-quartos-butanta-zona-oeste-sao-paulo-com-garagem-70m2-venda-RS369000-id-84167740/?__vt=map:b',
]


print urls
ri = Regex_scrapper(urls[0])
ri.crawl()