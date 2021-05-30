#MenuTitle: Print selected glyphs split by non-width space
# -*- coding: utf-8 -*-
__doc__="""
Print all glyphs in Font View, split by non-width space. 
"""

font = Glyphs.font
glyphs = font.glyphs

nonWidthSpace = u'\u200B'
space = u'\u0020'
textString = ''


for glyph in glyphs:
	if glyph.unicode and glyph.export:
		textString = textString + glyph.string + nonWidthSpace
		
	
print(textString)