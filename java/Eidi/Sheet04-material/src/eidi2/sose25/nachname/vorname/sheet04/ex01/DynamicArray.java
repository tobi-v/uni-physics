package eidi2.sose25.nachname.vorname.sheet04.ex01;

import java.util.Iterator;

public class DynamicArray implements UniList<Integer> {

    private int nextFree = 0;
    private int[] array;

    //constructors
    public DynamicArray() {
        array = new int[10];
    }

    public DynamicArray(int n) {
        array = new int[n];
    }

    public DynamicArray(int... values) {
        array = new int[values.length];

        System.arraycopy(values, 0, array, 0, values.length);
        nextFree = values.length;
    }

    //implementation of methods from UniList<Integer>
    @Override
    public boolean add(Integer value) {

        if (nextFree >= array.length) {
            resize(Math.max(array.length * 2, 1));
        }

        array[nextFree++] = value;

        return true;
    }

    @Override
    public void add(int index, Integer value) {
        if (index < 0 || index > size()) {
            throw new IndexOutOfBoundsException();
        }

        if (index == nextFree) {
            //also catches the case of an empty dynamic array
            add(value);
        } else {
            int last = array[nextFree - 1];
            for (int i = nextFree - 1; i > index; i--) {
                array[i] = array[i - 1];
            }
            array[index] = value;
            add(last);
        }
    }


    @Override
    public Integer set(int index, Integer value) {
        if (index < 0 || index >= size()) {
            throw new IndexOutOfBoundsException();
        }

        Integer old = array[index];
        array[index] = value;

        return old;
    }

    @Override
    public Integer get(int index) {
        if (index < 0 || index >= size()) {
            throw new IndexOutOfBoundsException();
        }

        return array[index];
    }

    @Override
    public int indexOf(Integer value) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == value) {
                return i;
            }
        }

        return -1;
    }

    @Override
    public int lastIndexOf(Integer value) {
        int index = -1;

        for (int i = 0; i < array.length; i++) {
            if (array[i] == value) {
                index = i;
            }
        }

        return index;
    }

    @Override
    public boolean contains(Integer value) {
        for (int x : array) {
            if (x == value) {
                return true;
            }
        }

        return false;
    }

    @Override
    public int size() {
        return nextFree;
    }

    @Override
    public boolean isEmpty() {
        return nextFree == 0;
    }


    @Override
    public void clear() {
        nextFree = 0;
    }

    @Override
    public Integer remove(int index) {
        if (index < 0 || index >= nextFree) {
            throw new ArrayIndexOutOfBoundsException();
        }

        Integer old = array[index];

        for (int i = index; i < nextFree - 1; i++) {
            array[i] = array[i + 1];
        }

        array[nextFree - 1] = 0;
        nextFree--;

        return old;
    }

    @Override
    public boolean remove(Integer value) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == value) {
                remove(i);
                return true;
            }
        }

        return false;
    }

    @Override
    public Iterator<Integer> iterator() {
        return new DynamicArrayIterator(this);
    }

    //helper methods
    public void resize(int newLength) {

        if (newLength < 0) {
            throw new IllegalArgumentException("newLength < 0");
        }

        int[] newArray = new int[newLength];

        for (int i = 0; i < Math.min(nextFree, newArray.length); i++) {
            newArray[i] = array[i];
        }

        nextFree = Math.min(nextFree, newArray.length);
        array = newArray;
    }

    //Object method overrides
    @Override
    public String toString() {

        StringBuilder sb = new StringBuilder();

        sb.append("[");

        for (int i = 0; i < size(); i++) {
            sb.append(array[i]);

            if (i < size() - 1) {
                sb.append(", ");
            }
        }

        sb.append("]");

        return new String(sb);
    }
}