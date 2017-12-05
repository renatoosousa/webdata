import re

regex_value = "[Vv][aA][lL][oO][Rr](.+)?:\s?R\$\s?\d+[,.]\d+([,.]\d+)?"
regex_quartos = ["[Qq][uU][aA][rR][tT].+:\s\d", "[Dd][Oo][Rr][Mm].+:\s\d"]

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
        

doc = "results/docs/doc_"
for i in range(255,355):
    doc_name = doc + str(i) + ".txt"
    with open(doc_name) as f:
        data = f.read()
        quartos = get_quartos(data)
        print quartos
        #z = input()


#banheiros, quartos, cidade, valor, vaga