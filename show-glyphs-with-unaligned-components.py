#MenuTitle: New tab with glyphs containing unaligned components
'''Open new tab with glyphs containing unaligned components (only in current layer)'''

font = Glyphs.font
glyphs = font.glyphs
glyphsString = ''

print("Glyphs with unaligned components:")
for glyph in glyphs:
	layer = glyph.layers[0]
	components = layer.components
	hasUnalignedComponent = False
	
	for component in components:
		if component.automaticAlignment == False:
			glyphsString = glyphsString + "/" + glyph.name
			print("/" + glyph.name)
			break


# Open new tab
font.newTab( glyphsString )