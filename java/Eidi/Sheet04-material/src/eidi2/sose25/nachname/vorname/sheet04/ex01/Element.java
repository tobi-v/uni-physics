package eidi2.sose25.nachname.vorname.sheet04.ex01;

public class Element<T> {
  private T _val;
  public Element<T> _next;

  public Element(T val){
    _val = val;
  }

  public Element(T val, Element<T> next){
    _val = val;
    _next = next;
  }

  public T GetValue(){
    return _val;
  }

  @Override
  public String toString() {
    return _val.toString();
  }
}
