package gamecomponents;

import java.util.ArrayList;

public class FourRule implements DieScoreRules {
	private int score;
	
	public FourRule() {
		score = 0;
	}

	@Override
	public int getScore(ArrayList<FarkleDie> myDice) {
		int count = 0;
		for(FarkleDie currentDie:myDice) {
			if(currentDie.isHeld() && !currentDie.isScored()) {
				if(currentDie.getCurrentValue() == 4) {
					count+=1;
					currentDie.scored();
				}
			}
		}
		if (count == 3) {
			score = 400;
		} else if (count == 6) {
			score = 800;
		}
		else {
			score = 0;
		}
		return score;
	}

}
