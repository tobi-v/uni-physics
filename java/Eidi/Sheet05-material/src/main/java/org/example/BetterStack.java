package org.example;

public interface BetterStack<T> {
    BetterStack<T> push(T item);

    T peek();
    T pop();

    Integer size();

    boolean empty();
}
