import re
from collections import defaultdict

regex_value = "[Vv][aA][lL][oO][Rr](.+)?:\s?R\$\s?\d+[,.]\d+([,.]\d+)?"
regex_quartos = ["[Qq][uU][aA][rR][tT].+:\s\d", "[Dd][Oo][Rr][Mm].+:\s\d"]
regex_cidade = ["[cC][iI][dD][aA][dD].+", "[mM][uU][nN][iI][cC].+", "[eE][nN][dD][eE][rR][eE].+"]
regex_banheiro = ["[bB][aA][nN][hH][eE].+", "[sS][uU].+:\s\d"]

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
                return cidade.lower()


    try:
        cidade = cidade[0].split(':')
        cidade = cidade[1]
    except:
        cidade = -1
        return cidade
    #print cidade
    return cidade.lower()

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

doc = "results/docs/doc_"
dist_quartos = {}
dist_banheiros = {}
for i in range(255,355):
    doc_name = doc + str(i) + ".txt"
    with open(doc_name) as f:
        data = f.read()

        #processing quartos
        quartos = get_quartos(data)
        if not dist_quartos.get(quartos):
            dist_quartos[quartos] = 1
        else:
            dist_quartos[quartos] += 1
        print "quartos: ", quartos

        #processing cidade
        cidade = get_cidade(data)
        print "cidade: ", cidade
        print "doc id: ", i


        #processing banheiro
        banheiros = get_banheiros(data)
        if not dist_banheiros.get(banheiros):
            dist_banheiros[banheiros] = 1
        else:
            dist_banheiros[banheiros] += 1
        print "banheiros: ", banheiros
        #z = raw_input()

print "distribuicao quartos: ", dist_quartos
print "distribuicao banheiros: ", dist_banheiros

# sum = 0
# for item in dist_quartos:
#     sum += dist_quartos[item]
# print sum

#banheiros, quartos, cidade, valor, vaga