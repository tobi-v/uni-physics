package eidi2.sose25.nachname.vorname.sheet02.ex02;

public class DynamicArray{

    private int[] array;
    private int nextFree;

    public DynamicArray() {
        array = new int[10];

        nextFree = 0;
    }

    public DynamicArray(int n) {
        array = new int[n];
        nextFree = 0;
    }

    public DynamicArray(int... values) {

        if (values == null) {
            return;
        }

        array = new int[values.length];

        for (int i = 0; i < array.length; i++) {
            array[i] = values[i];
        }

        nextFree = array.length;
    }

    public void resize(int newLength) {

    	if(newLength < 0) {
    		throw new IllegalArgumentException("newLength < 0");
    	}
    	
        int[] newArray = new int[newLength];

        for (int i = 0; i < Math.min(nextFree, newArray.length); i++) {
            newArray[i] = array[i];
        }

        nextFree = Math.min(nextFree, newArray.length);
        array = newArray;
    }
    
    public void add(int val) {

        if (nextFree == array.length) {
            resize(array.length * 2);
        }

        array[nextFree++] = val;
    }
    
    public int size() {
        return nextFree;
    }
    
    public int get(int index) {

        if (index < 0 || index >= nextFree) {
            throw new ArrayIndexOutOfBoundsException();
        }

        return array[index];
    }

    public void remove(int index) {
        if (index < 0 || index >= nextFree) {
        	throw new ArrayIndexOutOfBoundsException();
        }

        for (int i = index; i < nextFree - 1; i++) {
            array[i] = array[i + 1];
        }

        array[nextFree - 1] = 0;
        nextFree--;
    }

    @Override
    public String toString() {

        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i < array.length; i++) {
            sb.append(array[i]);
            if (i != array.length - 1) {
                sb.append(", ");
            }
        }
        sb.append("]");

        return new String(sb);
    }
}