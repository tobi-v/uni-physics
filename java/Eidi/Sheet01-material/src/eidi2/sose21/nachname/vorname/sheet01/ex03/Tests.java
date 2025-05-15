package eidi2.sose21.nachname.vorname.sheet01.ex03;

import org.junit.Test;
import org.junit.Assert;

public class Tests {

	@Test
	public void testValuedConstructor() {
		DynamicArray array = new DynamicArray(5, 4, 3, 2, 1);	
		
		Assert.assertEquals(array.get(0), 5);
	}
	
	@Test
	public void testAdd() {
		DynamicArray array = init();
		
		Assert.assertEquals(array.size(), 10);
		Assert.assertEquals(array.get(0), 1);
		Assert.assertEquals(array.get(3), 4);
	}
	
	@Test
	public void testResize() {
		DynamicArray array = init();
		
		Assert.assertEquals(array.size(), 10);	
		
		array.resize(5);		
		Assert.assertEquals(array.get(4), 5);
		Assert.assertEquals(array.size(), 5);	
		
		array.resize(10);
		Assert.assertEquals(array.size(), 10);		
	}	
	
	@Test
	public void testRemove() {
		DynamicArray array = init();
		
		array.remove(4);
		Assert.assertEquals(array.get(4), 6);
		Assert.assertEquals(array.size(), 9);
	}	
	
	@Test(expected = IllegalArgumentException.class)
	public void testResizeException() {
		DynamicArray array = init();
		
		array.resize(-1);
	}
	
	@Test(expected = ArrayIndexOutOfBoundsException.class)
	public void testRemoveException1() {
		DynamicArray array = init();
		
		array.remove(-1);
	}
	
	@Test(expected = ArrayIndexOutOfBoundsException.class)
	public void testRemoveException2() {
		DynamicArray array = init();
		
		array.remove(10);
	}
	
	
	@Test(expected = ArrayIndexOutOfBoundsException.class)
	public void testGetException1() {
		DynamicArray array = init();
		
		array.get(-1);
	}
	
	@Test(expected = ArrayIndexOutOfBoundsException.class)
	public void testGetException2() {
		DynamicArray array = init();
		
		array.get(10);
	}
	
	private static DynamicArray init() {
		DynamicArray array = new DynamicArray();
		for(int i = 0; i < 10; i++) {
			array.add(i+1);
		}
		
		return array;
	}
}