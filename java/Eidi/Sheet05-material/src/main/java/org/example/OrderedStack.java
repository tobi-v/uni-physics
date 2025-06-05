package org.example;

public class OrderedStack<T extends Disc> extends Stack<T> {
    @Override
    public BetterStack<T> push(T item){
        if(empty()){innerStack.push(item);}
        else if(item.compareTo(innerStack.peek()) > 0){ throw new IllegalStateException();}
        innerStack.push(item);
        return this;
    }
}
