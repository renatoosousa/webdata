import re
import sys
import pickle

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
        #print item
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



def insert_reverseindex_quartos(id, valor):

    if not dist_quartos.get(valor):
        dist_quartos[valor] = [id]
    else:
        dist_quartos[valor].append(id)

    dist_termos["quartos"].append(id)

    if id > 255:
        id -= 255
    if not dist_comp_quartos.get(valor):
        dist_comp_quartos[valor] = [id]
    else:
        dist_comp_quartos[valor].append(id)

    dist_comp_termos["quartos"].append(id)


def insert_reverseindex_valor(id, valor):

    if valor >= 480.0 and valor < 100000.0:
        dist_valor["480-10k"].append(id)

    elif valor >= 10000.0 and valor < 135000.0:
        dist_valor["10k-135k"].append(id)

    elif valor >= 135000.0 and valor < 225500.0:
        dist_valor["135k-225.5k"].append(id)

    elif valor >= 225500.0 and valor < 330000.0:
        dist_valor["225.5k-330k"].append(id)

    elif valor >= 330000.0 and valor < 480000.0:
        dist_valor["330k-480k"].append(id)

    elif valor >= 480000.0 and valor < 650000.0:
        dist_valor["480k-650k"].append(id)

    elif valor >= 650000.0 and valor < 850000.0:
        dist_valor["650k-850k"].append(id)

    elif valor >= 850000.0 and valor < 980000.0:
        dist_valor["850k-980k"].append(id)

    elif valor >= 980000.0 and valor < 1600000.0:
        dist_valor["980k-1.6kk"].append(id)

    elif valor >= 1600000.0 and valor < 2200000.0:
        dist_valor["1.6kk-2.2kk"].append(id)

    elif valor >= 2200000.0 and valor < 3800000.0:
        dist_valor["2.2kk-3.8kk"].append(id)

    elif valor >= 3800000.0:
        dist_valor["3.8kk+"].append(id)


    if id > 255:
        id -= 255

    if valor >= 480.0 and valor < 100000.0:
        dist_comp_valor["480-10k"].append(id)

    elif valor >= 10000.0 and valor < 135000.0:
        dist_comp_valor["10k-135k"].append(id)

    elif valor >= 135000.0 and valor < 225500.0:
        dist_comp_valor["135k-225.5k"].append(id)

    elif valor >= 225500.0 and valor < 330000.0:
        dist_comp_valor["225.5k-330k"].append(id)

    elif valor >= 330000.0 and valor < 480000.0:
        dist_comp_valor["330k-480k"].append(id)

    elif valor >= 480000.0 and valor < 650000.0:
        dist_comp_valor["480k-650k"].append(id)

    elif valor >= 650000.0 and valor < 850000.0:
        dist_comp_valor["650k-850k"].append(id)

    elif valor >= 850000.0 and valor < 980000.0:
        dist_comp_valor["850k-980k"].append(id)

    elif valor >= 980000.0 and valor < 1600000.0:
        dist_comp_valor["980k-1.6kk"].append(id)

    elif valor >= 1600000.0 and valor < 2200000.0:
        dist_comp_valor["1.6kk-2.2kk"].append(id)

    elif valor >= 2200000.0 and valor < 3800000.0:
        dist_comp_valor["2.2kk-3.8kk"].append(id)

    elif valor >= 3800000.0:
        dist_comp_valor["3.8kk+"].append(id)

    

def insert_reverseindex_cidade(id, cidade):

    if not dist_cidades.get(cidade):
        dist_cidades[cidade] = [id]
    else:
        dist_cidades[cidade].append(id)

    dist_termos["cidades"].append(id)

    if id > 255:
        id -= 255
    if not dist_comp_cidades.get(cidade):
        dist_comp_cidades[cidade] = [id]
    else:
        dist_comp_cidades[cidade].append(id)

    dist_comp_termos["cidades"].append(id)


def insert_reverseindex_banheiros(id, banheiros):

    if not dist_banheiros.get(banheiros):
        dist_banheiros[banheiros] = [id]
    else:
        dist_banheiros[banheiros].append(id)

    dist_termos["banheiros"].append(id)

    if id > 255:
        id -= 255
    if not dist_comp_banheiros.get(banheiros):
        dist_comp_banheiros[banheiros] = [id]
    else:
        dist_comp_banheiros[banheiros].append(id)

    dist_comp_termos["banheiros"].append(id)


