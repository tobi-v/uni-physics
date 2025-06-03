package eidi2.sose25.nachname.vorname.sheet04.ex01;

import java.util.Iterator;
import java.util.function.UnaryOperator;

public class DynamicArray<T> implements UniList<T> {

    private int nextFree = 0;
    private T[] array;

    //constructors
    // Laufzeit: O(1)
    public DynamicArray() {
        array = (T[]) new Object[10];
    }

    // Laufzeit: O(1)
    public DynamicArray(int n) {
        array = (T[]) new Object[n];
    }

    // Laufzeit: O(1)
    public DynamicArray(T... values) {
        array = (T[]) new Object[values.length];

        System.arraycopy(values, 0, array, 0, values.length);
        nextFree = values.length;
    }

    //implementation of methods from UniList<T>
    // Laufzeit: worst case O(resize) + 1
    @Override
    public boolean add(T value) {

        if (nextFree >= array.length) {
            resize(Math.max(array.length * 2, 1));
        }

        array[nextFree++] = value;

        return true;
    }

    // Laufzeit: worst case: O(n)
    @Override
    public void add(int index, T value) {
        if (index < 0 || index > size()) {
            throw new IndexOutOfBoundsException();
        }

        if (index == nextFree) {
            //also catches the case of an empty dynamic array
            add(value);
        } else {
            T last = array[nextFree - 1];
            for (int i = nextFree - 1; i > index; i--) {
                array[i] = array[i - 1];
            }
            array[index] = value;
            add(last);
        }
    }

    // Laufzeit: O(1)
    @Override
    public T set(int index, T value) {
        if (index < 0 || index >= size()) {
            throw new IndexOutOfBoundsException();
        }

        T old = array[index];
        array[index] = value;

        return old;
    }

    // Laufzeit: O(1)
    @Override
    public T get(int index) {
        if (index < 0 || index >= size()) {
            throw new IndexOutOfBoundsException();
        }

        return array[index];
    }

    // Laufzeit: O(n)
    @Override
    public int indexOf(T value) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == value) {
                return i;
            }
        }

        return -1;
    }

    // Laufzeit: O(n)
    @Override
    public int lastIndexOf(T value) {
        int index = -1;

        for (int i = 0; i < array.length; i++) {
            if (array[i] == value) {
                index = i;
            }
        }

        return index;
    }

    // Lauzeit: O(n)
    @Override
    public boolean contains(T value) {
        for (T x : array) {
            if (x == value) {
                return true;
            }
        }

        return false;
    }

    // Laufzeit: O(1)
    @Override
    public int size() {
        return nextFree;
    }

    // Laufzet: O(1)
    @Override
    public boolean isEmpty() {
        return nextFree == 0;
    }


    // Laufzeit: O(1)
    @Override
    public void clear() {
        nextFree = 0;
    }

    // Laufzeit: O(n)
    @Override
    public T remove(int index) {
        if (index < 0 || index >= nextFree) {
            throw new ArrayIndexOutOfBoundsException();
        }

        T old = array[index];

        for (int i = index; i < nextFree - 1; i++) {
            array[i] = array[i + 1];
        }

        array[nextFree - 1] = (T)null;
        nextFree--;

        return old;
    }

    // Laufzeit: O(n)
    @Override
    public boolean remove(T value) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == value) {
                remove(i);
                return true;
            }
        }

        return false;
    }

    // Laufzeit: O(1)
    @Override
    public Iterator<T> iterator() {
        return new DynamicArrayIterator<T>(this);
    }

    //helper methods
    // Laufzeit: O(n)
    public void resize(int newLength) {

        if (newLength < 0) {
            throw new IllegalArgumentException("newLength < 0");
        }

        T[] newArray = (T[]) new Object[newLength];

        for (int i = 0; i < Math.min(nextFree, newArray.length); i++) {
            newArray[i] = array[i];
        }

        nextFree = Math.min(nextFree, newArray.length);
        array = newArray;
    }

    //Object method overrides
    // Laufzeit: O(n)
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

    // Laufzeit: O(n)
    public void mutate(UnaryOperator<T> mutator){
        for (int ii=0; ii<size(); ii++){
            array[ii] = mutator.apply(array[ii]);
        }
    }
}