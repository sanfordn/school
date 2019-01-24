package gamecomponents;

import java.util.ArrayList;

public class ThreeRule implements DieScoreRules {
	
	

	private int score;
	
	public ThreeRule() {
		score = 0;
	}

	@Override
	public int getScore(ArrayList<FarkleDie> myDice) {
		int count = 0;
		for(FarkleDie currentDie:myDice) {
			if(currentDie.isHeld() && !currentDie.isScored()) {
				if(currentDie.getCurrentValue() == 3) {
					count+=1;
					currentDie.scored();
				}
			}
		}
		if (count == 3) {
			score = 300;
		} else if (count == 6) {
			score = 600;
		} else {
			score = 0;
		}
		return score;
	}

}
