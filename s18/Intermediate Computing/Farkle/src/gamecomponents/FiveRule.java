package gamecomponents;

import java.util.ArrayList;

public class FiveRule implements DieScoreRules {
	private int score;
	
	
	public FiveRule() {
		score = 0;
	}

	@Override
	public int getScore(ArrayList<FarkleDie> myDice) {
		int count = 0;
		for(FarkleDie currentDie:myDice) {
			if(currentDie.isHeld() && !currentDie.isScored()) {
				if(currentDie.getCurrentValue() == 5) {
					count+=1;
					currentDie.scored();
				}
			}
		}
		if(count == 0) {
			score = 0;
		} else if (count == 1) {
			score = 50;
		} else if (count == 2) {
			score = 100;
		} else if (count == 3) {
			score = 500;
		} else if (count == 4) {
			score = 550;
		} else if (count == 5) {
			score = 600;
		} else if (count == 6) {
			score = 1000;
		}
		
		return score;
	}

}
