#MenuTitle: Create copy of a master layer with new name
# -*- coding: utf-8 -*-
__doc__="""
Select a master to create a duplicate layer with new name
"""


# from GlyphsApp import *
import vanilla

font = Glyphs.font



class CopyMasterLayer(object):

	def __init__( self):
		self.w = vanilla.FloatingWindow((460, 120), "Create copy of a master layer with new name", minSize=(460, 120), maxSize=(460, 120))

		# Master
		self.w.textReplace = vanilla.TextBox((15, 12+2, 65, 14), "Master:", sizeStyle='small')
		self.w.masterName = vanilla.PopUpButton((120, 12, -120, 17), self.GetMasterNames(), sizeStyle='small')

		# New name
		self.w.textName = vanilla.TextBox((15, 40+2, 150, 14), "New layer name:", sizeStyle='small')
		self.w.newLayerName = vanilla.EditText((120, 40, -120, 19), "Intermediate {100}", sizeStyle='small', callback=self.SavePrefs)

		# Delete all extra layers option
		self.w.deleteExtraLayers = vanilla.CheckBox((120, 68, -120, 19), "Delete all other layers", value=False, sizeStyle='small', callback=self.SavePrefs )

		# Callback button
		self.w.createButton = vanilla.Button((-80, 68, -15, 17), "Create", sizeStyle='small', callback=self.ButtonCallback )
		self.w.setDefaultButton( self.w.createButton )

		# Use defaults if no saved preferences
		if not self.LoadPrefs( ):
			print "Note: Could not load preferences. Will resort to defaults."

		self.w.open()

	def ButtonCallback( self, sender ):
		# All selected glyphs
		selectedGlyphs = [ l.parent for l in Glyphs.font.selectedLayers ]

		# Variables
		newName = self.w.newLayerName.get()
		masterName = str( self.w.masterName.getItems()[self.w.masterName.get()] )
		deleteLayers = self.w.deleteExtraLayers.get()
		
		# Delete extra leyers
		if deleteLayers:
			self.DeleteExtraLayers()
			print "Extra layers deleted"

		# Create new layers
		for glyph in selectedGlyphs:
			for layer in glyph.layers:
				if layer.name == masterName:
					print layer.name
					newLayer = layer.copy()
					newLayer.name = newName
					glyph.layers.append(newLayer)

		# Update preview to show changes in interpolated instances
		font.disableUpdateInterface()
		font.enableUpdateInterface()
		return True
	
	def GetMasterNames( self ):
		myMasterList = set()
		allMasters = font.masters
		for master in allMasters:
			myMasterList.add( master.name )
		
		return sorted( list( myMasterList ))
	
	def DeleteExtraLayers( self ):
		Layers = Glyphs.font.selectedLayers
		for Layer in Layers:
			Glyph = Layer.parent
			NewLayers = {}
			for m in Glyphs.font.masters:
				NewLayers[m.id] = Glyph.layers[m.id]
			Glyph.setLayers_(NewLayers)


	def SavePrefs( self, sender ):
		Glyphs.defaults["com.tderkert.CopyMasterLayer.newLayerName"] = self.w.newLayerName.get()
		Glyphs.defaults["com.tderkert.CopyMasterLayer.deleteExtraLayers"] = self.w.deleteExtraLayers.get()
		return True
	
	def LoadPrefs( self ):
		try:
			self.w.newLayerName.set( Glyphs.defaults["com.tderkert.CopyMasterLayer.newLayerName"] )
			self.w.deleteExtraLayers.set( Glyphs.defaults["com.tderkert.CopyMasterLayer.deleteExtraLayers"] )
			return True
		except:
			return False

CopyMasterLayer()

