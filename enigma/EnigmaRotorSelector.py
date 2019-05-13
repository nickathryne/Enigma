# File: EnigmaRotorSelector

from pgl import GCompound, GLabel
from gtools import createFilledRect
from EnigmaConstants import *

# Constants

SELECTOR_WIDTH = ROTOR_WIDTH
SELECTOR_HEIGHT = ROTOR_HEIGHT
SELECTOR_BGCOLOR = ROTOR_BGCOLOR
SELECTOR_COLOR = ROTOR_COLOR
SELECTOR_LABEL_DY = ROTOR_LABEL_DY
SELECTOR_FONT = ROTOR_FONT


class EnigmaRotorSelector(GCompound):
	'''
	This class represents the rotor selectors on the enigma.
	'''

# Constructor

	def __init__(self, rotor):
		''' 
		The constructor initalizes the selector in the standard setting in the
		three rotor model.
		'''
		GCompound.__init__(self)
		self.offset = rotor
		self.rotor = rotor
		button = createFilledRect(-SELECTOR_WIDTH / 2, -SELECTOR_HEIGHT / 2,
			SELECTOR_WIDTH, SELECTOR_HEIGHT, fill = SELECTOR_BGCOLOR,
			border = SELECTOR_COLOR)
		button.setLineWidth(3)
		setting = GLabel(str(self.offset))
		setting.setFont(SELECTOR_FONT)
		setting.setColor(SELECTOR_COLOR)
		self.setting = setting
		self.add(button)
		self.add(setting, -setting.getWidth() / 2, SELECTOR_LABEL_DY)

# Methods

	def clickAction(self, enigma):
		'''
		When a rotor selector is clicked, it will advance the selector 
		and send the new offset to the enigma.
		'''
		if enigma.message == '':
			available_rotors = enigma.getAvailableRotors()
			self.advance(available_rotors)
			enigma.selectionChange(self.rotor, self.offset)

	def advance(self, available_rotors):
		'''
		This advances the selector to the next available rotor number.
		'''
		d = 5
		for i in available_rotors:
			if 0 < i - self.offset < d:
				d = i - self.offset
		if d == 5:
			self.offset = available_rotors[0]
		else:
			self.offset += d
		self.setting.setLabel(str(self.offset))

	def getSetting(self):
		'''
		This returns the current setting for the corresponding rotor.
		'''
		return self.offset

