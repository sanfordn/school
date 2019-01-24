package gamecomponents;

import java.util.Random;



/** 
 * The Die class represents a die of variable sides, and can be rolled to return a random value.
 * 
 * @author Michael J. Holmes
 * @version 2.0 Jan 8, 2015.
 */

public class Die
{
    //----------------------------------------------------------------------------------
    // Instance Variables
    //----------------------------------------------------------------------------------
    private int numSides;
    private int currentValue;
    private Random myRandomNumGenerator;
      
    
    //----------------------------------------------------------------------------------
    //Constructors
    //----------------------------------------------------------------------------------
   
    /** 
     * Default constructor creates a 6-sided die.
     */
    public Die()
    {
        numSides = 6;
        myRandomNumGenerator = new Random();
        roll();
    }
    
    /** 
     * This constructor takes in a single integer value and create a die with
     * that number of sides.
     * 
     * @param aNumSides Number of sides to create on the die.
     */
    public Die(int aNumSides)
    {
        numSides = aNumSides;
        myRandomNumGenerator = new Random();
        roll();
    }
    
    
    
    //----------------------------------------------------------------------------------
    //Class Methods
    //----------------------------------------------------------------------------------
    
    /** 
     * Getter for the number of sides on the die.
     * 
     * @return The number of sides on the die.
     */
    public int getNumOfSides() 
    {
        return numSides;
    }
    
    
    /** 
     * Getter for the number of sides on the die.
     * 
     * @return The number of sides on the die.
     */
    public int getCurrentValue() 
    {
        return currentValue;
    }
       
    /** 
     * Rolls the die to get a random value.
     * 
     * @return A random value between 1 and the number of sides.
     */
    public int roll() 
    {
        currentValue = myRandomNumGenerator.nextInt(numSides) + 1;
        return currentValue;
    }
    
}

