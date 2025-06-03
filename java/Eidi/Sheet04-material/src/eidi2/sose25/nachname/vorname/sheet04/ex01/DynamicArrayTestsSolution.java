package eidi2.sose25.nachname.vorname.sheet04.ex01;

import org.junit.Test;
import org.junit.Assert;

public class DynamicArrayTestsSolution {

	/**
	 * Requires constructor DynamicArray() to work.
	 * Requires methods get() and size() to work.
	 */
	@Test(timeout = 1000)
	public void testAdd1() {
		DynamicArray da = new DynamicArray();

		Assert.assertEquals(0, da.size());

		da.add(5);
		Assert.assertEquals(1, da.size());
		Assert.assertEquals(5, (int) da.get(0));

		da.add(7);
		Assert.assertEquals(2, da.size());
		Assert.assertEquals(5, (int) da.get(0));
		Assert.assertEquals(7, (int) da.get(1));
	}

	/**
	 * Requires constructor DynamicArray() to work.
	 * Requires methods get() and size() to work.
	 */
	@Test(timeout = 1000)
	public void testAdd2() {
		DynamicArray da = new DynamicArray();

		Assert.assertEquals(0, da.size());

		da.add(0, 5);
		Assert.assertEquals(1, da.size());
		Assert.assertEquals(5, (int) da.get(0));

		da.add(0, 7);
		Assert.assertEquals(2, da.size());
		Assert.assertEquals(7, (int) da.get(0));
		Assert.assertEquals(5, (int) da.get(1));
	}

	/**
	 * Requires constructor DynamicArray() to work.
	 * Requires methods resize() and get() to work.
	 */
	@Test(timeout = 1000)
	public void testAdd3() {
		DynamicArray da = new DynamicArray();

		for (int i = 0; i < 1000; i++) {
			da.add(i);
		}

		for (int i = 0; i < 1000; i++) {
			Assert.assertEquals(i, (int) da.get(i));
		}
	}

	/**
	 * Requires constructor DynamicArray() to work.
	 * Requires methods resize() and get() to work.
	 */
	@Test(timeout = 1000)
	public void testAdd4() {
		DynamicArray da = new DynamicArray();

		for (int i = 0; i < 1000; i++) {
			da.add(0, i);
		}

		for (int i = 0; i < 1000; i++) {
			Assert.assertEquals(1000 - i - 1, (int) da.get(i));
		}
	}

	/**
	 * Requires constructor DynamicArray(int n) to work.
	 * Requires methods add(...), size() and get() to work.
	 */
	@Test(timeout = 1000)
	public void testSet() {
		DynamicArray da = new DynamicArray(1000);

		for (int i = 0; i < 1000; i++) {
			da.add(i);
		}

		for (int i = 1000, k = 0; i > 0; i--, k++) {
			Assert.assertEquals(k, (int) da.get(k));
			da.set(k, i);
			Assert.assertEquals(i, (int) da.get(k));
		}

		Assert.assertEquals(1000, da.size());
	}

	/**
	 * Requires constructor DynamicArray(int...) to work
	 */
	@Test(timeout = 1000)
	public void testGet() {
		DynamicArray da = new DynamicArray(5, 2, 1);
		Assert.assertEquals(5, (int) da.get(0));
		Assert.assertEquals(2, (int) da.get(1));
		Assert.assertEquals(1, (int) da.get(2));
	}

	/**
	 * Requires constructor DynmaicArray(int...) to work
	 */
	@Test(timeout = 1000)
	public void testIndexOf(){
		DynamicArray da = new DynamicArray(3, 5, 2, 0);
		Assert.assertEquals(0, da.indexOf(3));
		Assert.assertEquals(2, da.indexOf(2));
		Assert.assertEquals(-1, da.indexOf(42));
	}

