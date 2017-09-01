import operator
import pandas as pd
import re

text = open('text.txt', 'r')
txt = text.read()

#eleminate some chars
txt = txt.replace(",", " ")
txt = txt.replace("(", " ")
txt = txt.replace(")", " ")
txt = txt.replace(".", " ")
txt = txt.replace(",", " ")
txt = txt.replace("[", " ")
txt = txt.replace("]", " ")

wordcount = {}

#text.read().split()
for word in txt.split():
	if word not in wordcount:
		wordcount[word] = 1
	else:
		wordcount[word] += 1

#wordcount = sorted(wordcount.items(), key=operator.itemgetter(1))

#for k in wordcount:
#    print k

header = [x for x in wordcount]
elemns = [wordcount[key] for key in wordcount]
# print(type(wordcount[0]))

df = pd.DataFrame.from_dict(elemns).T
df.columns = header
#df = df.pivot(header)
