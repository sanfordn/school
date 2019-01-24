package presentation;

import java.awt.*;
import javax.swing.*;

import gamecomponents.*;

import java.awt.event.*;
import java.util.ArrayList;

/** 
 * The DieFrame class contains a Frame with two dice and a roll button.
 * 
 * @author Michael J. Holmes
 * @version 1.0 Dec 17, 2012.
 */
public class DiceFrame extends JFrame
{
	//----------------------------------------------------------------------------------
    // Instance Variables
	//----------------------------------------------------------------------------------
    private DiePanel die1;
    private DiePanel die2;
    private DiePanel die3;
    private DiePanel die4;
    private DiePanel die5;
    private DiePanel die6;
    private FarkleDice farkleDice;
    private JPanel field;
    private JPanel menu;
    //private int turnScore;
    private JButton scoreButton;
    private JButton resetButton;
    private JButton rollButton;
    private int player = 1;
    private int firstScore = 0;
    private int secondScore = 0;
   

    
	//----------------------------------------------------------------------------------
    // Constructors
	//----------------------------------------------------------------------------------    
    public DiceFrame()
    {
    	/** 
        	* Default constructor.
        */
    	
    	// Initialize the frame properties
    	this.setLayout(new FlowLayout());
	   	this.setSize( 300, 300 );
       	this.setTitle( "Farkle" );


       	this.createFieldPanel();
       	this.createMenuPanel();
       

       	//Add the field and menu panels to the frame.
       	this.add(field);
       	this.add(menu);
   }
   
    
	//----------------------------------------------------------------------------------
    // Class Methods
	//----------------------------------------------------------------------------------    
    public void resetDice() {
    	die1.reset();
		die2.reset();
		die3.reset();
		die4.reset();
		die5.reset();
		die6.reset();
		rollDice();
		scoreButton.setEnabled(true);
		rollButton.setEnabled(false);
		flipTurn();
    }
    
    public void scoreDice() {
    	int turnScore;
    	
    	ArrayList<FarkleDie> myDice = new ArrayList<FarkleDie>(6);
		myDice.add(die1.myDie);
		myDice.add(die2.myDie);
		myDice.add(die3.myDie);
		myDice.add(die4.myDie);
		myDice.add(die5.myDie);
		myDice.add(die6.myDie);
		
		FarkleScorer myScorer = new Scorer();
		turnScore = myScorer.scoreDice(myDice);
		if(player == 1) {
			firstScore +=turnScore;
		} else {
			secondScore += turnScore;
		}
		
		if(turnScore != 0) {
			if(die1.isScored()) {
    			die1.setBackground(Color.red);
    		}
    		if (die2.isScored()) {
    			die2.setBackground(Color.red);
    		}
    		if (die3.isScored()) {
    			die3.setBackground(Color.red);
    		}
    		if(die4.isScored()) {
    			die4.setBackground(Color.red);
    		}
    		if (die5.isScored()) {
    			die5.setBackground(Color.red);
    		}
    		if (die6.isScored()) {
    			die6.setBackground(Color.red);
    		}
    		
    		scoreButton.setEnabled(false);
    		rollButton.setEnabled(true);
    		
    		if (die1.isScored() && die2.isScored() && die3.isScored() 
    				&& die4.isScored() && die5.isScored() && die6.isScored()) {
    			die1.reset();
    			die2.reset();
    			die3.reset();
    			die4.reset();
    			die5.reset();
    			die6.reset();
    			scoreButton.setEnabled(true);
    			rollButton.setEnabled(false);
    		}
    		
    		if(player == 1) {
    			JOptionPane.showMessageDialog(field,"Player 1's Score is: " + firstScore);
    		} else {
    			JOptionPane.showMessageDialog(field,"Player 2's Score is: " + secondScore);
    		}
    		
		} else {
			JOptionPane.showMessageDialog(field, "You Farkled!");
			resetDice();
		}
		
    }
    
    public void flipTurn() {
    	if(player == 1) {
    		player = 2;
    	} else {
    		player = 1;
    	}
    }
    
    public void rollDice() {
    	if (!die1.isHeld() && !die1.isScored()) {
			die1.rollDie();
		}
		if (!die2.isHeld() && !die2.isScored()) {
			die2.rollDie();
		}
		if (!die3.isHeld() && !die3.isScored()) {
			die3.rollDie();
		}
		if (!die4.isHeld() && !die4.isScored()) {
			die4.rollDie();
		}
		if (!die5.isHeld() && !die5.isScored()) {
			die5.rollDie();
		}
		if (!die6.isHeld() && !die6.isScored()) {
			die6.rollDie();
		}
		scoreButton.setEnabled(true);
		rollButton.setEnabled(false);
		
		
    }
    

    
  
	//----------------------------------------------------------------------------------
    // Private Helpers
	//----------------------------------------------------------------------------------  

    /** 
     * Build the menu panel.
    */
    private void createMenuPanel()
    {
    	//Set up the menu area.
    	menu = new JPanel();
    	menu.setBounds(0,300,250,100);
       	//Create a button and add a listener to it.
    	rollButton = new JButton("Re-Roll");
    	rollButton.setSize(300,200);
    	resetButton = new JButton("Reset");
    	resetButton.setSize(300,200);
    	scoreButton = new JButton("Score");
    	scoreButton.setSize(300,200);
      
   
    	rollButton.addActionListener(new RollListener());
    	resetButton.addActionListener(new ResetListener());
    	scoreButton.addActionListener(new ScoreListener());
      
    	//Add the button to the menu area.
    	menu.add(rollButton);
    	menu.add(resetButton);
    	menu.add(scoreButton);
    	rollButton.setEnabled(false);
    }
    
    
    /** 
     * Build the field panel.
    */
    private void createFieldPanel()
    {
        //Set up the dice field area.
        field = new JPanel();
        field.setBounds(0,0,250,200);
       
        //Create the dice and add them.
        die1 = new DiePanel();
        die2 = new DiePanel();
        die3 = new DiePanel();
        die4 = new DiePanel();
        die5 = new DiePanel();
        die6 = new DiePanel();
        field.add(die1);
        field.add(die2);
        field.add(die3);
        field.add(die4);
        field.add(die5);
        field.add(die6);
    	
    }
    
    private class ResetListener implements ActionListener {
    	public void actionPerformed(ActionEvent reset) {
    		resetDice();
    	}
    }
    
    private class ScoreListener implements ActionListener {
    	public void actionPerformed(ActionEvent score) {
    		scoreDice();
    	}
    }
    
    private class RollListener implements ActionListener {
    	public void actionPerformed(ActionEvent roll) { 
    		rollDice();
    	}
    }
}