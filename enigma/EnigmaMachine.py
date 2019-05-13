# File: EnigmaMachine.py

"""
This module is the file for the EnigmaMachine class.
"""

from pgl import GImage
from EnigmaConstants import *
from EnigmaKey import EnigmaKey
from EnigmaLamp import EnigmaLamp
from EnigmaRotor import EnigmaRotor, applyPermutation
from EnigmaReturn import EnigmaReturn
from EnigmaRotorSelector import EnigmaRotorSelector

# Constants 
SELECTOR_LOCATIONS = [
    (240, 190),
    (325, 190),
    (408, 190)
]

ROTOR_PERMUTATIONS = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ", # Standard permutation for slow rotor
    "AJDKSIRUXBLHWTMCQGZNPYFVOE", # Standard permutation for medium rotor
    "BDFHJLCPRTXVZNYEIWGAKMUSQO", # Standard permutation for fast rotor
    "CWMFJORDBANKGLYPHSVEXTQUIZ", # alternative permutations
    "SPHINXOFBLACKQURTZJDGEMYVW"  # (not random -- bad cryptography)
]

# Class: EnigmaMachine

class EnigmaMachine():
    """
    This class is responsible for storing the data needed to simulate
    the Enigma machine.
    """

    def __init__(self, gw):
        """
        The constructor for the EnigmaMachine class is responsible for
        initializing the graphics window along with the state variables
        that keep track of the machine's operation.
        """
        enigmaImage = GImage("images/EnigmaTopView.png")
        gw.add(enigmaImage)
        self.gw = gw
        for letter in ALPHABET:
            i = ALPHABET.find(letter)
            key = EnigmaKey(letter)
            lamp = EnigmaLamp(letter)
            gw.add(key, KEY_LOCATIONS[i][0], KEY_LOCATIONS[i][1])
            gw.add(lamp, LAMP_LOCATIONS[i][0], LAMP_LOCATIONS[i][1])
        for i in range(3):
            selector = EnigmaRotorSelector(i)
            gw.add(selector, SELECTOR_LOCATIONS[i][0], SELECTOR_LOCATIONS[i][1])
            rotor = EnigmaRotor(ROTOR_PERMUTATIONS[i])
            gw.add(rotor, ROTOR_LOCATIONS[i][0], ROTOR_LOCATIONS[i][1])
        gw.add(EnigmaReturn(), 98, 95)
        self.message = ''


# Methods

    def keyPressed(self, index):
        '''
        keyPressed advances the rotors when necessary, sends the key through
        the permutations, lights up the apporpriate lamp, and stores the 
        coded key in message.
        '''
        fast_rotor = self.gw.getElementAt(ROTOR_LOCATIONS[2][0], 
            ROTOR_LOCATIONS[2][1])
        fast = fast_rotor.advance()
        index = fast_rotor.translate(index)
        medium_rotor = self.gw.getElementAt(ROTOR_LOCATIONS[1][0], 
            ROTOR_LOCATIONS[1][1])
        if fast:
            med = medium_rotor.advance()
        else:
            med = False
        index = medium_rotor.translate(index)
        slow_rotor = self.gw.getElementAt(ROTOR_LOCATIONS[0][0], 
            ROTOR_LOCATIONS[0][1])
        if med:
            slow_rotor.advance()
        index = slow_rotor.translate(index)
        index = applyPermutation(index, REFLECTOR_PERMUTATION, 0)
        for i in range(3):
            rotor = self.gw.getElementAt(ROTOR_LOCATIONS[i][0], 
                ROTOR_LOCATIONS[i][1])
            index = rotor.inverseTranslate(index)
        lamp = self.gw.getElementAt(LAMP_LOCATIONS[index][0], 
            LAMP_LOCATIONS[index][1])
        lamp.setState(True)
        self.message += lamp.getKey()
    
    def keyReleased(self, index):
        '''
        keyReleased turns off the apporpriate lamp light.
        '''
        for i in range(3)[::-1]:
            rotor = self.gw.getElementAt(ROTOR_LOCATIONS[i][0], 
                ROTOR_LOCATIONS[i][1])
            index = rotor.translate(index)
        index = applyPermutation(index, REFLECTOR_PERMUTATION, 0)
        for i in range(3):
            rotor = self.gw.getElementAt(ROTOR_LOCATIONS[i][0], 
                ROTOR_LOCATIONS[i][1])
            index = rotor.inverseTranslate(index)
        lamp = self.gw.getElementAt(LAMP_LOCATIONS[index][0], 
            LAMP_LOCATIONS[index][1])
        lamp.setState(False)    

    def returnMessage(self):
        '''
        returnMessage prints the current message in the terminal and 
        resets the message variable.
        '''
        print(self.message)
        self.message = ''

    def selectionChange(self, rotor, offset):
        '''
        This changes the permutation of the rotor to the permutation 
        indicated by the selector.
        '''
        rotor = self.gw.getElementAt(ROTOR_LOCATIONS[rotor][0], 
            ROTOR_LOCATIONS[rotor][1])
        rotor.changePermutation(offset)
        rotor.reset()

    def getAvailableRotors(self):
        '''
        returns the rotor settings not currently in use.
        '''
        available_rotors = [0, 1, 2, 3, 4]
        for x,y in SELECTOR_LOCATIONS:
            selector = self.gw.getElementAt(x, y)
            available_rotors.remove(selector.getSetting())
        return available_rotors

        
        