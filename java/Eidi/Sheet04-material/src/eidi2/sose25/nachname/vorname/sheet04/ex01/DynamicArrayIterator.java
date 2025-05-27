package eidi2.sose25.nachname.vorname.sheet04.ex01;

import java.util.Iterator;

public class DynamicArrayIterator implements Iterator<Integer> {

    private DynamicArray da;
    int index = 0;

    public DynamicArrayIterator(DynamicArray da) {
        this.da = da;
    }

    @Override
    public boolean hasNext() {
        return index < da.size();
    }

    @Override
    public Integer next() {
        return da.get(index++);
    }
}
