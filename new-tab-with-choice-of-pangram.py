#MenuTitle: New Tab With Pangram from Selected Langauge
'''Select a language in list and open a new tab with a pangram'''


# Glyphs.clearLog()
# Glyphs.showMacroWindow()

from GlyphsApp import *
from vanilla import *
import json
from pprint import pprint

font = Glyphs.font

# LOAD JSON DATA
with open('pangrams.json') as data_file:    
    pangrams = json.load(data_file)

class PangramSelecter(object):
	def __init__(self):
		self.w = Window((700, 400),"New Tab With Pangram", minSize=(250,200), maxSize=(1000,1000))
		self.w.textBox = TextBox((10, 10, -10, 55), "Select Language(s):")
		self.w.checkBox = CheckBox((400, 10, -10, 20), "Turn on Localized Forms", value=True)
		self.w.list = List((10, 40, -10, -40), pangrams, columnDescriptions=[{"title": "lang", "width": 200}, {"title": "phrase"}, {"title": "usesAllLetters", "width": 300}])
		self.w.button = Button((10, -30, -10, 20), "OpenTab", callback=self.buttonCallback)
		self.w.open()
	
	def buttonCallback(self, sender):
		listIndexes = self.w.list.getSelection()
		showLocalizedForms = self.w.checkbox.get()
		for i in listIndexes:
			# Pangram data
			phrase = pangrams[i]["phrase"]
			iso = pangrams[i]["iso"]
			scriptTag = pangrams[i]["scriptTag"]

			# New tab with phrase
			font.newTab( phrase )
				
			# Set script
			if showLocalizedForms:
				langSystems = False # Initial
				if font.featurePrefixes['Languagesystems']:
					langSystems = font.featurePrefixes['Languagesystems'].code

				# Check if feature of setLang exist
				if langSystems:
					code = langSystems.split('\n'); 
					for line in code: 
						if iso in line:
							scriptString = scriptTag + ' ' + iso
							# Turn on 'locl' and turn on script
							font.currentTab.features.append('locl')
							font.currentTab.setValue_forKey_(scriptString, "selectedScript")
							# Update view hack
							font.currentTab.textCursor = 1
							font.currentTab.textCursor = 0

			# Print details in Macro window
			print("---- " + pangrams[i]["lang"] + " ----")
			print( "Phrase: " + pangrams[i]["phrase"] )
			print( "Translation: " + pangrams[i]["translation"] )
			print( "Uses All Letters: " + pangrams[i]["usesAllLetters"] )
		print("------------------")
		# Close
		self.w.close() 


PangramSelecter()