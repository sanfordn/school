package gamecomponents;

import java.util.ArrayList;

public class OneRule implements DieScoreRules {
	private int score;
	
	public OneRule() {
		score = 0;
	}

	@Override
	public int getScore(ArrayList<FarkleDie> myDice) {
		int count = 0;
		for(FarkleDie currentDie:myDice) {
			if(currentDie.isHeld() && !currentDie.isScored()) {
				if(currentDie.getCurrentValue() == 1) {
					count+=1;
					currentDie.scored();
				}
			}
		}
		if(count == 0) {
			score = 0;
		} else if (count == 1) {
			score = 100;
		} else if (count == 2) {
			score = 200;
		} else if (count == 3) {
			score = 1000;
		} else if (count == 4) {
			score = 1100;
		} else if (count == 5) {
			score = 1200;
		} else if (count == 6) {
			score = 2000;
		}
		return score;
	}

}
