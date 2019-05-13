# File: EngimaRotor.py

from pgl import GCompound, GLabel
from gtools import createFilledRect
from EnigmaConstants import *

# Constants 

ROTOR_PERMUTATIONS = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    "BDFHJLCPRTXVZNYEIWGAKMUSQO",
    "QAZXSWEDCVFRTGBNHYUJMKILOP",
    "QMWNEBRVTCYUXIZOPALSKDJFGH",
    "MNBVCXZLKJHGFDSAQWERTYUIOP"]


class EnigmaRotor(GCompound):
	''' 
	This class represents a rotor on the enigma.
	'''

# Constructor 
	def __init__(self, permuation):
		'''
		The constructor initalizes the rotor in the base setting.
		'''
		GCompound.__init__(self)
		self.permuation = permuation
		self.inversion = invertKey(permuation)
		self.offset = 0
		rotor = createFilledRect(-ROTOR_WIDTH / 2, -ROTOR_HEIGHT / 2,
			ROTOR_WIDTH, ROTOR_HEIGHT, fill = ROTOR_BGCOLOR)
		setting = GLabel(ALPHABET[self.offset])
		setting.setColor(ROTOR_COLOR)
		setting.setFont(ROTOR_FONT)
		self.setting = setting
		self.add(rotor)
		self.add(setting, -setting.getWidth() / 2, ROTOR_LABEL_DY)

# Methods

	def clickAction(self, enigma):
		'''
		When a rotor is clicked advance is called.
		'''
		self.advance()

	def advance(self):
		'''
		advace advaces the rotor to the next setting.
		'''
		self.offset = (self.offset + 1) % 26
		self.setting.setLabel(ALPHABET[self.offset])
		if self.offset == 0:
			return True
		else:
			return False

	def translate(self, index):
		'''
		translate applies the permuation of the rotor in its current setting.
		'''
		return applyPermutation(index, self.permuation, self.offset)

	def inverseTranslate(self, index):
		''' 
		inverseTranslate applies the inverse permuation of the rotor in its 
		current setting.
		'''
		return applyPermutation(index, self.inversion, self.offset)

	def changePermutation(self, offset):
		'''
		Sets the permuation and inversion to the new setting from the selector.
		'''
		self.permuation = ROTOR_PERMUTATIONS[offset]
		self.inversion = invertKey(self.permuation)

	def reset(self):
		self.offset = 0
		self.setting.setLabel(ALPHABET[self.offset])


def applyPermutation(index, permuation, offset):
	'''
	applyPermutation returns the index of the letter after applying the 
	permuation.
	'''
	index = (index + offset) % 26
	return (ALPHABET.find(permuation[index]) - offset) % 26

def invertKey(permuation):
	'''
	inverKey inverts the permuation.
	'''
	inversion = ''
	for letter in ALPHABET:
		i = permuation.find(letter)
		inversion += ALPHABET[i]
	return inversion



