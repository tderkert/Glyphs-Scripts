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
		self.w = vanilla.FloatingWindow((400, 80), "Create copy of a master layer with new name", minSize=(400, 180), maxSize=(500, 80), autosaveName="com.tderkert.CopyMasterLayer.mainwindow" )

		# Master
		self.w.textReplace = vanilla.TextBox((15, 12+2, 65, 14), "Master:", sizeStyle='small')
		self.w.masterName = vanilla.PopUpButton((120, 12, -120, 17), self.GetMasterNames(), sizeStyle='small')

		# New name
		self.w.textName = vanilla.TextBox((15, 40+2, 150, 14), "New layer name:", sizeStyle='small')
		self.w.newLayerName = vanilla.EditText((120, 40, -120, 19), "Intermediate {100}", sizeStyle='small', callback=self.SavePrefs)

		# Callback button
		self.w.createButton = vanilla.Button((-80, 12+2, -15, 17), "Create", sizeStyle='small', callback=self.ButtonCallback )
		self.w.setDefaultButton( self.w.createButton )

		# Use defaults if no saved preferences
		if not self.LoadPrefs( ):
			print "Note: Could not load preferences. Will resort to defaults."

		self.w.open()

	def ButtonCallback( self, sender ):
	
		selectedGlyphs = [ l.parent for l in Glyphs.font.selectedLayers ]

		
		newName = self.w.newLayerName.get()
		masterName = str( self.w.masterName.getItems()[self.w.masterName.get()] )
		
		for glyph in selectedGlyphs:
			for layer in glyph.layers:
				if layer.name == masterName:
					print layer.name
					newLayer = layer.copy()
					newLayer.name = newName
					glyph.layers.append(newLayer)

		# newLayer = font.glyphs['a'].layers[0].copy()
		# newLayer.name = 'Copy of layer'

		return True
	
	def GetMasterNames( self):
		myMasterList = set()
		allMasters = font.masters
		for master in allMasters:
			myMasterList.add( master.name )
		
		# myComponentList.sort( key=len, reverse=False )
		return sorted( list( myMasterList ))
	
	def SetComponentNames( self, sender ):
		myComponentList = self.GetMasterNames()
		self.w.componentName.setItems( myComponentList )
		return True
	
	
	def SavePrefs( self, sender ):
		Glyphs.defaults["com.tderkert.CopyMasterLayer.newLayerName"] = self.w.newLayerName.get()
		return True
	
	def LoadPrefs( self ):
		try:
			self.w.newLayerName.set( Glyphs.defaults["com.tderkert.CopyMasterLayer.newLayerName"] )
			return True
		except:
			return False

CopyMasterLayer()