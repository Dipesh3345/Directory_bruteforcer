import requests
import argparse


def getUserArguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--url", dest = "url", help = "[*] Please specipy a url or use --help ,for more info")
	parse.add_argument("-f","--file", dest="file" , help ="[*] Please specify a word list , or use --help for more info")
	options = parser.parse_args()
	return options

getUserArguments()
file = open(options.file)
u = options.url

for i in range(397):
	a = file.readline()
	r = requests.get(u+a)
	print(u+a)
	print(r.status_code) 
	


	









