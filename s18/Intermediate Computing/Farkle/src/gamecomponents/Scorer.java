package gamecomponents;

import java.util.ArrayList;

public class Scorer implements FarkleScorer {
	private ArrayList<DieScoreRules> myRules;
	private OneRule theOneRule;
	private TwoRule theTwoRule;
	private ThreeRule theThreeRule;
	private FourRule theFourRule;
	private FiveRule theFiveRule;
	private SixRule theSixRule;
	
	
	public Scorer() {
		
		myRules = new ArrayList<DieScoreRules>();
		
		theOneRule = new OneRule();
		theTwoRule = new TwoRule();
		theThreeRule = new ThreeRule();
		theFourRule = new FourRule();
		theFiveRule = new FiveRule();
		theSixRule = new SixRule();
		
		
		myRules.add(theOneRule);
		myRules.add(theTwoRule);
		myRules.add(theThreeRule);
		myRules.add(theFourRule);
		myRules.add(theFiveRule);
		myRules.add(theSixRule);
		
	}

	@Override
	public int scoreDice(ArrayList<FarkleDie> myDice) {
		int currentScore = 0;
		for(DieScoreRules currentRule:myRules) {
			currentScore += currentRule.getScore(myDice);
		}
		return currentScore;
	}

	@Override
	public boolean isFarkle(ArrayList<FarkleDie> myDice) {
		// TODO Auto-generated method stub
		int currentScore = 0;
		for(DieScoreRules currentRule:myRules) {
			currentScore += currentRule.getScore(myDice);
		}
		return currentScore==0;
		
	}

}
