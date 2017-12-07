#!/usr/bin/python2.4
# -*- coding: utf-8 -*-

# list1 = ['http://www.directimoveis.com.br/imovel-v0932/edf-parador-de-cervantes\nBanheiros: 2\n\xc3\x81rea \xc3\xbatil: 60,00 m\xc2\xb2\nArea Total: \xc3\x81rea total n\xc3\xa3o consta\nTipo: Apartamento Padr\xc3\xa3o\nBairro: Boa Viagem\nCidade: Recife\nVagas de garagem: 2\nIPTU: R$ 148,00\nDormit\xc3\xb3rios: 2 (sendo 1 su\xc3\xadtes)\nCondominio: 400\nValor: R$ 530.000,00\nEstado: PE\n',
#  '\n\n\nhttp://www.directimoveis.com.br/imovel-AL0101\nTipo: O melhor para o seu neg\xc3\xb3cio\n',
#  '\n\n\nhttp://www.directimoveis.com.br/imovel-AL0141\nBanheiros: 1\n\xc3\x81rea \xc3\xbatil: 211,00 m\xc2\xb2\nArea Total: \xc3\x81rea total 440,00\nTipo: Comercial Casa\nBairro: Aflitos\nCidade: Recife\nVagas de garagem: 5\nIPTU: R$ 540,00\nCondominio: 244\nValor: R$ 4.500,00\nEstado: PE\n',
#  '\n\n\nhttp://www.directimoveis.com.br/imovel-V0390/edificio-maison-languth\nBanheiros: 1\n\xc3\x81rea \xc3\xbatil: 125,00 m\xc2\xb2\nArea Total: \xc3\x81rea total n\xc3\xa3o consta\nTipo: Apartamento Padr\xc3\xa3o\nBairro: Aflitos\nCidade: Recife\nVagas de garagem: 2\nDormit\xc3\xb3rios: 3 (sendo 1 su\xc3\xadtes)\nCondominio: 700\nValor: R$ 320.000,00\nEstado: PE\n',
#  '\n\n\nhttp://www.directimoveis.com.br/imovel-V0496/verano\nBanheiros: 1\n\xc3\x81rea \xc3\xbatil: 97,00 m\xc2\xb2\nArea Total: \xc3\x81rea total n\xc3\xa3o consta\nTipo: Apartamento Padr\xc3\xa3o\nBairro: 2, R\nCidade: Praia do Pai\nVagas de garagem: 2\nDormit\xc3\xb3rios: 3 (sendo 3 su\xc3\xadtes)\nValor: R$ 800.000,00\nEstado: a\n']

#  


# fi = open("dicionario.txt", "r")

alist = [line.rstrip() for line in open('dic_city.txt')]
print alist
	

