import re
import urllib2
from sets import Set

start_link = 'http://precog.iiitd.edu.in/'
urls = Set([start_link])

def findId(source):
    l = re.findall(r'"(http[s]*://\S+)"',source)
    return l

def get_source(url):
    response = urllib2.urlopen(url)
    page_source = response.read()
    return page_source

def search(source, depth):
    if depth==2:
        return
    print source, depth

    try:
        page_source = get_source(source)
        links = Set(findId(page_source))
    except:
        print 'some error encountered'
        return

    global urls
    for link in links:
        if link not in urls:
            urls = urls|Set([link])        

    for link in urls:
        search(link,depth+1)

search(start_link,0)