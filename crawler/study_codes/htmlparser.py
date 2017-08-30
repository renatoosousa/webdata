import HTMLParser
import urllib

urlText = []

class parseText(HTMLParser.HTMLParser):
	def handle_data(self, data):
		if data != '\n':
			urlText.append(data)

lParser = parseText()

thisurl = "http://www-rohan.sdsu.edu/~gawron/index.html"

lParser.feed(urllib.urlopen(thisurl).read())
lParser.close()
for item in urlText:
	print item