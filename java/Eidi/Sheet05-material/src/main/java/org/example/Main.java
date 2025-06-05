package eidi2_ex05;

import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		
		// Liste anlegen und mit Zufallswerten befüllen:
		List<SomethingNamed> myList = new ArrayList<>();
		for(int i=0; i<100; i++) {
			myList.add(new SomethingNamed((int)(Math.random()*100)));
		}

		System.out.println(myList);  // unsortiert ausgeben
		sort(myList);                // sortieren
		System.out.println(myList);  // sortiert ausgeben
	}

	private static <T extends Comparable<? super T>> void sort(List<T> myList) {
		for(int i=0; i<myList.size(); i++) {
			for(int j=i+1; j<myList.size(); j++) {
				// aufsteigend sortieren
				if(myList.get(i).compareTo(myList.get(j)) > 0) {
					T temp = myList.get(i);
					myList.set(i, myList.get(j));
					myList.set(j, temp);
				}
			}
		}
		
	}

}



 
