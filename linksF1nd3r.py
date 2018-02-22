#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''
 Extracts links from an HTML page and display them with friendly way ,this tool could be used for web information gathering ,to get more details about the web
 application.
'''
__author__ = "Ihebski (S0ld1er)"
__copyright__ = "Copyright 2017, Bugs_Bunny Team | Pentesting Tools"
__version__ = "0.5"
__email__ = "ihebbensalem.dev@gmail.com"
__status__ = "Development"
__codename__ = 'linksF1nd3r'
__source__ ="https://github.com/ihebski/angryFuzzer"
__info__ ="LinksF1nd3r"

try: 
	import sys
	import urllib2
	from bs4 import BeautifulSoup
	import re
	import os
	import colorama
	from colorama import Fore, Back, Style 
	from colorama import init
	from urlparse import urlparse
	import time
except Exception as err:
	print "[!] "+str(err)
	sys.exit(0)

LIGHTRED = '\033[91m'
YL = '\033[33m'




def banner():
	print Fore.BLUE+".__  .__        __           ___________.__            .___            "
	print LIGHTRED +"|  | |__| ____ |  | __  _____\_   _____/|__| ____    __| _/___________ "
	print 			"|  | |  |/    \|  |/ / /  ___/|    __)  |  |/    \  / __ |/ __ \_  __ \""
	print 			"|  |_|  |   |  \    <  \___ \ |     \   |  |   |  \/ /_/ \  ___/|  | \/"
	print  		    "|____/__|___|  /__|_ \/____  >\___  /   |__|___|  /\____ |\___  >__|   "
	print Fore.BLUE+ "             \/     \/     \/     \/            \/      \/    \/      "
	print LIGHTRED+ " ==============================================> by S0ld1er \n"
	print Fore.YELLOW+"[ JS ] "+Fore.CYAN+"[ PHP ]"+Fore.MAGENTA+"[ IMG ]"+YL+"[ HTML ]"+Fore.GREEN+"[ Unkown ]\n"

def usage():
	'''
	Show the usage of the app
	'''
	scr = os.path.basename(sys.argv[0])
	banner()
	print Fore.CYAN+"python links.py URL"

def start(argv):
	if len(sys.argv) < 2:
		usage()
		sys.exit()
	url = argv[0]	
	o = urlparse(url)
	if o[0] not in ['http','https', 'ftp']:
		banner()
		print Fore.RED+"[!] Please checkout your URL http://, https:// or ftp://"
		sys.exit(0)		
	banner()	
	report(url)	
		


def serchLinks(url):
	'''
	Search for all the urls with http:// or https:// regx and all the <a href=""> tags
	'''
	website = urllib2.urlopen(url)
	html = website.read()
	soup = BeautifulSoup(html,'lxml')
	#use re.findall to get all the links with http:// or https:// url
	mylinks =[]
	links = re.findall('"((http|ftp)s?://.*?)"', html)
	for x in links:
		mylinks.append(x[0])

	# Find all the href links in <a > tags	
	for link in soup.find_all('a', href=True):
	    mylinks.append(link['href'])
	# Remove the redondant links    
	k = list(dict.fromkeys(mylinks))
	return k	
	
def report(url):
	'''
	Show the final results with the extension of the url
	'''
	js_= 0
	PHP_= 0
	IMG = 0
	Other = 0
	html = 0
	links = serchLinks(url)
	for link in links:
		if 'js' in link:
			print Fore.YELLOW+"[{time}] -[ JS ] - {mylink}".format(mylink=link,time=time.strftime("%H:%M:%S"))
			js_+=1
		elif 'php' in link:
			print Fore.CYAN+"[{time}] -[ PHP ] - {mylink}".format(mylink=link,time=time.strftime("%H:%M:%S"))
			PHP_+=1
		elif 'jpg' in link or 'png' in link or 'jpg' in link:
			print Fore.MAGENTA+"[{time}] -[ IMG ] - {mylink}".format(mylink=link,time=time.strftime("%H:%M:%S"))
			IMG+=1
		elif 'html' in link:
			print YL+"[{time}] -[ HTML ] - {mylink}".format(mylink=link,time=time.strftime("%H:%M:%S"))
			html +=1
		else:
			print Fore.GREEN+"[{time}] - [ ! ] - {mylink}".format(mylink=link,time=time.strftime("%H:%M:%S"))
			Other+=1
	print "================== Report =================="
	print Fore.WHITE+" URL => "+url
	print Fore.WHITE+"[TOTALE] => [ JS = {js} ] - [ PHP = {php} ] - [ IMG = {img} ] - [ HTML = {html} ] - [ Unknown = {unkonwn} ]".format(js=js_,php=PHP_,img=IMG,unkonwn=Other,html=html)
	

if __name__ == "__main__":
	try:
		start(sys.argv[1:])
	except KeyboardInterrupt as err:
		print r+"\n[!] By... :)"+t
		sys.exit(0)

