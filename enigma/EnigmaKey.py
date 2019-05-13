# File: EnigmaKey.py

from pgl import GCompound, GLabel
from gtools import createFilledCircle
from EnigmaConstants import *

class EnigmaKey(GCompound):
	'''
	This class represents a key on the Enigma.
	'''

# Constructor

	def __init__(self, letter):
		'''
		The constructor initalizes the key for a given letter.
		'''
		GCompound.__init__(self)
		button = createFilledCircle(0, 0, KEY_RADIUS, 
			fill = KEY_BGCOLOR, border = KEY_BORDER_COLOR)
		button.setLineWidth(KEY_BORDER)
		key = GLabel(letter)
		key.setFont(KEY_FONT)
		self.key = key
		key.setColor(KEY_UP_COLOR)
		self.add(button)
		self.add(key, -key.getWidth() / 2, KEY_LABEL_DY)

# Methods

	def mousedownAction(self, enigma):
		'''
		Changes the color of the key to indicated it's selected and 
		sends the key presed to the enigma machine.
		'''
		self.key.setColor(KEY_DOWN_COLOR)
		enigma.keyPressed(ALPHABET.find(self.key.getLabel()))


	def mouseupAction(self, enigma):
		'''
		Returns the color to its original state and sends the key 
		released the the enigma machine.
		'''
		self.key.setColor(KEY_UP_COLOR)
		enigma.keyReleased(ALPHABET.find(self.key.getLabel()))


