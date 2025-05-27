package eidi2.sose25.nachname.vorname.sheet04.ex01;

import java.util.Iterator;


/**
 * Interface for the lecture EidI2 in the summer term of 2020.<br>
 *
 * This interface defines methods for unidirectional lists, mostly derived from <code>java.util.List<T></code>.
 * @author h3ssto
 *
 * @param <T>
 */
public interface UniList<T> extends Iterable<T>{

    boolean add(T value);

    void add(int index, T value);

    T set(int index, T value);

    T get(int index);

    int indexOf(T value);

    int lastIndexOf(T value);

    boolean contains(T value);

    int size();

    boolean isEmpty();

    void clear();

    T remove(int index);

    boolean remove(T value);

    @Override
    Iterator<T> iterator();
}
