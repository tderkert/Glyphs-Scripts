#MenuTitle: New Tab With All Glyphs Containing Bracket Layers
'''New tab with glyphs containing bracket layers'''

font = Glyphs.font
glyphs = font.glyphs

brackets = ['[', ']']
glyphsString = ''

for glyph in glyphs:
	for layer in glyph.layers:
		for bracket in brackets:
			if bracket in layer.name:
				glyphsString += glyph.string + ' '
				

font.newTab(glyphsString)			
print('Glyphs containing bracket layers: ' + glyphsString)