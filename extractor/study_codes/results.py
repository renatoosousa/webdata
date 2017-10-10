import pandas as pd 

urls = pd.read_csv('../../classifier/dataframe/urls.csv')
zapimoveis = []
expoimovel = []


for index, webpage in urls.iterrows():
    if webpage['label'] == 1:
        if webpage['site'].find('zapi') != -1:
            print webpage['site']
            print "\n\n\n"