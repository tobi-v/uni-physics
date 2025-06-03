package eidi2.sose25.nachname.vorname.sheet04.ex01;

public class List<T> {
  private Element<T> first;
  private Element<T> last;
  private int size;

  public List(T... vals){
    for (T val : vals){
      Append(val);
    }
  }

  private void InitList(T val){
    first = new Element<>(val);
    last = first;
  }

  public void Prepend(T val){
    if (first == null){
      InitList(val);
    } else {
      Element<T> tmp = first;
      first = new Element<>(val, tmp);
    }
    size++;
  }

  public void Append(T val){
    if (first == null){
      InitList(val);
    } else {
      last._next = new Element<>(val);
      last = last._next;
    }
    size++;
  }

  public int Size(){
    return size;
  }

  public void Insert(int idx, T val){
    if(idx < 1){
      Prepend(val);
    } else if(idx > size){
      Append(val);
    } else{
      Element<T> current = first;
      for(int ii = 0; ii < idx-1 ; ii++){
        current = current._next;
      }
      Element<T> tmp = current._next;
      current._next = new Element<>(val, tmp);
    }
  }

  @Override
  public String toString(){
    Element<T> tmp = first;
    StringBuilder strb = new StringBuilder();
    while(tmp._next != null){
      strb.append(tmp.toString() + ", ");
      tmp = tmp._next;
    }
    strb.append(tmp.toString());
    return strb.toString();
  }
}
