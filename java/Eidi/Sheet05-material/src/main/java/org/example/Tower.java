package org.example;

public class Tower extends OrderedStack<Disc> {
  @Override
  public String toString(){
    return "Topmost disc size: " + peek().toString();
  }
}
