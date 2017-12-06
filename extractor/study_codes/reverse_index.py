import re
from collections import defaultdict

regex_valor = "R\$.+"
regex_quartos = ["[Qq][uU][aA][rR][tT].+:\s\d", "[Dd][Oo][Rr][Mm].+:\s\d"]
regex_cidade = ["[cC][iI][dD][aA][dD].+", "[mM][uU][nN][iI][cC].+", "[eE][nN][dD][eE][rR][eE].+"]
regex_banheiro = ["[bB][aA][nN][hH][eE].+", "[sS][uU].+:\s\d"]
regex_vagas = ["[vV][aA][gG].+:\s\d", "[gG][aA][rR][aA][gG][eE].+:\s\d"]

def get_valor(data):
    valor = re.findall(regex_valor, data)
    if not valor:
        return -1
    #print valor
    max = 0.0
    for item in valor:
        item = item.split(' ')
        item = item[1].replace('.', '')
        item = item.replace(',', '.')
        try:
            item = float(item)
        except:
            item = 0.0
        print item
        if item > max:
            max = item
    
    #print "valor: ", max
    return max


def get_quartos(data):

    quartos = re.findall(regex_quartos[0], data)
    if not quartos:
        quartos = re.findall(regex_quartos[1], data)
        #print quartos
    try: 
        quartos = quartos[0].split(':')
        quartos = int(quartos[1])
    except:
        quartos = -1

    return quartos

def get_cidade(data):

    cidade = re.findall(regex_cidade[0], data)
    if not cidade:
        cidade = re.findall(regex_cidade[1], data)
        if not cidade:
            cidade = re.findall(regex_cidade[2], data)
            if cidade :
                cidade = cidade[0].split(' ')
                cidade = cidade[-1].split('-')
                cidade = cidade[0]
                #print cidade
                return cidade.lower().strip()


    try:
        cidade = cidade[0].split(':')
        cidade = cidade[1]
    except:
        cidade = -1
        return cidade
    #print cidade
    return cidade.lower().strip()

def get_banheiros(data):
    banheiro = re.findall(regex_banheiro[0], data)
    if not banheiro:
        banheiro = re.findall(regex_banheiro[1], data)

    if banheiro:
        banheiro = banheiro[0].split(' ')
        banheiro = int(banheiro[1])
        return banheiro
    else:
        return -1

def get_vagas(data):
    vagas = re.findall(regex_vagas[0], data)
    if not vagas:
        vagas = re.findall(regex_vagas[1], data)
        if not vagas:
            return -1
    
    vagas = vagas[0].split(' ')
    vagas = int(vagas[-1])
    return vagas

doc = "results/docs/doc_"
dist_quartos = {}
dist_banheiros = {}
dist_vagas = {}
dist_cidades = {}
dist_valor = {}
for i in range(255,355):
    doc_name = doc + str(i) + ".txt"
    with open(doc_name) as f:
        data = f.read()

        print "doc id: ", i
        #processing valor
        valor = get_valor(data)
        if not dist_valor.get(valor):
            dist_valor[valor] = 1
        else:
            dist_valor[valor] += 1
        print "valor: ", valor


        #processing quartos
        quartos = get_quartos(data)
        if not dist_quartos.get(quartos):
            dist_quartos[quartos] = 1
        else:
            dist_quartos[quartos] += 1
        print "quartos: ", quartos

        #processing cidade
        cidade = get_cidade(data)
        if not dist_cidades.get(cidade):
            dist_cidades[cidade] = 1
        else:
            dist_cidades[cidade] += 1

        print "cidade: ", cidade


        #processing banheiro
        banheiros = get_banheiros(data)
        if not dist_banheiros.get(banheiros):
            dist_banheiros[banheiros] = 1
        else:
            dist_banheiros[banheiros] += 1
        print "banheiros: ", banheiros

        #processing vagas
        vagas = get_vagas(data)
        if not dist_vagas.get(vagas):
            dist_vagas[vagas] = 1
        else:
            dist_vagas[vagas] += 1
        print "vagas: ", vagas

        #z = raw_input()
    print "------------------------------"

print "distribuicao quartos: ", sorted(dist_quartos.items())
print "distribuicao banheiros: ", sorted(dist_banheiros.items())
print "distribuicao vagas: ", sorted(dist_vagas.items())
print "distribuicao cidades: ", sorted(dist_cidades.items())
print "distribuicao valor: ", sorted(dist_valor.items())

for item in dist_cidades:
    print item



# sum = 0
# for item in dist_quartos:
#     sum += dist_quartos[item]
# print sum

#banheiros, quartos, cidade, valor, vaga