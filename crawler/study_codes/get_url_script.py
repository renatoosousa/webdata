# Opens communication link with a URL. The link can then be used to download the raw content of the web site

import urllib 

thisurl = "http://www-rohan.sdsu.edu/~gawron/index.html"
handle = urlli.urlopen(thisurl)

# Downloading an entire web page and extracting information from it.
html_gunk = handle.read()

html_gunk[:150]