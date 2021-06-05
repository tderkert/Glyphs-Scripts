#MenuTitle: New Tab With Unicode Glyphs Separated by A Glyph
# -*- coding: utf-8 -*-
__doc__="""
New Tab With Unicode Glyphs Separated by A Glyph
"""

font = Glyphs.font
glyphs = font.glyphs

nonWidthSpace = u'\u200B'
space = u'\u0020'







########################

class PrintUnicodeGlyphsWithSeparator(object):

	def __init__( self):
		self.w = vanilla.FloatingWindow((360, 60), "New Tab With Unicode Glyphs Separated by A Glyph", minSize=(460, 120), maxSize=(460, 120))


		# New name
		self.w.labelGlyphName = vanilla.TextBox((15, 16+2, 150, 14), "Glyph name:", sizeStyle='small')
		self.w.separatorGlyphName = vanilla.EditText((90, 16, -90, 19), "thinspace", sizeStyle='small', callback=self.SavePrefs)


		# Callback button
		self.w.printButton = vanilla.Button((-80, 16, -15, 17), "Create", sizeStyle='regular', callback=self.ButtonCallback )
		self.w.setDefaultButton( self.w.printButton )

		# Use defaults if no saved preferences
		if not self.LoadPrefs( ):
			print ("Note: Could not load preferences. Will resort to defaults.")

		self.w.open()
		self.w.makeKey()

	def ButtonCallback( self, sender ):
		glyphName = self.w.separatorGlyphName.get()
		if font.glyphs[glyphName]:
			textString = ''
			for glyph in glyphs:
				if glyph.unicode and glyph.export:
					textString = textString + glyph.string + "/" + glyphName + " "
					
			font.newTab(textString)
			self.w.close()
		else:
			print('Error: there is no "' + glyphName + '" in the font.')




	def SavePrefs( self, sender ):
		Glyphs.defaults["com.tderkert.PrintUnicodeGlyphsWithSeparator.separatorGlyph"] = self.w.separatorGlyphName.get()
		return True
	
	def LoadPrefs( self ):
		try:
			self.w.separatorGlyphName.set( Glyphs.defaults["com.tderkert.PrintUnicodeGlyphsWithSeparator.separatorGlyph"] )
			return True
		except:
			return False

PrintUnicodeGlyphsWithSeparator()

