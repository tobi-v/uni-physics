
package eidi2.sose21.nachname.vorname.sheet01.ex03;

public class DynamicArray extends Array{
    
    private int dynamicAllocationSize = 20;

    public DynamicArray() {
        this(10);
    }

    public DynamicArray(int n) {
        super(n);
    }

    public DynamicArray(int... values) {
        super(values.length);
        array = values;
        firstFreeIdx = size() - 1;
    }

    @Override
    public void add(int val){
        if(firstFreeIdx >= size())
            resize(firstFreeIdx+dynamicAllocationSize);
        super.add(val);
    }

    @Override
    public void remove(int idx){
        super.remove(idx);        
        resize(size()-1);
    }

    public void resize(int newLength) {
        if(newLength < 0)
            throw new IllegalArgumentException();
        
        int oldLength = size();
        int[] oldArray = array.clone();
        array = new int[newLength];
        if(newLength > oldLength){
            for(int ii = 0; ii < oldLength; ii++)
                array[ii] = oldArray[ii];
            for(int ii = oldLength; ii < newLength; ii++)
                array[ii] = 0;
        } else{
            for(int ii = 0; ii < newLength; ii++)
                array[ii] = oldArray[ii];
            if (firstFreeIdx > newLength){
                firstFreeIdx = newLength;
            }
        }
    }
}