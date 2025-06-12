package eidi2.sose25.nachname.vorname.sheet06.ex01;

public class BinaryTree <T extends Comparable<T>> implements Tree<T> {
	private Node<T> root;
	private int size;

	@Override
	public boolean add(T value){
		if (root == null){ root = new Node<T>(value); size++; return true;}
		return addNode(root, value);
	}

	private boolean addNode(Node<T> node, T value){
		if (value.compareTo(node.value) < 0){
			if (node.left == null){
				node.left = new Node<T>(value); size++; return true;
			}
			return addNode(node.left, value);
		}
		if (value.compareTo(node.value) > 0){
			if (node.right == null){
				node.right = new Node<T>(value); size++; return true;
			}
			return addNode(node.right, value);
		}
		return false;
	}

	@Override
	public boolean addIt(T value){
		if (root == null){ root = new Node<T>(value); size++; return true;}
		Node<T> node = root;
		for(int ii = 0; ii < size; ii++){
			if (value.compareTo(node.value) < 0){
				if (node.left == null){
					node.left = new Node<T>(value); size++; return true;
				}
				node = node.left; continue;
			}
			if (value.compareTo(node.value) > 0){
				if (node.right == null){
					node.right = new Node<T>(value); size++; return true;
				}
				node = node.right; continue;
			}
		}
		return false;
	}

	@Override
	public String preorder(){
		if(root == null) return "";
		StringBuilder sb = new StringBuilder();
		sb.append("[");
		printSubTreePreorder(sb, root);
		sb.delete(sb.lastIndexOf(","), sb.length());
		sb.append("]");
		return sb.toString();
	}

	private void printSubTreePreorder(StringBuilder sb, Node<T> node){
		sb.append(node.value.toString());
		sb.append(", ");
		if(node.left != null){ printSubTreePreorder(sb, node.left);}
		if(node.right != null){ printSubTreePreorder(sb, node.right);}
	}

	@Override
	public String inorder(){
		if(root == null) return "";
		StringBuilder sb = new StringBuilder();
		sb.append("[");
		printSubTreeInorder(sb, root);
		sb.delete(sb.lastIndexOf(","), sb.length());
		sb.append("]");
		return sb.toString();
	}

	private void printSubTreeInorder(StringBuilder sb, Node<T> node){
		if(node.left != null){ printSubTreeInorder(sb, node.left);}
		sb.append(node.value.toString());
		sb.append(", ");
		if(node.right != null){ printSubTreeInorder(sb, node.right);}
	}

	@Override
	public String postorder(){
		if(root == null) return "";
		StringBuilder sb = new StringBuilder();
		sb.append("[");
		printSubTreePostorder(sb, root);
		sb.delete(sb.lastIndexOf(","), sb.length());
		sb.append("]");
		return sb.toString();
	}

	private void printSubTreePostorder(StringBuilder sb, Node<T> node){
		if (node.left != null) printSubTreePostorder(sb, node.left);
		if (node.right != null) printSubTreePostorder(sb, node.right);
		sb.append(node.value.toString());
		sb.append(", ");
	}

	@Override
	public int size(){return size;}

	private void AddCurrentAndChildrenIfNotVal(BinaryTree<T> tree, Node<T> node, T val){
		if(!node.value.equals(val)) tree.add(node.value);
		if(node.left != null)	AddCurrentAndChildrenIfNotVal(tree, node.left, val);
		if(node.right != null) AddCurrentAndChildrenIfNotVal(tree, node.right, val);
	}

	@Override
	public boolean remove(T value){
		if(root == null) return false;
		BinaryTree<T> newTree = new BinaryTree<>();
		AddCurrentAndChildrenIfNotVal(newTree, root, value);
		if(size == newTree.size) return false;
		else{
			root = newTree.root;
			size = newTree.size;
			return true;
		}
	}
}
