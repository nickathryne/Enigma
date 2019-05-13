# File: EnigmaReturn.py

from pgl import GCompound, GLabel
from gtools import createFilledRect
from EnigmaConstants import *

# Constants

RETURN_WIDTH = ROTOR_WIDTH * 5
RETURN_HEIGHT = ROTOR_HEIGHT * 2
RETURN_BGCOLOR = LAMP_BGCOLOR
RETURN_BORDER_COLOR = LAMP_BORDER_COLOR
RETURN_BORDER = KEY_BORDER
RETURN_FONT = LAMP_FONT
RETURN_LABEL_DY = ROTOR_LABEL_DY
RETURN_COLOR = LAMP_OFF_COLOR
RETURN_LOCATION = (98, 95)


class EnigmaReturn(GCompound):
	'''
	This class represents the return key on the enigma.
	'''

# Constructor

	def __init__(self):
		'''
		The constructor creates a return button on the enigma.
		'''
		GCompound.__init__(self)
		button = createFilledRect(-RETURN_WIDTH / 2, -RETURN_HEIGHT / 2,
			RETURN_WIDTH, RETURN_HEIGHT, fill = RETURN_BGCOLOR, 
			border = RETURN_BORDER_COLOR)
		button.setLineWidth(RETURN_BORDER)
		label = GLabel('RETURN')
		label.setFont(RETURN_FONT)
		label.setColor(RETURN_COLOR)
		self.add(button)
		self.add(label, -label.getWidth() / 2, RETURN_LABEL_DY)
		
# Methods

	def clickAction(self, enigma):
		'''
		Clicking on the return button calls returnMessage on enigma.
		'''
		enigma.returnMessage()

