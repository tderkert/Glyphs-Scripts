#MenuTitle: New Tab with kerning pairs for F,T,V,W,Y to selected glyphs
'''Useful for making kerning exceptions for tall diacritical characters'''

font = Glyphs.font
selectedGlyphs = font.selection


masterLetters = "FTVWY"
sideLetters = selectedGlyphs
prepend = "HHOH"
append = "nnoi"
finalString = ""

for mLetter in masterLetters:
	for sLetter in sideLetters:
		sLetterString = '/'+sLetter.name+' '

		newLine = prepend + mLetter + sLetterString + append
		finalString += newLine+'\n'

font.newTab(finalString)
font.currentTab.textCursor(0)
print(finalString)