# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup
import re



file = open("/Users/vbas/Documents/UFPE/RI/htmls.html", "w")

agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
          'Accept-Language': 'pt-BR'}

class Regex_scrapper:

    def __init__(self, start_url):
        self.start_url = start_url
        self.data = {}
        self.title = ""

    def crawl(self):
        info = self.pre_processing()

        for string in info.stripped_strings:
            print string
            print "\n\n\n"

        # x = info.contents
        # for item in x:
        #     print item
        #     print "\n\n\n"
        # print self.start_url
        # # x = input()
        # # os.system("clear")

        file.write(info.prettify().encode("utf-8"))
        file.write("\n------------------------------------------------------------------------ FIM DO HTML --------------------------------------------------------------------------------------\n")
        # print dir(info)
        # print info.prettify()        
        

        return

    def pre_processing(self):
        start_page = requests.get(self.start_url, headers = agent)
        soup = BeautifulSoup(start_page.content, "html.parser")

        for js in soup(["script", "style"]):
            js.extract()

        uls = soup.find_all("ul")
        divs = soup.find_all("div")

        regex = "([Qq]uartos?)|(Dorm)"

        foundUL = 0
        #print "*"*71
        for ul in uls:
            if re.search(regex, ul.text):
                if re.search("[Vv]aga", ul.text):
                    info = ul
                    foundUL = 1
                    break
        if foundUL:
            return info

        for div in divs:
            if re.search(regex, div.text):
                info = div
                break
        
        for div in info.find_all("div"):
            if re.search(regex, div.text):
                if re.search("[Vv]aga", div.text):
                    info = div
        
        return info

urls = [
        'https://www.zapimoveis.com.br/lancamento/apartamento+venda+socorro+jaboatao-dos-guararapes+pe+reserva-villa-natal--goiabeiras+mrv-engenharia-s-a+49m2/ID-9704/?oti=1',
        'https://www.expoimovel.com/imovel/apartamentos-comprar-vender-imbui-salvador-bahia/389449/pt/BR',
        'http://pe.olx.com.br/grande-recife/imoveis/excelente-locacao-engenho-do-meio-397980090',
        'http://www.directimoveis.com.br/imovel-V0373/morada-da-peninsula',
        'http://imovelavenda.com.br/Fiateci_Apto_2_Dorm_Sao_Geraldo_Porto_Alegre_10066_RS__YWQ10',
        'http://www.imovelweb.com.br/propriedades/apartamento-residencial-para-locacao-boa-viagem-2932218008.html',
        'http://diariodepernambuco.lugarcerto.com.br/imovel/casa-em-condominio-2-quartos-aldeia-camaragibe-54m2-venda-rs230000-id-329299726',
        'http://www.redeimoveispe.com.br/imovel-detalhes.aspx?refRede=AP0193-CZA',
        'http://www.teuimovel.com/index_detalheimovel_id_2116_desc_sao-paulo-sp-vila-silvia',
        'https://www.vivareal.com.br/imovel/apartamento-3-quartos-butanta-zona-oeste-sao-paulo-com-garagem-70m2-venda-RS369000-id-84167740/?__vt=map:b',
]

for url in urls:
    ri = Regex_scrapper(url)
    ri.crawl()
    z = input()

file.close()