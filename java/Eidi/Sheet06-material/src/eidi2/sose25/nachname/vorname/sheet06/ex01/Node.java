package eidi2.sose25.nachname.vorname.sheet06.ex01;

public class Node {

	char value;
	Node left;
	Node right;

	public Node(char value) {
		this.value = value;
	}

	@Override
	public String toString() {
		return String.format("%s", value);
	}
}