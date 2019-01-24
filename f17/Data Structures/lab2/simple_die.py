"""
File: simple_die.py

This module defines a simple 6-sided Die class.
"""

from random import randint

class Die(object):
    """This class represents a six-sided die."""

    def __init__(self):
        """The initial face of the die.
           Precondition: none
           Postcondition: Creates a Die with an initial random roll between 1 and 6 inclusive
           Raises: no exception raised"""
        self._currentRoll = randint(1, 6)

    def roll(self):
        """Resets the die's value to a random number between 1 and 6.
           Precondition: none
           Postcondition: the Die was rerolled and has a random roll between 1 and 6 inclusive
           Raises: no exception raised"""
        self._currentRoll = randint(1, 6)

    def getRoll(self):
        """Returns the face value of the die.
           Precondition: none
           Postcondition: the current roll was returned
           Raises: no exception raised"""
        return self._currentRoll

    def __str__(self):
        """Returns the string representation of the die.
           Precondition:  none
           Postcondition:  the string of the current roll was returned
           Raises: no exception raised"""
        return str(self._currentRoll)   
