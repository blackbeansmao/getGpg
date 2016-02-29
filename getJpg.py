#!/usr/bin/env python
#coding=utf-8
#python2

import urllib
from sys import argv
import re

script, url = argv

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

html = getHtml(url)
#print html

def getImage(html):
	reg = r'src="(.+?\.jpg)" pic_ext'
	imgre = re.compile(reg)
	imglist = re.findall(imgre, html)
	
	x = 0
	for imgurl in imglist:
		urllib.urlretrieve(imgurl, '%s.jpg' % x)
		x += 1
getImage(html)
