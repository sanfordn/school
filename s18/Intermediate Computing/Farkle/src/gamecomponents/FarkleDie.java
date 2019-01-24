package gamecomponents;

public class FarkleDie extends Die {
	private boolean holdValue = false;
	private boolean scoreValue = false;
	
	
	public FarkleDie() {
		holdValue = false;
		scoreValue = false;
	}
	
	public void reset() {
		holdValue = false;
		scoreValue = false;
	}
	
	public void hold() {
		holdValue = true;
	}
	
	public boolean isScored() {
		return scoreValue;
	}
	
	public void scored() {
		scoreValue = true;
	}
	
	public void flipHeld() {
		if (isHeld()) {
			holdValue = false;
		} else {
			holdValue = true;
		}
	}
	
	public boolean isHeld() {
		return holdValue;
	}
	
	public void release() {
		holdValue = false;
	}

}
