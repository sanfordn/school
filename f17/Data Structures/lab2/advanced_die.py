"""
File:  advanced_die.py
Description: Implements an AdvancedDie class that allows for any number of sides
Inherits from the parent class Die in module simple_die
"""
from simple_die import Die
from random import randint

class AdvancedDie(Die):
    """AdvancedDie class that allows for any number of sides"""

    def __init__(self, sides = 6):
        """Constructor for any-sided Die that takes the number of sides 
        as a parameter; if no parameter is given then default is 6-sided.
        Precondition: sides is an integer >= 1
        Postcondition:  current roll of the die between 1 and sides
        Raises: TypeError if sides in not an integer
                ValueError if sides < 1"""
        # Check preconditions
        if not isinstance(sides,int):
            raise TypeError("Die sides must be an integer!")
        if sides < 1:
            raise ValueError("Die sides must be a positive integer!")
        # call Die parent class constructor
        Die.__init__(self)
        self._numSides = sides
        self._currentRoll = randint(1, self._numSides)

    def roll(self):
        """Resets the die's value to a random number between 1 and the number
           of sides on the die.
           Precondition: none
           Postcondition: current roll randomly reset between 1 and the number
           of sides on the die."""
        self._currentRoll = randint(1, self._numSides)
    
    def __eq__(self, rhs_Die):
        """Returns the result of comparing the current rolls on two Die objects for equality.
           Precondition: rhs_Die is a Die
           Postcondition:  if self's current roll is equal rhs_Die's current roll, return True;
                        otherwise return False.
           Raises: TypeError if rhs_Die is not a Die"""

        if not isinstance(rhs_Die, Die):
            raise TypeError("right-hand-side operand of == must be a Die!")
        return self._currentRoll == rhs_Die._currentRoll

    def __lt__(self, rhs_Die):
        """Returns the result of comparing the current rolls on two Die objects for 'less than' (<).
           Precondition: rhs_Die is a Die
           Postcondition:  if self's current roll is < rhs_Die's current roll, return True;
                        otherwise return False.
           Raises: TypeError if rhs_Die is not a Die"""
        return self._currentRoll < rhs_Die._currentRoll

    def __gt__(self, rhs_Die):
        """Returns the result of comparing the current rolls on two Die objects for 'greater than' (>).
           Precondition: rhs_Die is a Die
           Postcondition:  if self's current roll is > rhs_Die's current roll, return True;
                        otherwise return False.
           Raises: TypeError if rhs_Die is not a Die"""
        return self._currentRoll > rhs_Die._currentRoll

    def __le__(self, rhs_Die):
        """Returns the result of comparing the current rolls on two Die objects for 'less than or equal' (<=).
           Precondition: rhs_Die is a Die
           Postcondition:  if self's current roll is <= rhs_Die's current roll, return True;
                        otherwise return False.
           Raises: TypeError if rhs_Die is not a Die"""
        return self._currentRoll <= rhs_Die._currentRoll

    def __ge__(self, rhs_Die):
        """Returns the result of comparing the current rolls on two Die objects for 'greater than or equal' (>=).
           Precondition: rhs_Die is a Die
           Postcondition:  if self's current roll is >= rhs_Die's current roll, return True;
                        otherwise return False.
           Raises: TypeError if rhs_Die is not a Die"""
        return self._currentRoll > rhs_Die._currentRoll

    def __str__(self):
        """Returns the string representation of the AdvancedDie.
           Precondition:  none
           Postcondition:  returns a string containing the number of sids and the
                           current roll of the die."""
        return 'Number of Sides='+str(self._numSides)+' Roll='+str(self._currentRoll)   

    def __add__(self, rhs_Die):
        """Returns the sum of two dice rolls
           Precondition: rhs_Die is a Die
           Postcondition:  returns the sum of self's current roll and rhs_Die's
                           current roll values
           Raises: TypeError if rhs_Die is not a Die"""

        if not isinstance(rhs_Die, Die):
            raise TypeError("right-hand-side operand must be a Die!")

        return self._currentRoll + rhs_Die._currentRoll
        
    def getSides(self):
        """Returns the number of sides on the die.
           Precondition:  none
           Postcondition:  returns the number of sides"""
        return self._numSides



