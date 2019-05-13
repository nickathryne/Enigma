# File: EnigmaLamp.py

from pgl import GCompound, GLabel
from gtools import createFilledCircle
from EnigmaConstants import *

class EnigmaLamp(GCompound):
	'''
	This class represents a lamp on the enigma.
	'''

# Constructor 
	
	def __init__(self, letter):
		''' 
		The constructor creates a lamp for a given letter.
		'''
		GCompound.__init__(self)
		self.letter = letter
		lamp = createFilledCircle(0, 0, LAMP_RADIUS, 
			fill = LAMP_BGCOLOR, border = LAMP_BORDER_COLOR)
		lamp = GLabel(letter)
		lamp.setFont(LAMP_FONT)
		self.lamp = lamp
		self.state = False
		lamp.setColor(LAMP_OFF_COLOR)
		self.add(lamp)
		self.add(lamp, -lamp.getWidth() / 2, LAMP_LABEL_DY)

# Methods

	def setState(self, state):
		'''
		Sets the state of the lamp to the given input.
		'''
		self.state = state
		if state:
			self.lamp.setColor(LAMP_ON_COLOR)
		else:
			self.lamp.setColor(LAMP_OFF_COLOR)

	def getState(self):
		'''
		Returns the state of the lamp.
		'''
		return self.state

	def getKey(self):
		'''
		returns the letter that the lamp represents.
		'''
		return self.letter

		