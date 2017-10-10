# -*- coding: utf-8 -*-

import requests
import os
import bs4
from bs4 import BeautifulSoup
import re




agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
          'Accept-Language': 'pt-BR',
          'Accept-Charset': 'utf-8'	}

class Regex_scrapper:

    def __init__(self, start_url):
        self.start_url = start_url
        self.data = {}
        self.pattern = 0

    def crawl(self):
        info = self.pre_processing()

        raw_data = []
        for string in info.stripped_strings:
            raw_data.append(string)

        #print raw_data

        self.post_processing(raw_data)

       
        for key, value in self.data.items():
            if re.search("R\$", key):
                self.data.pop(key,None)
        
        for key in self.data:
                print key + ": " + self.data[key]

        return

    def post_processing(self, raw_data):

        self.try_pattern2(raw_data)
        if not self.pattern:
            self.try_pattern1(raw_data)

        #print "pattern: " + str(self.pattern)

    def try_pattern1(self, raw_data):
        self.pattern = 1

        pattern_Digits = "\d+"
        pattern_NonDigits = "\D+"
        regex = "([Qq]uartos?)|(Dorm)|([Vv]aga)|([Ss]u)|([Bb]anh)"

        
        digit = 0
        nonDigit = 0
        digit_Ocurrences = []
        nonDigit_Ocurrences = []

        for i in range(0, len(raw_data)):
            try:
                x = re.search(pattern_Digits, raw_data[i]).group()
                if raw_data[i] == x:
                    digit += 1
                    digit_Ocurrences.append(i)

            except Exception, e:
                pass

            try:
                y = re.search(pattern_NonDigits, raw_data[i]).group()
                if raw_data[i] == y:
                    nonDigit += 1
                    nonDigit_Ocurrences.append(i)
            except Exception, e:
                pass

        if digit == nonDigit:
            for i, j in zip(digit_Ocurrences, nonDigit_Ocurrences):
                #print raw_data[j] + ": " + raw_data[i]
                self.data[raw_data[j]] = raw_data[i]
        else:
            if raw_data[-1] == raw_data[digit_Ocurrences[-1]]:
                if re.search(regex, raw_data[-2]):
                    for i in digit_Ocurrences:
                        #print raw_data[i - 1] + ": " + raw_data[i]
                        self.data[raw_data[i-1]] = raw_data[i]
                else:
                    for i in range(0, len(digit_Ocurrences)-1):
                        #print raw_data[digit_Ocurrences[i]+1] + ": " + raw_data[digit_Ocurrences[i]]
                        self.data[raw_data[digit_Ocurrences[i]+1]] = raw_data[digit_Ocurrences[i]]

            else:
                for i in digit_Ocurrences:
                    #print raw_data[i+1] + ": " + raw_data[i]
                    self.data[raw_data[i+1]] = raw_data[i]

    def try_pattern2(self, raw_data):
        regex = "([Vv]aga.+\d+)|(\d+.+[Vv]aga(.+)?$)"

        for i in range(0, len(raw_data)):
            try:
                if re.search(regex, raw_data[i]).group():
                    self.pattern = 2
                    break
            except Exception, e:
                pass


        if  self.pattern != 2:
            return
        else:
            for i in raw_data:
                try:
                    if re.search("\d+", i):
                        split = 0
                        try:
                            out = i.split(':')
                            if len(out) == 2:
                                #print out[0] + ": " + out[1]
                                self.data[out[0]] = out[1]
                                split = 1
                            elif len(out) == 1:
                                if not split:
                                    out = i.split(' ')
                                    if len(out) == 1 or len(out) > 20:
                                        out = []
                                    else:
                                        self.try_pattern1(out)
                        except:
                            pass

                except Exception, e:
                    pass



    def pre_processing(self):
        start_page = requests.get(self.start_url, headers = agent)
        soup = BeautifulSoup(start_page.content, "html.parser")

        # for js in soup(["script", "style"]):
        #     js.extract()


        regex_prices = "(R\$\s?\d+([.,])?\d+)"
        regex_priceNu = "\d+([,.]\d+)?"
        regex_casa_apt = "([cC][aA][sS][aA])|([aA][pP][aA][rR][tT])|([fF][lL][aA][tT])|([lL][oO][jJ][aA])"
        regex_address_av = "[Aa][vV](.)?([eE][nN][iI])?.+-\s\w+"
        regex_address_rua = "[Rr][uU][aA].+-?\w+$"
        try:
            prices = []
            price = re.findall(regex_prices, soup.text)
            while len(price) > 4:
                price.pop()
            for item in price:
                try:
                    #print item
                    prices.append(float(re.search(regex_priceNu, str(item)).group()))
                except:
                    pass
            self.data["Valor"] = str(max(prices))

            imovel = re.search(regex_casa_apt, soup.text).group()
            if imovel:
                self.data["Imovel"] = imovel

            address = soup.find("address")
            print address
            if not address:
                address = re.search(regex_address_av, soup.text).group()
                print address
                if address:
                    print address
                print address
                else:
                    address = re.search(regex_address_rua, soup.text).group()
                    if address:
                        print address
            else:
                address = address.text
                print address    
        

        except Exception, e:
            print str(e)
        


        uls = soup.find_all("ul")
        divs = soup.find_all("div")

        regex = "([Qq][uU][aA][rR][tT][oO][sS]?)|(Dorm)"

        foundUL = 0
        for ul in uls:
            if re.search(regex, ul.text):
                if re.search("[Vv][aA][gG][aA]", ul.text):
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

'''urlx = 'http://www.imovelweb.com.br/propriedades/apartamento-locacao-boa-viagem-2-quartos-2932218024.html?labs=I-spark-sep_&labs_source=Recomendados_ficha_propiedad_desktop&userid=0'
ri = Regex_scrapper(urlx)
ri.crawl()'''
for url in urls:
    ri = Regex_scrapper(url)
    ri.crawl()
    z = input()

