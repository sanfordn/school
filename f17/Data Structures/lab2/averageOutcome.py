"""
File:  averageOutcomes.py
Description:  Rolls two 10-sided dice 1,000 times to determine the average outcome
on the pair of dice.
"""
from random import randint
from advanced_die import AdvancedDie
from more_advanced_die import MoreAdvancedDie

# Global Constants
NUMBER_OF_ROLLS = 1000
DIE_SIDES = 10

def main():
    """ Main program provides an outline of program """
    displayWelcome()
    averageOutcome = calculateAverageOutcome()
    displayResults(averageOutcome)


def displayWelcome():
    """ Displays welcome message for the user """
    print("This program rolls two %d-sided dice %d times to"
          % (DIE_SIDES,NUMBER_OF_ROLLS))
    print("determine the average outcome on the pair of dice.")
    print()


def calculateAverageOutcome():
    """Rolls a pair of dice the correct number of times, tallies the outcomes, and
       returns the average outcome."""
    outcomesTotal = 0
    die = AdvancedDie(DIE_SIDES)
    rhsDie = AdvancedDie(DIE_SIDES)
        
    for count in range(NUMBER_OF_ROLLS):
        die.roll()
        rhsDie.roll()
        #print('die 1 roll =', die.getRoll())
        #print('die 2 roll =', rhsDie.getRoll())
        outcome = die.getRoll() + rhsDie.getRoll() #randint(1,DIE_SIDES) + randint(1,DIE_SIDES)
        outcomesTotal += outcome
        #print('outcome total is:', outcomesTotal)


    return outcomesTotal / NUMBER_OF_ROLLS


def displayResults(averageOutcome):
    """ Displays the average outcome"""
    print("The average outcome was %3.1f." % averageOutcome)
    newDie = MoreAdvancedDie(13)
    newDie.setRoll(11)
    print('More Advanced Die roll is:', newDie.getRoll())
main()
    
        
    
    


