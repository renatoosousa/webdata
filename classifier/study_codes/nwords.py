import pandas as pd
import operator
import matplotlib.pyplot as plt

def filter_txt(txt):
    stopw = (open('stopwords.txt', 'r')).read()
    for word in stopw.split():
        txt = txt.replace(" "+word+" "," ")
    txt = txt.decode('utf-8')
    
    splits = [',', '(', ')', '[', ']', '.', '!', '?', ';', ':', '/', '|', '"', '+', '-']
    for split in splits:
        txt = txt.replace(split, ' ')
    return txt

url = 'https://www.zapimoveis.com.br/lancamento/apartamento+venda+boa-viagem+recife+pe+jardim-das-orquideas+moura-dubeux+95m2-124m2/ID-13235/?contato=0'

text = open('text.txt', 'r')
txt = text.read() + '\n' + url

txt = filter_txt(txt.lower())

wordcount = {}

#text.read().split()
for word in txt.split():
	if word not in wordcount:
		wordcount[word] = 1
	else:
		wordcount[word] += 1

wordcount_sorted = sorted(wordcount.items(), key=operator.itemgetter(1))

#for k in wordcount:
#    print k

header = [x for x in wordcount]
elemns = [wordcount[key] for key in wordcount]
# print(type(wordcount[0]))

df = pd.DataFrame.from_dict(elemns).T
df.columns = header
#df = df.pivot(header)

#row = df.iloc[0]
#row.plot(kind='bar')
#plt.show()
