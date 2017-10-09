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

        raw_data = []
        for string in info.stripped_strings:
            raw_data.append(string)

        print raw_data

        self.post_processing(raw_data)
        return

    def post_processing(self, raw_data):
        '''
            padroes:
                [valor, campo]
                [lixo, lixo, valor, campo, lixo, lixo]
                [campo:, valor]
                [lixo, lixo... , campo: valor,]
                [valor campo valor campo valor campo]
                [campo, valor, campo, valor]
        '''
        self.try_pattern1(raw_data)
        pattern1 = "(\d+\s+.+)|(.+\s+\d+)"

    def try_pattern1(self, raw_data):
        pattern_Digits = "\d+"
        pattern_NonDigits = "\D+"
        regex = "([Qq]uartos?)|(Dorm)|([Vv]aga)|([Ss]u)|([Bb]anh)"

        
        digit = 0
        nonDigit = 0
        digit_Ocurrences = []
        nonDigit_Ocurrences = []
        #procura e conta palavras e numeros
        for i in range(0, len(raw_data)):
            #print raw_data[i]
            try:
                x = re.search(pattern_Digits, raw_data[i]).group()
                if raw_data[i] == x:
                    #print "match -> " + raw_data[i]
                    digit += 1
                    digit_Ocurrences.append(i)

            except Exception, e:
                print str(e)

            try:
                y = re.search(pattern_NonDigits, raw_data[i]).group()
                if raw_data[i] == y:
                    #print "match -> " + raw_data[i]
                    nonDigit += 1
                    nonDigit_Ocurrences.append(i)
            except Exception, e:
                print str(e)


        if digit == nonDigit:
            for i, j in zip(digit_Ocurrences, nonDigit_Ocurrences):
                print raw_data[j] + ": " + raw_data[i]
        else:
            if raw_data[-1] == raw_data[digit_Ocurrences[-1]]:
                if re.search(regex, raw_data[-2]):
                    for i in digit_Ocurrences:
                        print raw_data[i - 1] + ": " + raw_data[i]
                for i in range(0, len(digit_Ocurrences)-1):
                    print raw_data[digit_Ocurrences[i]+1] + ": " + raw_data[digit_Ocurrences[i]]


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