"""
File: more_advanced_die.py
Description: Gives the user an option of setting the roll number
"""

from advanced_die import AdvancedDie

class MoreAdvancedDie(AdvancedDie):
    def setRoll(self,rollNum):
        if rollNum < 1 or rollNum > self._numSides:
            raise ValueError('Roll Number must be between 1 and Die Sides!')
        if not isinstance(self._numSides,int):
            raise TypeError('Roll Number must be an integer!')
        self._currentRoll = rollNum
            
            
