#MenuTitle: Print An Array Of All Unicode Glyphs In String Format
# -*- coding: utf-8 -*-
__doc__="""
Generate an array of all unicode glyphs in string format -> ["a", "b", "c"]. Print in Macro console.
"""

font = Glyphs.font
glyphs = font.glyphs

listString = '['

for glyph in glyphs:
	if glyph.unicode:
		listString = listString + '"' + glyph.string + '",'
		
	
listString = listString + ']'
print(listString)