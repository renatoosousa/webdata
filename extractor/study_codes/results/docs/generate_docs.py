import re

extracted_data = [ "../directimoveis.txt",
                "../expoimovel.txt",
                "../imoveisavenda.txt",
                "../imovelweb.txt",
                "../lugarcerto.txt",
                "../olx.txt",
                "../redeimoveispe.txt",
                "../teuimovel.txt",
                "../vivareal.txt",
                "../zapi.txt" ]

aux = []
doc_index = 255

for file in extracted_data:
    with open(file) as f:
        data = f.readlines()
        for line in data:
            line = line.strip()
            doc_name = "doc_" + str(doc_index) + ".txt"
            docs = open(doc_name, "a")
            if line.isdigit():
                doc_index = doc_index + 1
                docs.close()
                doc_name = "doc_" + str(doc_index) + ".txt"
                print doc_name
                docs = open(doc_name, "a")
                #z = input()
            else:
                docs.write(line + "\n")
                #print line
                #z = input()
