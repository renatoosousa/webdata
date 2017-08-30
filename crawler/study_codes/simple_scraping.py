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
	return TextParser()