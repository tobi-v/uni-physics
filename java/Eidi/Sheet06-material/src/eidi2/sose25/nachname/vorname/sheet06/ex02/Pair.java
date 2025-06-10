package eidi2.sose25.nachname.vorname.sheet06.ex02;

public class Pair<F, S> {
	F first;
	S second;
	
	public static<F,S> Pair<F,S> of(F first, S second) {
		Pair<F,S> pair = new Pair<>();
		pair.first = first;
		pair.second = second;
		return pair;
	}
}