def insert_reverseindex_vagas(id, vagas):

    if not dist_vagas.get(vagas):
        dist_vagas[vagas] = [id]
    else:
        dist_vagas[vagas].append(id)

    dist_termos["vagas"].append(id)

    if id > 255:
        id -= 255
    if not dist_comp_vagas.get(vagas):
        dist_comp_vagas[vagas] = [id]
    else:
        dist_comp_vagas[vagas].append(id)

    dist_comp_termos["vagas"].append(id)



doc = "results/docs/doc_"

dist_termos = {"quartos":[], "banheiros":[], "vagas":[], "valor":[], "cidades":[]}
dist_comp_termos = {"quartos":[], "banheiros":[], "vagas":[], "valor":[], "cidades":[]}


dist_quartos = {}
dist_banheiros = {}
dist_vagas = {}
dist_cidades = {}
dist_valor = {"480-10k":[], "10k-135k":[],"135k-225.5k":[], "225.5k-330k":[], "330k-480k":[], "480k-650k":[],
                "650k-850k":[], "850k-980k":[], "980k-1.6kk":[], "1.6kk-2.2kk":[], "2.2kk-3.8kk":[], "3.8kk+":[]}
dist_comp_quartos = {}
dist_comp_banheiros = {}
dist_comp_valor = {"480-10k":[], "10k-135k":[],"135k-225.5k":[], "225.5k-330k":[], "330k-480k":[], "480k-650k":[],
                "650k-850k":[], "850k-980k":[], "980k-1.6kk":[], "1.6kk-2.2kk":[], "2.2kk-3.8kk":[], "3.8kk+":[]}
dist_comp_cidades = {}
dist_comp_vagas = {}


for i in range(255,355):
    doc_name = doc + str(i) + ".txt"
    with open(doc_name) as f:
        data = f.read()

        #print "doc id: ", i
        #processing valor
        valor = get_valor(data)
        insert_reverseindex_valor(i, valor)

        #processing quartos
        quartos = get_quartos(data)
        insert_reverseindex_quartos(i, quartos)
        
        #processing cidade
        cidade = get_cidade(data)
        insert_reverseindex_cidade(i, cidade)


        # #processing banheiro
        banheiros = get_banheiros(data)
        insert_reverseindex_banheiros(i, banheiros)


        #processing vagas
        vagas = get_vagas(data)
        if not dist_vagas.get(vagas):
            dist_vagas[vagas] = [i]
        else:
            dist_vagas[vagas].append(i)

        #z = raw_input()'''
    '''print "------------------------------"

print "distribuicao quartos: ", dist_quartos
print "\n\ndistribuicao quartos: ", dist_comp_quartos
print "\n\ndistribuicao banheiros: ", sorted(dist_banheiros.items())
print "\n\ndistribuicao banheiros: ", sorted(dist_comp_banheiros.items())
print "distribuicao vagas: ", sorted(dist_vagas.items())
print "distribuicao vagas: ", sorted(dist_comp_vagas.items())
print "\n\ndistribuicao cidades: ", sorted(dist_cidades.items())
print "\n\ndistribuicao cidades: ", sorted(dist_comp_cidades.items())
print "\n\ndistribuicao valor: ", sorted(dist_valor.items())
print "\n\ndistribuicao valor: ", sorted(dist_comp_valor.items())
print "\n\ntermos: ", dist_termos
print "\n\ntermos: ", dist_comp_termos

print "termos size: ", sys.getsizeof(dist_termos)
print "termos_comp size: ", sys.getsizeof(dist_comp_termos)

print len(dist_valor)
for item in sorted(dist_valor.items()):
    print item
'''

file = open("reverse_index.txt", "w")

dist_banheiros.pop(-1, None)
print "BANHEIROS"
for item in dist_banheiros:
    print str(item) + ": ",
    print dist_banheiros[item]
    pickle.dump(dist_banheiros[item], file)

dist_cidades.pop(-1, None)
print "CIDADE"
for item in dist_cidades:
    print str(item) + ": ",
    print dist_cidades[item]
    pickle.dump(dist_cidades[item],file)

print "QUARTOS"
dist_quartos.pop(-1, None)
for item in dist_quartos:
    print str(item) + ": ",
    print dist_quartos[item]
    pickle.dump(dist_quartos[item],file)

print "VAGAS"
dist_vagas.pop(-1, None)
for item in dist_vagas:
    print str(item) + ": ",
    print dist_vagas[item]
    pickle.dump(dist_vagas[item], file)

print "VALOR"
for item in dist_valor:
    print str(item) + ": ",
    print dist_valor[item]
    pickle.dump(dist_valor[item], file)




file.close()


#banheiros, quartos, cidade, valor, vaga