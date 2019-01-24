package presentation;

import java.awt.event.ComponentEvent;
import java.awt.event.ComponentListener;

import javax.swing.JFrame;

import gamecomponents.Magic8Ball;


/**
 * A windowed frame that will contain a Magic 8 Ball and display it's answer when moved.
 * 
 * @author Michael J. Holmes
 * @version 1.0   January 25, 2018
 *
 */
public class Magic8BallFrame extends JFrame {
	
	//------------------------------------
	// Instance Variables
	//------------------------------------
	private Magic8BallPanel oracle;
	
	
	//------------------------------------
	// Constructors
	//------------------------------------
	
	/**
	 * Creates a frame with a Magic 8 Ball in it.
	 */
	public Magic8BallFrame(){
		
		this.setTitle("Magic 8 Ball");
		this.setSize(360,450);
	
		//Create a Magic 8 Ball panel and add it to the Frame
		oracle = new Magic8BallPanel();
		add(oracle);
		
		//Attached a listener to the Frame
		this.addComponentListener(new ShakeListener());
	}

	
	
	
	/**
	 * ShakeListener is an inner class that will provide a listener to respond to
	 * the frame being moved and shake the Magic 8 Ball.
	 * 
	 * @author Michael J. Holmes
	 * @version 1.0  January 25, 2018
	 *
	 */
	private class ShakeListener implements ComponentListener{

		//------------------------------------
		// Instance Variables
		//------------------------------------
		private int shakeCount;
		
		
		//------------------------------------
		// Constructor
		//------------------------------------
		/**
		 * Initializes a listener that will listen to when the component is Moved.
		 */
		private ShakeListener(){
			shakeCount = 0;
		}
		
		
		//------------------------------------
		// Class methods
		//------------------------------------
		/**
		 * Responds when the component is moved.
		 */
		@Override
		public void componentMoved(ComponentEvent arg0) {
		
			switch (shakeCount){
				case 1:
					oracle.clear();
					break;
				case 40:
					oracle.shake();
					break;
				case 75:
					shakeCount = 0;
					break;
				default:
			}
			
			shakeCount++;
		}
		
		@Override
		public void componentHidden(ComponentEvent arg0) {/*Do Nothing.*/}

		@Override
		public void componentResized(ComponentEvent arg0) {/*Do Nothing.*/}

		@Override
		public void componentShown(ComponentEvent arg0) {/*Do Nothing.*/}
		
	}
}
