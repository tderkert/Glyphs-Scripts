#MenuTitle: Sync All Bracket Layer Metrics With Parent Layer
'''Copies metrics from master layer to its associated bracket layers'''

font = Glyphs.font
glyphs = font.glyphs
masters = font.masters
brackets = ('[',']')

for glyph in glyphs:
	for layer in glyph.layers:
		for bracket in brackets:
			if bracket in layer.name:
				# Parent master layer
				pMaster = masters[layer.associatedMasterId]
				pMasterLayer = glyph.layers[pMaster.id]
				
				# Copy metric from parent master layer
				layer.LSB = pMasterLayer.LSB
				layer.RSB = pMasterLayer.RSB	