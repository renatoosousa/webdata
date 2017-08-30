from lxml.html import parse 
from urllib2 import urlopen
from pandas.io.parses import TextParser

def _unpack(row, kind='td'):
	elts = row.findall('.//%s' % kind)
	return [val.text for val in elts]

def parse_options_data(table):
	rows = table.findall('.//tr')
	header = _unpack(rows[0], kind ='th')
	data = [_unpack(r) for r in rows[1:]]
	return TextParser(data, names=header).get_chunk()

if __name__ == '__main__':
	url = 'http://www.ezfshn.com/tides/usa/california/san%20diego'
	parsed = parse(url)

	doc = parsed.getroot()

	links = doc.findall('.//a')

	links_sub_list = links[15:20]
	lnk = links_sub_list[0]

	sample_url = lnk.get('href')

	sample_display_text = lnk.text_content()

	tables = doc.findall('.//table')

	dt = tables[0]

	rows = dt.finall('.//tr')

	headers = _unpack(rows[0], kind = 'th')

	row_vals = _unpack(rows[1], kind = 'td')

	tide_data = parse_options_data(dt)

	print tide_data[:10]
	