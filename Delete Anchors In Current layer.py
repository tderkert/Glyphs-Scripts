#MenuTitle: Delete Anchors In Current Layer
# -*- coding: utf-8 -*-

__doc__="""
Delete all anchors in current layer, in selected glyphs.
"""


import GlyphsApp

Font = Glyphs.font
selectedLayers = Font.selectedLayers

print ("Deleting anchors in:")

for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	print ("-- %s" % thisGlyph.name)
	thisGlyph.beginUndo()	
	thisLayer.setAnchors_( None )
	thisGlyph.endUndo()