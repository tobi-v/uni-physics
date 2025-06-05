package org.example;

public class Something implements Comparable<Something> {
	
	protected int number;
	
	public Something(int i) {
		this.number = i;
	}

	public int getNumber() {
		return number;
	}

	public void setNumber(int number) {
		this.number = number;
	}

	@Override
	public String toString() {
		return "[" + number + "]";
	}

	@Override
	public int compareTo(Something o) {
		return this.number - o.getNumber();
	}
	
	@Override
	public boolean equals(Object o) {
		if(o == null || !(o instanceof Something)) {
			return false;
		} else {
			return (this.number - ((Something) o).getNumber()) == 0;
		}
	}

}
