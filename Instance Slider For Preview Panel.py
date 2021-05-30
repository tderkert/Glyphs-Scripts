#MenuTitle: Instance Slider For Preview Panel
# encoding: utf-8
# by Teddy Derkert

__doc__="""
Use a slider to quickly switch between instances in Preview Panel. Use the combobox to quickly switch between instances using up and down arrow keys.
"""

from GlyphsApp import *
import vanilla
font = Glyphs.font

# Initial costants
instances = font.instances
totalInstances = len( instances)
previewInstances = font.currentTab.previewInstances
savedPreviewInstances = previewInstances

# Set an inital instance if none is set
if previewInstances in ('live', 'all'):
	previewInstances = instances[0]
	
# Create list instances in string format for ComboBox
instanceListNames = []
for i in instances:
	instanceListNames.append(i.name)





def interpolateNumbers(factor, a, b):
	return a + factor * (b - a)


def factorToInstance(factor):
	instanceIndex = int( interpolateNumbers(factor,0,totalInstances-1) )
	instance = font.instances[instanceIndex]
	return instance

	
def instanceToPercent(instance):
	index = indexOfInstance(instance)
	ratio = (index+1) / (totalInstances - 1)
	return ratio * 100

def nameToInstance(string):
	for instance in instances:
		if instance.name == string:
			return instance

def indexOfInstance(instance):
	for index, i in enumerate(instances):
		if i is instance:
			return index-1

# Hack to avoid crash of Glyphs. Not sure why.
def updateSlider(slider,value):
	slider.set(value)

def updateUI(instance, self, sender):
	# Update Preview Panel
	font.currentTab.previewInstances = instance

	# Update Script UI	
	if sender is self.w.slider:
		self.w.comboBox.set(instance.name)
	elif sender is self.w.comboBox:
		updateSlider(self.w.slider, instanceToPercent(instance))	
	






# UI Class
class UpdateInstanceInPreviewPanel():
	def __init__( self):
		self.w = vanilla.FloatingWindow((230, 100), 
								"Instance In Preview Panel Slider", 
								minSize=(230, 108), 
								maxSize=(260, 200))

		self.w.slider = vanilla.Slider((12, 10, -12, 23),
								tickMarkCount=totalInstances,
								value=instanceToPercent(previewInstances),
								stopOnTickMarks=1,
								sizeStyle="small",
								callback=self.SliderCallback)

		self.w.comboBox = vanilla.ComboBox((12, 50, -12, 21),
								items=instanceListNames,
								callback=self.ComboBoxCallback)

		# Set initial comboBox Value
		self.w.comboBox.set(previewInstances.name)

		# Open and focus on window
		self.w.open()
		self.w.makeKey()

		# Hack to update Preview Panel
		updateUI(previewInstances,self,self.w.slider)

		# Callback when window is closed
		self.w.bind("close", self.CloseCallback)


	def SliderCallback( self, sender ):
		# Get instance from slider value
		sliderFactor = sender.get() / 100
		newInstance = factorToInstance(sliderFactor)
		# Update UI
		updateUI(newInstance, self, sender)

	def ComboBoxCallback( self, sender ):
		name = sender.get()
		newInstance = nameToInstance(name)
		# Update UI
		updateUI(newInstance, self, sender)

	def CloseCallback(self, sender):
		font.currentTab.previewInstances = savedPreviewInstances


# Run UI Class
UpdateInstanceInPreviewPanel()

