package eidi2.sose25.nachname.vorname.sheet04.ex01;

import java.util.Iterator;

public class DynamicArrayIterator<T> implements Iterator<T> {

    private DynamicArray<T> da;
    int index = 0;

    public DynamicArrayIterator(DynamicArray<T> da) {
        this.da = da;
    }

    @Override
    public boolean hasNext() {
        return index < da.size();
    }

    @Override
    public T next() {
        return da.get(index++);
    }
}
