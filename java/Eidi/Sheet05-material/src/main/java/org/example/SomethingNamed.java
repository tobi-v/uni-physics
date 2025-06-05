package eidi2_ex05;

public class SomethingNamed extends Something{
	
	private String name;
	
	public SomethingNamed(int number) {
		super(number);
		this.name = "X";
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	@Override
	public String toString() {
		return "[" + this.name + "(" + this.number + ")]";
	}
	
}
