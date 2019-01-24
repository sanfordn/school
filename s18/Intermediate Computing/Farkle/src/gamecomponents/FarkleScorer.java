package gamecomponents;

import java.util.ArrayList;

import presentation.DiePanel;

public interface FarkleScorer {
	public int scoreDice(ArrayList<FarkleDie> myDice);
	public boolean isFarkle(ArrayList<FarkleDie> myDice);
}
