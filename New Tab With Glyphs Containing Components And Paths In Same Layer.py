#MenuTitle: New Tab With Glyphs Containing Both Components And Paths In Current Master
# -*- coding: utf-8 -*-
__doc__="""
New tab with glyphs containing both components and paths (only in current master)
"""

font = Glyphs.font
glyphs = font.glyphs
glyphsString = ''
currentMaster = font.selectedFontMaster

print("Glyphs with components and paths (" + currentMaster.name + "):")
for glyph in glyphs:
	layer = glyph.layers[currentMaster.id]
	components = layer.components
	paths = layer.paths
	
	if ( len(components) and len(paths) ):
		print(glyph.name)
		glyphsString = glyphsString + "/" + glyph.name


# Open new tab
font.newTab( glyphsString )