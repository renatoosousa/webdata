import pandas as pd
import sys
sys.path.append('../../extractor/study_codes/')

from zapi_bs import Zapi_crawler
from nltk.stem import RSLPStemmer

def filter_txt(txt):
    stopw = (open('../study_codes/stopwords.txt', 'r')).read()
    for word in stopw.split():
        txt = txt.replace(" "+word+" "," ")
    txt = txt.decode('utf-8')
    
    
    splits = [',', '(', ')', '[', ']', '.', '!', '?', ';', ':', '/', '|', '"',
              '+', '-', '_', '#', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
              '\'', '\\', '\t', '\n', '>', '<', '*']
#    splits = [',', '(', ')', '[', ']', '.', '!', '?', ';', ':', '/', '|', '"',
#              '+', '-', '_', '#', '\'', '\\', '\t', '\n', '>', '<', '*']
    for split in splits:
        txt = txt.replace(split, ' ')
    
    st = RSLPStemmer()
    txt2 = ""
    for token in txt.split():
        txt2 = txt2 + ' ' + (st.stem(token))
        
    return txt2

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

def makedb(df_name):
    # dataframe with urls and labels
    urls = pd.read_csv('../dataframe/urls.csv')
    
    wrapper = Zapi_crawler('')
    alldict = []
    sucess = 0
    
    for index, webpage in urls.iterrows():
        wrapper.start_url = webpage['site']
        
        try:
            txt = filter_txt(wrapper.get_rawHtml().lower()) 
            alldict.append(countWords(txt))
            sucess += 1
            print("\n" + "sucess=" + str(sucess) + " " + wrapper.start_url + "\n")
        except:
            print("\n\n" + "error: "+ wrapper.start_url + "\n\n")
        
    allkeys = all_keys(alldict)
    header = all_keys(alldict)
    header.append('label')
    df = pd.DataFrame(columns = header)
    
    for idx, i_dict in enumerate(alldict):
        row = dict2row(i_dict, allkeys)
        row.append(urls.loc[idx]['label'])
        df.loc[idx] = row
    
    df_name = df_name + '.csv'        
    df.to_csv(df_name, sep='\t', encoding = 'utf-8')
    print('Save '+ df_name)
    return df
