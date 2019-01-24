package gamecomponents;

import java.util.ArrayList;

public class FarkleDice {
	private ArrayList<FarkleDie> myFarkleDice = new ArrayList<FarkleDie>(6);
	
	public FarkleDice() {
		for(FarkleDie myFarkleDie:myFarkleDice) {
			myFarkleDie = new FarkleDie();
		}
	}
	
	public ArrayList<Integer> rollDice() {
		ArrayList<Integer> myRolls = new ArrayList<Integer>(6);
		for(FarkleDie myFarkleDie:myFarkleDice) {
			myRolls.add(myFarkleDie.roll());
		}
		return myRolls;
		
	}

}
