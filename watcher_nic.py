#!/usr/bin/python
import requests,os
import datetime

# Download CVE from NIC.CL
def download_cve(url):
	# Kudos: http://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
	CUR_DIR = os.path.dirname(os.path.abspath(__file__))	
	local_filename = CUR_DIR + "/dominios_{0}.cvs".format(datetime.datetime.today().strftime("%H%M%S_%d%m%Y"))
	
	# NOTE the stream=True parameter
	r = requests.get(url, stream=True)
	with open(local_filename, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024): 
			if chunk: # filter out keep-alive new chunks
				f.write(chunk)
				#f.flush() commented by recommendation from J.F.Sebastian
	return local_filename

def watch(time_lapse = 0):
	# Download CVE
	# Add more if you like (I don't think there will be)
	dataurl = {
		"url_hora"	:	"http://www.nic.cl/registry/Ultimos.do?t=1h&f=csv",
		"url_dia"	:	"http://www.nic.cl/registry/Ultimos.do?t=1d&f=csv",
		"url_semana":	"http://www.nic.cl/registry/Ultimos.do?t=1w&f=csv",
		"url_mes"	:	"http://www.nic.cl/registry/Ultimos.do?t=1m&f=csv"
	}

	# Select Mode
	url = ""
	if time_lapse == 0:
		url = dataurl['url_hora']
	elif time_lapse == 1:
		url = dataurl['url_dia']
	elif time_lapse == 2:
		url = dataurl['url_semana']
	elif time_lapse == 3:
		url = dataurl['url_mes']

	if url is not "":
		cve = download_cve(url)
		cvedata = open(cve)
		print cve
#		for line in cvedata:
#			print line

if __name__ == "__main__":
	# Choose 0 for hourly
	#		 1 for daily
	#		 2 for weekly
	#		 3 for montly
	watch(0)
