package eidi2.sose21.nachname.vorname.sheet01.ex03;

public class Main {
    
   public static void main(String[] args) {
       
   }
   
   private static void wissenAnwenden() {
//     Array a = new Array(); //<- Fehler da Array eine Abstrakte Klasse ist und somit nicht erzeugt werden kann.
     Array b = new SimpleArray();
     Array c = new DynamicArray();
     DynamicArray d = new DynamicArray();
     System.out.println(b.size());
     System.out.println(c.size());
//     c.resize(100); //<- Fehler c ist vom Typ Array
     d.resize(100);
     ((DynamicArray) c).resize(100);//<- geht nachdem c zu DynamicArray gecastet wurde
     ((DynamicArray) b).resize(100);//<- ClassCastException, da b SimpleArray ist
   }

}
