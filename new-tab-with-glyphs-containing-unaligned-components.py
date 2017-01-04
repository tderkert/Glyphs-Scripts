#MenuTitle: New Tab With Glyphs Containing Unaligned Components
# -*- coding: utf-8 -*-
__doc__="""
New tab with glyphs containing unaligned components (only in current master)
"""

font = Glyphs.font
glyphs = font.glyphs
glyphsString = ''
currentMaster = font.selectedFontMaster

print("Glyphs with unaligned components (" + currentMaster.name + "):")
for glyph in glyphs:
	layer = glyph.layers[currentMaster.id]
	components = layer.components
	isAligned = layer.isAligned

	if not isAligned and len(components):
		print("/" + glyph.name)
		print("")
		glyphsString = glyphsString + "/" + glyph.name


# Open new tab
font.newTab( glyphsString )