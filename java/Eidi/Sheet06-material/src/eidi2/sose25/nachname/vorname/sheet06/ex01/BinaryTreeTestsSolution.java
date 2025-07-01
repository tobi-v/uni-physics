package eidi2.sose25.nachname.vorname.sheet06.ex01;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

import org.junit.Test;
import org.junit.Assert;

public class BinaryTreeTestsSolution {

	private static Random random = new Random(42);
	private static int N = 5000;

	@Test(timeout = 1000)
	public void testAdd() {
		BinaryTree<Integer> tree = new BinaryTree<>();

		List<Integer> list = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			list.add(Math.abs(random.nextInt()));
		}

		for (int n : list) {
			tree.add(n);
		}

		Assert.assertEquals(N, tree.size());

		Collections.sort(list);
		compareInorderToList(tree.inorder(), list);
	}

	@Test(timeout = 1000)
	public void testAddIt() {
		BinaryTree<Integer> tree = new BinaryTree<>();

		List<Integer> list = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			list.add(Math.abs(random.nextInt()));
		}

		for (int n : list) {
			tree.addIt(n);
		}

		Assert.assertEquals(N, tree.size());

		Collections.sort(list);
		compareInorderToList(tree.inorder(), list);
	}

	@Test(timeout = 1000)
	public void testAddBoth() {
		BinaryTree<Integer> tree1 = new BinaryTree<>();
		BinaryTree<Integer> tree2 = new BinaryTree<>();

		List<Integer> list = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			list.add(Math.abs(random.nextInt()));
		}

		for (int n : list) {
			Assert.assertEquals(tree1.add(n), tree2.addIt(n));
		}
	}

	@Test(timeout = 1000)
	public void testAddReturns() {
		BinaryTree<Integer> tree = new BinaryTree<>();

		int[] arr = { 5, 1, 4, 3, 7, 9, 8, 7, 3, 5, 6 };
		boolean[] isDuplicate = { false, false, false, false, false, false, false, true, true, true, false };

		for (int k = 0; k < arr.length; k++) {
			Assert.assertEquals(!isDuplicate[k], tree.add(arr[k]));
		}

		Assert.assertEquals(8, tree.size());
	}

	@Test(timeout = 1000)
	public void testAddItReturns() {
		BinaryTree<Integer> tree = new BinaryTree<>();

		int[] arr = { 5, 1, 4, 3, 7, 9, 8, 7, 3, 5, 6 };
		boolean[] isDuplicate = { false, false, false, false, false, false, false, true, true, true, false };

		for (int k = 0; k < arr.length; k++) {
			Assert.assertEquals(!isDuplicate[k], tree.addIt(arr[k]));
		}

		Assert.assertEquals(8, tree.size());
	}

	@Test(timeout = 1000)
	public void testStringOrder() {
		BinaryTree<Integer> tree = new BinaryTree<>();

		int[] arr = { 5, 1, 4, 3, 7, 9, 8, 6 };

		for (int k = 0; k < arr.length; k++) {
			tree.add(arr[k]);
		}

		Assert.assertEquals(8, tree.size());

		// inhaltlich
		Assert.assertEquals("[5, 1, 4, 3, 7, 6, 9, 8]".replaceAll("[^\\d]+", ""),
				tree.preorder().replaceAll("[^\\d]+", ""));
		Assert.assertEquals("[1, 3, 4, 5, 6, 7, 8, 9]".replaceAll("[^\\d]+", ""),
				tree.inorder().replaceAll("[^\\d]+", ""));
		Assert.assertEquals("[3, 4, 1, 6, 8, 9, 7, 5]".replaceAll("[^\\d]+", ""),
				tree.postorder().replaceAll("[^\\d]+", ""));

		// size unverändert
		Assert.assertEquals(8, tree.size());

		// korrektes Layout
		Assert.assertEquals("[5, 1, 4, 3, 7, 6, 9, 8]", tree.preorder());
		Assert.assertEquals("[1, 3, 4, 5, 6, 7, 8, 9]", tree.inorder());
		Assert.assertEquals("[3, 4, 1, 6, 8, 9, 7, 5]", tree.postorder());
	}

	@Test(timeout = 3000)
	public void testRemove() {
		BinaryTree<Integer> tree = new BinaryTree<>();

		List<Integer> list = new ArrayList<>();

		for (int i = 0; i < 1000; i++) {
			list.add(Math.abs(random.nextInt()));
		}

		for (int n : list) {
			tree.add(n);
		}

		Collections.sort(list);

		while (tree.size() > 0) {

			Integer n;
			if (random.nextDouble() < 0.1) {
				n = random.nextInt();
			} else {
				n = list.get(random.nextInt(list.size()));
			}

			boolean exists = list.contains(n);
			while (list.contains(n)) {
				list.remove(n);
			}

			Assert.assertEquals(exists, tree.remove(n));
			compareInorderToList(tree.inorder(), list);
		}
	}

	@Test(timeout = 1000)
	public void testMutate() {
		BinaryTree<Integer> tree = new BinaryTree<>();

		List<Integer> list = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			list.add(Math.abs(random.nextInt()));
		}

		for (int n : list) {
			tree.add(n);
		}

		tree.mutate(x -> 0);
		Assert.assertTrue(tree.inorder().replaceAll("[^\\d]+", "").replaceAll("[0]+", "#").equals("#"));
	}

	@Test(timeout = 1000)
	public void testFlat() {
		BinaryTree<Integer> tree = new BinaryTree<>();

		for (int i = 0; i < N; i++) {
			tree.add(Math.abs(random.nextInt()));
		}

		List<Integer> list = tree.flat((x, y) -> {
			y.add(x);
			return y;
		}, new ArrayList<Integer>());

		Collections.sort(list);
		compareInorderToList(tree.inorder(), list);
	}

	@Test(timeout = 1000)
	public void testFlatSum() {
		BinaryTree<Integer> tree = new BinaryTree<>();

		Integer sum = 0;
		for (int i = 0; i < N; i++) {
			int x = random.nextInt();
			tree.add(x);
			sum += x;
		}

		Assert.assertEquals(sum, tree.flat((x, y) -> x + y, 0));
	}

	@Test(timeout = 1000)
	public void testContains() {
		BinaryTree<Integer> tree = new BinaryTree<>();

		List<Integer> list = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			list.add(Math.abs(random.nextInt()));
		}

		for (int n : list) {
			tree.add(n);
		}

		for (int i = 0; i < N; i++) {

			Integer n;
			if (random.nextDouble() < 0.1) {
				n = random.nextInt();
			} else {
				n = list.get(random.nextInt(list.size()));
			}

			boolean exists = list.contains(n);

			Assert.assertEquals(exists, tree.contains(n));
		}
	}

	@Test(timeout = 1000)
	public void testMax() {
		for (int i = 0; i < 100; i++) {
			BinaryTree<Integer> tree = new BinaryTree<>();

			List<Integer> list = new ArrayList<>();

			for (int j = 0; j < N; j++) {
				list.add(Math.abs(random.nextInt()));
			}

			for (int n : list) {
				tree.add(n);
			}

			Integer max = Collections.max(list);
			Assert.assertEquals(max, tree.max());
		}
	}

	public static void compareInorderToList(String str, List<Integer> list) {
		String[] fields = str.replaceAll("[\\]\\[ ]", "").split(",");

		int k = 0;
		if (fields[0].equals("")) {
			k++;
		}
		for (int n : list) {
			Assert.assertEquals(String.valueOf(n), fields[k++]);
		}
	}
}
