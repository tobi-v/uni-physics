package org.example;

public class Stack<T> implements BetterStack<T> {

    java.util.Stack<T> innerStack = new java.util.Stack<>();

    @Override
    public BetterStack<T> push(T item) {
        innerStack.push(item);
        return this;
    }

    @Override
    public T peek() {
        return innerStack.peek();
    }

    @Override
    public T pop() {
        return innerStack.pop();
    }

    @Override
    public Integer size() {
        return innerStack.size();
    }

    @Override
    public boolean empty() {
        return innerStack.empty();
    }
}
