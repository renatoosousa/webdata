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

def countWords(txt):
    wordcount = {}
    
    for word in txt.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount

def all_keys(dictlist):
    return list(set().union(*dictlist))

def getValue(dic, word):
    count = 0
    try:
        count = dic[word]
    except:
        count = 0
    return count

def dict2row(dic, header):
    return [(getValue(dic, word)) for word in header]


url1 = 'https://www.zapimoveis.com.br/lancamento/apartamento+venda+boa-viagem+recife+pe+jardim-das-orquideas+moura-dubeux+95m2-124m2/ID-13235/?contato=0'
url2 = 'https://www.zapimoveis.com.br/lancamento/apartamento+venda+boa-viagem+recife+pe+jardim-das-acacias+moura-dubeux+185m2/ID-13234/?contato=0'
url3 = 'https://revista.zapimoveis.com.br/?utm_source=zapimoveis&utm_medium=link-header&utm_campaign=btn-zapemcasa&_ga=2.41900458.9832649.1504960224-2135475700.1504045699'

text = open('text1.txt', 'r')
txt1 = text.read() + '\n' + url1
text.close()

text = open('text2.txt', 'r')
txt2 = text.read() + '\n' + url2
text.close()

text = open('text3.txt', 'r')
txt3 = text.read() + '\n' + url3
text.close()

txt1 = filter_txt(txt1.lower())
txt2 = filter_txt(txt2.lower())
txt3 = filter_txt(txt3.lower())
dict1 = countWords(txt1)
dict2 = countWords(txt2)
dict3 = countWords(txt3)

alldict = [dict1, dict2, dict3]
allkey = all_keys(alldict)

row1 = dict2row(dict1, allkey)
row2 = dict2row(dict2, allkey)
row3 = dict2row(dict3, allkey)

df = pd.DataFrame(columns = allkey)
df.loc[0] = row1
df.loc[1] = row2
df.loc[2] = row3
#wordcount_sorted = sorted(wordcount.items(), key=operator.itemgetter(1))

#for k in wordcount:
#    print k

#header = [x for x in wordcount]
#elemns = [wordcount[key] for key in wordcount]
## print(type(wordcount[0]))
#
#df = pd.DataFrame.from_dict(elemns).T
#df.columns = header
##df = df.pivot(header)
#
##row = df.iloc[0]
##row.plot(kind='bar')
##plt.show()
