package presentation;

import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.*;
import gamecomponents.*;


/** 
 * The DiePanel class draws the image of a die.
 * 
 * @author Michael J. Holmes
 * @version 2.0 Jan 8, 2015.
 */

public class DiePanel extends JPanel 
{
	
	
	//----------------------------------------------------------------------------------
    // Instance Variables
	//----------------------------------------------------------------------------------
    private static final int PIP_DIAMETER = 15;
    public FarkleDie myDie;
      
  
	//----------------------------------------------------------------------------------
    // Constructors
	//----------------------------------------------------------------------------------
    
    /** 
     * Default constructor creates a white die.
     */
    public DiePanel() 
    {
        myDie = new FarkleDie();
    
        this.setBackground(Color.white);
        this.setPreferredSize(new Dimension(100,100)); 
        this.addMouseListener(new clickListener());
    }
    
    //----------------------------------------------------------------------------------
    //Class Methods
    //----------------------------------------------------------------------------------
    /** 
     * Rolls the die and repaints the display to the new result.
     */
    public void rollDie()
    {
        myDie.roll();
        repaint();    
    }
    
    public int getCurrentNum() {
    	return myDie.getCurrentValue();
    }
    
    public void reset() {
    	myDie.reset();
    	this.setBackground(Color.white);
    	myDie.roll();
    }
    
    public void flipHeld() {
    	myDie.flipHeld();
    }
    
    public boolean isHeld() {
    	return myDie.isHeld();
    }
    
    public boolean isScored() {
    	return myDie.isScored();
    }


    /** 
     * Defines how this object is drawn on the screen.
     * 
     * @param g The Graphics object to draw to.
     */
    public void paintComponent(Graphics g) 
    {
    	// Required to draw the panel.
        super.paintComponent(g);
        
        // Initialize local variables.
        int panelWidth = this.getWidth();
        int panelHeight = this.getHeight(); 
        
        // Draw the outside border of die.
        g.drawRoundRect(0, 0, panelWidth-1, panelHeight-1, 10, 10);
                
        // Add on the pips.
        this.drawPips(g, myDie.getCurrentValue());
    }
    
    
    
    //----------------------------------------------------------------------------------
    // Private Helper Methods
    //----------------------------------------------------------------------------------
    
    /** 
     * Defines how this object is drawn on the screen.
     * 
     * @param g The Graphics object to draw to.
     * @param numberOfPips the number of pips to draw on the die.
     */    
    private void drawPips(Graphics g, int numberOfPips)
    {
    	//Initialize local variables.
        int panelWidth = this.getWidth();
        int panelHeight = this.getHeight(); 
    	
        //Conditinal to determine how many and locations of pips.
    	switch (numberOfPips) 
        {
        case 1: drawPip(g, panelWidth/2, panelHeight/2);
                break;
        
        case 2: drawPip(g, panelWidth/4, panelHeight/4);
                drawPip(g, 3*panelWidth/4, 3*panelHeight/4);
                break;
                
        case 3: drawPip(g, panelWidth/2, panelHeight/2);
        		drawPip(g, panelWidth/4, panelHeight/4);
        		drawPip(g, 3*panelWidth/4, 3*panelHeight/4);
                break;
        
        case 4: drawPip(g, panelWidth/4, panelHeight/4);
                drawPip(g, 3*panelWidth/4, 3*panelHeight/4);
                drawPip(g, 3*panelWidth/4, panelHeight/4);
                drawPip(g, panelWidth/4, 3*panelHeight/4);
                break;
                
        case 5: drawPip(g, panelWidth/2, panelHeight/2);
                drawPip(g, panelWidth/4, panelHeight/4);
                drawPip(g, 3*panelWidth/4, 3*panelHeight/4);
                drawPip(g, 3*panelWidth/4, panelHeight/4);
                drawPip(g, panelWidth/4, 3*panelHeight/4);
                break;
                
        case 6: drawPip(g, panelWidth/4, panelHeight/4);
                drawPip(g, 3*panelWidth/4, 3*panelHeight/4);
                drawPip(g, 3*panelWidth/4, panelHeight/4);
                drawPip(g, panelWidth/4, 3*panelHeight/4);
                drawPip(g, panelWidth/4, panelHeight/2);
                drawPip(g, 3*panelWidth/4, panelHeight/2);
                break;
         }
    }
    
    private class clickListener implements MouseListener
	{
		public void mouseClicked(MouseEvent arg0) 
		{
			if(!myDie.isScored()) {
				if(myDie.isHeld()) {
					DiePanel.this.setBackground(Color.WHITE);
				} else {
					DiePanel.this.setBackground(Color.yellow);
				}
				myDie.flipHeld();
			}
			
		}

		public void mouseEntered(MouseEvent arg0) 
		{
		}

		public void mouseExited(MouseEvent arg0) 
		{
		}

		public void mousePressed(MouseEvent arg0) 
		{
		}

		public void mouseReleased(MouseEvent arg0) 
		{
		}
	}
    
    
    /** 
     * Defines how this object is drawn on the screen.
     * 
     * @param g The Graphics object to draw to.
     * @param x the x coordinate of where to draw the pip.
     * @param y the y coordinate of where to draw the pip.
     */       
    private void drawPip(Graphics g, int x, int y) 
    {
        g.fillOval(x-PIP_DIAMETER/2, y-PIP_DIAMETER/2, PIP_DIAMETER, PIP_DIAMETER);
    }
    
    
    
}