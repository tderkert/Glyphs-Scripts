#MenuTitle: Round Kerning
# encoding: utf-8
from __future__ import division

# by Teddy Derkert
# Based on a Round Kerning by Tim Ahrens

__doc__="""
Round kerning by specified quantization and set minimum value.
"""

MIN_VALUE = 4
QUANTISATION = 2
from GlyphsApp import *
from GlyphsApp import MGOrderedDictionary
import time
import vanilla
font = Glyphs.font

def filterKern():
	print( QUANTISATION )
	kerning = font.kerning
	for master in Font.masters:
		masterDict = kerning[master.id]
		newMasterDict = MGOrderedDictionary.new()
		firstKeys = masterDict.keys()
		for firstKey in firstKeys:
			rightDict = masterDict[firstKey]
			secondKeys = rightDict.keys()
			newRightDict = MGOrderedDictionary.new()
			for secondKey in secondKeys:
				value = rightDict[secondKey]
				# Remove kerning below minimum value
				if abs(value) < MIN_VALUE:
					newRightDict[secondKey] = 0
				else:
					# Quantize according to quantisation value
					value = round(value / QUANTISATION) * QUANTISATION
					newRightDict[secondKey] = value
			if len(newRightDict) > 0:
				newMasterDict[firstKey] = newRightDict
		kerning[master.id] = newMasterDict
	font.kerning = kerning

class RoundKerningUI(object):
	def __init__( self):
		self.w = vanilla.FloatingWindow((260, 108), "Round Kerning", minSize=(260, 108), maxSize=(260, 200))

		# Min value of kerning
		self.w.textMinValue = vanilla.TextBox((15, 14+2, 150, 14), "Min value:", sizeStyle='small')
		self.w.newMinValue = vanilla.EditText((120, 14, -15, 19), MIN_VALUE, sizeStyle='small')
		
		# Quantisation
		self.w.textQuantisation = vanilla.TextBox((15, 38+2, 150, 14), "Quantisation:", sizeStyle='small')
		self.w.newQuantisation = vanilla.EditText((120, 38, -15, 19), QUANTISATION, sizeStyle='small')

		# Callback button
		self.w.runButton = vanilla.Button((15, 72, -15, 20), "Round kerning", sizeStyle='regular', callback=self.ButtonCallback )
		self.w.setDefaultButton( self.w.runButton )


		self.w.open()
		self.w.makeKey()

	def ButtonCallback( self, sender ):
		global MIN_VALUE, QUANTISATION
		# Update values from UI, after converting to Int
		MIN_VALUE = int( self.w.newMinValue.get() )
		QUANTISATION = int( self.w.newQuantisation.get() )

		# Run 
		start = time.time()
		filterKern()
		end = time.time()
		print("time", end - start)

		# Hack tp update preview to show changes
		font.disableUpdateInterface()
		font.enableUpdateInterface()

		# Close UI
		self.w.close()
		return True		




RoundKerningUI()