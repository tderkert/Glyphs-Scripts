#MenuTitle: New Tab With Pangram from Selected Langauge
# -*- coding: utf-8 -*-
__doc__="""
Select a language in list and open a new tab with a pangram
"""


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
		self.w = Window((900, 500),"New Tab With Pangram", minSize=(250,200), maxSize=(1000,1000))
		self.w.localizedFormCheckBox = CheckBox((20, -45, -10, 30), "Turn on Localized Forms", value=True, callback=self.SavePrefs )
		self.w.list = List((20, 20, -20, -60), pangrams, columnDescriptions=[{"title": "lang", "width": 200}, {"title": "phrase", "width": 400}, {"title": "usesAllLetters", "width": 300}], selectionCallback=self.SavePrefs)
		self.w.button = Button((-200, -45, -20, 30), "New Tab", callback=self.buttonCallback)
		self.w.setDefaultButton( self.w.button )


		# Use defaults if no saved preferences

		if not self.LoadPrefs( ):
			print ("Note: Could not load preferences. Will resort to defaults.")

		self.w.open()


	
	def buttonCallback(self, sender):
		listIndex = self.w.list.getSelection()
		showLocalizedForms = self.w.localizedFormCheckBox.get()

		# Save Prefs
		self.SavePrefs(self)

		for i in listIndex:
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
						if str(iso) in line:
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


	# Persist selection for next time
	def SavePrefs( self, sender ):
		print ("SavePrefs()")
		Glyphs.defaults["com.tderkert.ChoiceOfPangram.listSelection"] =        self.w.list.getSelection()
		Glyphs.defaults["com.tderkert.ChoiceOfPangram.turnOnLocalizedForms"] = self.w.localizedFormCheckBox.get()
		return True
	
	def LoadPrefs( self ):
		try:
			self.w.localizedFormCheckBox.set( Glyphs.defaults["com.tderkert.ChoiceOfPangram.turnOnLocalizedForms"] )
			self.w.list.setSelection(         Glyphs.defaults["com.tderkert.ChoiceOfPangram.listSelection"] )
			return True
		except:
			return False

PangramSelecter()