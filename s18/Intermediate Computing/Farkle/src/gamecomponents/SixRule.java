package gamecomponents;

import java.util.ArrayList;

public class SixRule implements DieScoreRules {

	private int score;
	
	public SixRule() {
		score = 0;
	}

	@Override
	public int getScore(ArrayList<FarkleDie> myDice) {
		int count = 0;
		for(FarkleDie currentDie:myDice) {
			if(currentDie.isHeld() && !currentDie.isScored()) {
				if(currentDie.getCurrentValue() == 6) {
					count+=1;
					currentDie.scored();
				}
			}
		}
		if (count == 3) {
			score = 600;
		} else if (count == 6) {
			score = 1200;
		} else {
			score = 0;
		}
		return score;
	}

}
