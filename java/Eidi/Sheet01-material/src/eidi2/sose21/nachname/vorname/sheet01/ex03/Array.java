package eidi2.sose21.nachname.vorname.sheet01.ex03;

public abstract class Array{
    protected int[] array;
    protected int firstFreeIdx;

    public Array(int length){
        array = new int[length];
        firstFreeIdx = 0;
    }
    
    public void add(int val) {
        if(firstFreeIdx >= array.length)
            throw new ArrayIndexOutOfBoundsException();
        array[firstFreeIdx++] = val;
    }

    public int size() {
        return array.length;
    }

    public int get(int index) {
        if(index >= firstFreeIdx)
            throw new ArrayIndexOutOfBoundsException();
        return array[index];
    }

    public void remove(int index) {
        if(index >= firstFreeIdx)
            throw new ArrayIndexOutOfBoundsException();

        for(int ii = index; ii < firstFreeIdx-1; ii++)
            array[ii] = array[ii+1];
        array[--firstFreeIdx] = 0;
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
