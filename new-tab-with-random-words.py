#MenuTitle: New Tab With Random Words
'''New tab with 10 random words from 'http://www.setgetgo.com/randomword' API. (Required internet connection)'''

import urllib2

font = Glyphs.font
url = "http://www.setgetgo.com/randomword/get.php"
length = 10
tabString = ""

def getPage(url):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	return response.read()

for i in range(length):
	tabString = tabString + getPage(url) + '\n'

if isinstance(tabString, basestring):
	font.newTab(tabString)