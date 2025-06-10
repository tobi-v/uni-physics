package eidi2.sose25.nachname.vorname.sheet06.ex01;

public class BinaryTree <T extends Comparable<T>> implements Tree<T> {
	private Node<T> root;

	@Override
	public boolean add(T value){
		if (root == null){ root = new Node<T>(value); return true;}
		return addNode(root, value);
	}

	private boolean addNode(Node<T> node, T value){
		if (value.compareTo(node.value) < 0){
			if (node.left == null){
				node.left = new Node<T>(value); return true;
			}
			return addNode(node.left, value);
		}
		if (value.compareTo(node.value) > 0){
			if (node.right == null){
				node.right = new Node<T>(value); return true;
			}
			return addNode(node.right, value);
		}
		return false;
	}

	@Override
	public boolean addIt(T value){
		Node<T> node = root;
		if (node == null){ node = new Node<T>(value); return true;}
		while(true){
			if (value.compareTo(node.value) < 0){
				if (node.left == null){
					node.left = new Node<T>(value); return true;
				}
				node = node.left; continue;
			}
			if (value.compareTo(node.value) > 0){
				if (node.right == null){
					node.right = new Node<T>(value); return true;
				}
				node = node.right; continue;
			}
			return false;

		}
	}

	@Override
	public String preorder(){return "";}

	@Override
	public String inorder(){return "";}

	@Override
	public String postorder(){return "";}

	@Override
	public int size(){return 0;}

	@Override
	public boolean remove(T value){
		return false;
	}
}
