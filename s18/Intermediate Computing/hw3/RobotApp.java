/*	
*	Programmer: Nick Sanford
*	Date: 24 January 2018
*	File: RobotApp.java
*	Description: Using the Robot class to create a robot fighting game where the user
*		fights a computer robot by either attacking or raising its shields
*/


import java.util.Scanner;


public class RobotApp {
	public static void main(String[] args) {
		String userInput = "";
		boolean gameOver = false;
		Robot playerBot = new Robot();
		Robot computerBot = new Robot();
		Scanner consoleInput = new Scanner(System.in);
		System.out.println("Welcome to the Robot Battle Game");	
		
		while(gameOver == false) {
			printStatus(playerBot,computerBot);
			System.out.print("(A)ttack or (S)hields?: ");
			userInput = consoleInput.next();
		
			if (userInput.toUpperCase().startsWith("A")) {
				playerBot.attack(computerBot);
				computerBot.attack(playerBot);
				System.out.println("ComputerBot Attacks!\n");
			} else if(userInput.toUpperCase().startsWith("S")) {
				playerBot.raiseShields();
				computerBot.attack(playerBot);
				System.out.println("ComputerBot Attacks!\n");
			} else {
				System.out.println("Incorrect input.");
			}
			
			if (playerBot.getPowerLevel() == 0) {
				gameOver = true;
				System.out.println("YOU LOSE!");
			} else if(computerBot.getPowerLevel() == 0) {
				gameOver = true;
				System.out.println("YOU WIN!");
			}
			
			
			
			

		}
		
		
		
		
		
	}

	public static void printStatus(Robot player,Robot com) {
		System.out.println("PlayerBot: Power = " + player.getPowerLevel() + " " + "Shield = " + player.getShieldLevel());
		System.out.println("ComputerBot: Power = " + com.getPowerLevel() + " " + "Shield = " + com.getShieldLevel());
	}
	
	
	
	
	
}
