package eidi2.sose25.nachname.vorname.sheet06.ex01;

public class Node<T extends Comparable<T>> {

	T value;
	Node<T> left;
	Node<T> right;

	public Node(T value) {
		this.value = value;
	}

	@Override
	public String toString() {
		return String.format("%s", value.toString());
	}
}