#MenuTitle: New Tab With Random Words
# -*- coding: utf-8 -*-
__doc__="""
New tab with 10 random words from 'http://www.wordnik.com' API. (internet connection required)
"""

import urllib2
import json

font = Glyphs.font
tabString = ""
apiUrl = "http://api.wordnik.com:80/v4/words.json/randomWords?hasDictionaryDef=true&includePartOfSpeech=noun,adjective,verb,adverb,pronoun,prepostition,abbreviation,auxiliary-verb,conjunction,proper-noun&minCorpusCount=4&maxCorpusCount=-1&minDictionaryCount=10&maxDictionaryCount=-1&minLength=5&maxLength=-1&limit=10&api_key=3191606ee718b5a4702020562100443d08ef308204146b103"

# Get words from url
def getWords(url):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	return json.loads(response.read())

# Word list
wordList = getWords(apiUrl)

# Create string of words
for word in wordList:
	tabString = tabString + word["word"] + "\n"

# Open tab with words
font.newTab(tabString)
