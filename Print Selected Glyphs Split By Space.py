#MenuTitle: Print glyphs split by space
# -*- coding: utf-8 -*-
__doc__="""
Print selected glyphs split by non-width space. 
"""

font = Glyphs.font
glyphs = font.glyphs

nonWidthSpace = u'\u200B'
space = u'\u0020'
textString = ''


for glyph in glyphs:
	if glyph.selected:
		if glyph.unicode and glyph.export:
			textString = textString + glyph.string + space
		
	
print(textString)