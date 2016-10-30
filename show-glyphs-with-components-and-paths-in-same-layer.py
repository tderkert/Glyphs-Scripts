#MenuTitle: New tab with glyphs containing both components and paths in current master
'''Open new tab with glyphs containing both components and paths (only in current master)'''

font = Glyphs.font
glyphs = font.glyphs
glyphsString = ''
currentMaster = font.selectedFontMaster

print("Glyphs with components and paths (" + currentLayer.name + "):")
for glyph in glyphs:
	layer = glyph.layers[currentMaster.id]
	components = layer.components
	paths = layer.paths
	
	if ( len(components) and len(paths) ):
		print(glyph.name)
		glyphsString = glyphsString + "/" + glyph.name


# Open new tab
font.newTab( glyphsString )