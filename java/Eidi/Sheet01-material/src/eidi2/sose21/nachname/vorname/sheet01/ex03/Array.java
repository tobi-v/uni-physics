package eidi2.sose21.nachname.vorname.sheet01.ex03;

public abstract class Array{
    protected int[] array;
    
    public void add(int val) {
        // TODO b)
    }

    public int size() {
        // TODO c)
        return 0;
    }

    public int get(int index) {
        // TODO d)
        return 0;
    }

    public void remove(int index) {
        // TODO e)
        
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
