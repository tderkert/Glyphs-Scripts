#MenuTitle: New Tab With All Glyphs Containing Bracket Layers (Glyphs 2)
# -*- coding: utf-8 -*-
__doc__="""
New tab with glyphs containing bracket layers (Glyphs 2)
"""

font = Glyphs.font
glyphs = font.glyphs

brackets = ['[', ']']
glyphsString = ''

for glyph in glyphs:
	bracketFound = False
	for layer in glyph.layers:
		for bracket in brackets:
			if bracket in layer.name and not bracketFound:
				glyphsString += '/'+glyph.name + ' '
				bracketFound = True
		if bracketFound:
			break


				

font.newTab(glyphsString)			
print('Glyphs containing bracket layers: ' + glyphsString)