	/**
	 * Requires constructor DynmaicArray(int...) to work
	 */
	@Test(timeout = 1000)
	public void testLastIndexOf(){
		DynamicArray da = new DynamicArray(3, 5, 2, 0);
		Assert.assertEquals(0, da.lastIndexOf(3));
		Assert.assertEquals(2, da.lastIndexOf(2));
		Assert.assertEquals(-1, da.lastIndexOf(42));

		da = new DynamicArray(3,5,4,3,2,0,5);

		Assert.assertEquals(3, da.lastIndexOf(3));
		Assert.assertEquals(6, da.lastIndexOf(5));
		Assert.assertEquals(-1, da.lastIndexOf(42));
	}

	/**
	 * Requires constructor DynmaicArray(int...) to work
	 */
	@Test(timeout = 1000)
	public void testContains(){
		DynamicArray da = new DynamicArray(3, 5, 2, 0);
		Assert.assertTrue(da.contains(3));
		Assert.assertTrue(da.contains(5));
		Assert.assertTrue(da.contains(2));
		Assert.assertTrue(da.contains(0));
		Assert.assertFalse(da.contains(42));
	}

	/**
	 * Requires constructor DynamicArray(int...) to work
	 */
	@Test(timeout = 1000)
	public void testSize() {
		DynamicArray da = new DynamicArray(5, 2, 1);
		Assert.assertEquals(3, da.size());
	}

	/**
	 * Requires constructors DynamicArray(),  DynamicArray(int...) to work
	 */
	@Test(timeout = 1000)
	public void testIsEmpty() {
		DynamicArray da = new DynamicArray(5, 2, 1);
		Assert.assertFalse(da.isEmpty());

		da = new DynamicArray();
		Assert.assertTrue(da.isEmpty());
	}

	/**
	 * Requires constructors DynamicArray(int...) to work
	 * Requires method isEmpty(), size() to work
	 */
	@Test(timeout = 1000)
	public void testClear() {
		DynamicArray da = new DynamicArray(5, 2, 1);
		Assert.assertFalse(da.isEmpty());

		da.clear();

		Assert.assertEquals(0, da.size());
		Assert.assertTrue(da.isEmpty());
	}


	/**
	 * Requires constructors DynamicArray(int...) to work
	 * Requires method size() to work
	 */
	@Test(timeout = 1000)
	public void testRemove() {
		DynamicArray da = new DynamicArray(5, 2, 1);

		Assert.assertEquals(5, (int) da.remove(0));
		Assert.assertEquals(2, da.size());
		Assert.assertEquals(1, (int) da.remove(1));
		Assert.assertEquals(1, da.size());
	}

	/**
	 * Requires constructor DynamicArray(int...) to work
	 * Requires method size() to work
	 */
	@Test(timeout = 1000)
	public void testRemove2() {
		DynamicArray da = new DynamicArray(5, 2, 1);

		Assert.assertTrue(da.remove((Integer) 5));
		Assert.assertTrue(da.remove((Integer) 1));
		Assert.assertFalse(da.remove((Integer) 42));
		Assert.assertTrue(da.remove((Integer) 2));
		Assert.assertFalse(da.remove((Integer) 2));
	}

	/**
	 * Require constructor DynamicArray(int...) to work
	 */
	@Test(timeout = 1000)
	public void testIterator(){
		int[] test = {1,5,7,3};

		DynamicArray<Integer> da = new DynamicArray<Integer>(1,5,7,3);

		int i = 0;
		for(int n : da){
			Assert.assertEquals(test[i++], n);
		}

		Assert.assertEquals(4, i);
	}

	//Testing the exception cases

	/**
	 * Requires DynamicArray(int...) to work
	 */
	@Test(timeout = 1000, expected = IndexOutOfBoundsException.class)
	public void testAddException1(){
		DynamicArray da = new DynamicArray(42, 3, 27);
		da.add(-1, 5);
	}

	/**
	 * Requires DynamicArray(int...) to work
	 */
	@Test(timeout = 1000, expected = IndexOutOfBoundsException.class)
	public void testAddException2(){
		DynamicArray da = new DynamicArray(42, 3, 27);
		da.add(5, 5);
	}

