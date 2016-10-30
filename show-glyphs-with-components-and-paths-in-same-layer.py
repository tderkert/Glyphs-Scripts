#MenuTitle: New tab with glyphs containing both components and paths in same layer
'''Open new tab with glyphs containing both components and paths in same layer (only in current layer)'''

font = Glyphs.font
glyphs = font.glyphs
glyphsString = ''

print("Glyphs with components and paths in same layer:")
for glyph in glyphs:
	layer = glyph.layers[0]
	components = layer.components
	paths = layer.paths
	
	if ( len(components) and len(paths) ):
		print(glyph.name)
		glyphsString = glyphsString + "/" + glyph.name


font.newTab( glyphsString )