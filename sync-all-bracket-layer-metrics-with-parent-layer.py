#MenuTitle: Sync All Bracket Layer Metrics With Parent Layer
# -*- coding: utf-8 -*-
__doc__="""
Copies metrics from master layer to its associated bracket layers
"""

font = Glyphs.font
glyphs = font.glyphs
brackets = ('[',']')

print "Copy metrics to bracket Layers"
for glyph in glyphs:
	for layer in glyph.layers:
		for bracket in brackets:
			if bracket in layer.name:
				# Parent master layer
				pMasterLayer = glyph.layers[layer.associatedMasterId]
				
				# Copy metrics from parent master layer
				layer.LSB = pMasterLayer.LSB
				layer.RSB = pMasterLayer.RSB

				# Log changes
				print glyph.name + ':', pMasterLayer.name, '->' ,layer.name

				# Stop checking for brackets
				break