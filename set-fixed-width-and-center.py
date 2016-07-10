#MenuTitle: Fixed Width and Center Selected Glyphs
'''Set fixed width and center selected glyphs. Proceed with caution!'''

thisFont = Glyphs.font # frontmost font
selectedGlyphs = thisFont.selection

def decomposeAllComponents():
	print('decomposAllComponents()')
	for g in selectedGlyphs:
		cLayer = g.layers[0]
		cLayer.decomposeComponents()
			
def setFixedWidth(width):
	print('setFixedWidth')
	for g in selectedGlyphs:
		cLayer = g.layers[0]
		cComponents = cLayer.components

		cLayer.setLeftMetricsKeyUI_(None)
		cLayer.setRightMetricsKeyUI_(None)
		cLayer.LSB = 0
		cLayer.RSB = 0
		cLayer.width = width
		cLayer.RSB = cLayer.RSB/2
		cLayer.LSB = cLayer.RSB	
		cLayer.width = width


decomposeAllComponents()

setFixedWidth(1000)