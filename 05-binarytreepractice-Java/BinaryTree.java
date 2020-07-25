
class Node {
	public int value;
	public Node left, right;
	public Node(int value) {
		this.value = value;
		this.left = null;
		this.right = null;
	}
}

public class BinaryTree {
	public Node root;
	
	public BinaryTree(int value) {
		// Your code goes here
		this.root=new Node(value);
	}

	public boolean search(int value) {
		// Your code goes here
		Node node =this.root;
		return search_Node(node, value);
	}

	private boolean search_Node(Node node, int value) {
		// Your code goes here
		if (node == null) return false;
		else if (node.value == value) return true;
		boolean lft = search_Node(node.left, value);
		if(lft) return lft;
		boolean rght = search_Node(node.right, value);
		return rght;
		}

	}