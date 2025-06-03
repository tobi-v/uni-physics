package eidi2.sose25.nachname.vorname.sheet04.ex01;

public class Element<T> {
  private T val;
  private Element<T> next;

  @Override
  public String toString() {
    return val.toString();
  }
}
