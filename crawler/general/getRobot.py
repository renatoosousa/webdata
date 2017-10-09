import urllib2 

def getRobot(url):
	try:
		DOWNLOAD_URL = url+"/robots.txt"

		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
		req = urllib2.Request(DOWNLOAD_URL, headers=hdr)

		result = urllib2.urlopen(req)
		result_data_set = {"Disallowed":[], "Allowed":[]}

		for line in result:
		    if line.startswith('Allow'):    # this is for allowed url
		        result_data_set["Allowed"].append(line.split(': ')[1].split(' ')[0])    # to neglect the comments or other junk info
		    elif line.startswith('Disallow'):    # this is for disallowed url
		        result_data_set["Disallowed"].append(url+(line.split(': ')[1].split(' ')[0]).replace("\r\n",""))    # to neglect the comments or other junk info

		# print (result_data_set)
		# print result_data_set["Disallowed"]
		return result_data_set["Disallowed"]
	except Exception:
		return []