	/**
	 * Requires DynamicArray(int...) to work
	 */
	@Test(timeout = 1000, expected = IndexOutOfBoundsException.class)
	public void testSetException1(){
		DynamicArray da = new DynamicArray(42, 3, 27);
		da.set(-1, 5);
	}

	/**
	 * Requires DynamicArray(int...) to work
	 */
	@Test(timeout = 1000, expected = IndexOutOfBoundsException.class)
	public void testSetException2(){
		DynamicArray da = new DynamicArray(42, 3, 27);
		da.set(5, 5);
	}


	/**
	 * Requires DynamicArray(int...) to work
	 */
	@Test(timeout = 1000, expected = IndexOutOfBoundsException.class)
	public void testGetException1(){
		DynamicArray da = new DynamicArray(42, 3, 27);
		da.get(-1);
	}

	/**
	 * Requires DynamicArray(int...) to work
	 */
	@Test(timeout = 1000, expected = IndexOutOfBoundsException.class)
	public void testGetException2(){
		DynamicArray da = new DynamicArray(42, 3, 27);
		da.get(5);
	}

	/**
	 * Requires DynamicArray(int...) to work
	 */
	@Test(timeout = 1000, expected = IndexOutOfBoundsException.class)
	public void testRemoveException1(){
		DynamicArray da = new DynamicArray(42, 3, 27);
		da.remove(-1);
	}

	/**
	 * Requires DynamicArray(int...) to work
	 */
	@Test(timeout = 1000, expected = IndexOutOfBoundsException.class)
	public void testRemoveException2(){
		DynamicArray da = new DynamicArray(42, 3, 27);
		da.remove(5);
	}

	@Test(timeout = 1000)
	public void testMutate(){
		DynamicArray<Integer> da = new DynamicArray<>(42, 3, 27);
		DynamicArray<Integer> expected =  new DynamicArray<>(84, 6, 54);
		da.mutate(x -> (x*2));
		Assert.assertEquals(expected.get(0), da.get(0));
		Assert.assertEquals(expected.get(1), da.get(1));
		Assert.assertEquals(expected.get(2), da.get(2));
	}

	@Test(timeout=1000)
	public void testListCTor(){
		List<Integer> SUT = new List<>(2, 5, 7);
		Assert.assertEquals("2, 5, 7", SUT.toString());
	}

	@Test(timeout = 1000)
	public void testListPrepend(){
		List<Integer> SUT = new List<>(5, 7);

		SUT.Prepend(2);

		Assert.assertEquals("2, 5, 7", SUT.toString());
	}

	@Test(timeout = 1000)
	public void testListAppend(){
		List<Integer> SUT = new List<>(2, 5);

		SUT.Append(7);

		Assert.assertEquals("2, 5, 7", SUT.toString());
	}

	@Test(timeout = 1000)
	public void testListSize(){
		List<Integer> SUT = new List<>(2, 5, 7);

		Assert.assertEquals(3, SUT.Size());
	}

	@Test(timeout = 1000)
	public void testListInsertFront(){
		List<Integer> SUT = new List<>(2, 5, 7);

		SUT.Insert(-3, 0);

		Assert.assertEquals("0, 2, 5, 7", SUT.toString());
	}

	@Test(timeout = 1000)
	public void testListInsertMiddle(){
		List<Integer> SUT = new List<>(2, 5, 7);

		SUT.Insert(1, 0);

		Assert.assertEquals("2, 0, 5, 7", SUT.toString());
	}

	@Test(timeout = 1000)
	public void testListInsertBack(){
		List<Integer> SUT = new List<>(2, 5, 7);

		SUT.Insert(12, 0);

		Assert.assertEquals("2, 5, 7, 0", SUT.toString());
	}

	@Test(timeout = 1000)
	public void testListGet(){
		List<Integer> SUT = new List<>(2, 5, 7);
		Integer expected = 5;

		Assert.assertEquals(expected, SUT.Get(1));
	}
}
