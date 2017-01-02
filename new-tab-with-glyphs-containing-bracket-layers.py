#MenuTitle: New Tab With All Glyphs Containing Bracket Layers
'''New tab with glyphs containing bracket layers'''

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