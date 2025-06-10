package eidi2.sose25.nachname.vorname.sheet06.ex01;

public interface Tree<T> {

	boolean add(T value);

	boolean addIt(T value);

	String preorder();

	String inorder();

	String postorder();

	int size();

	boolean remove(T value);
}
