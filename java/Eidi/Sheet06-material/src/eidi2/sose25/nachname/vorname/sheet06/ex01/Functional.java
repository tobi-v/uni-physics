package eidi2.sose25.nachname.vorname.sheet06.ex01;

import java.util.function.BiFunction;
import java.util.function.UnaryOperator;

public interface Functional<T> {

	/**
	 * Replace each element "t" with the result of f.apply(t).
	 * @param f The function to apply on each element.
	 */
	void mutate(UnaryOperator<T> f);
	
	/**
	 * Combine all elements using the function f.
	 * @param <R> Type of the return value.
	 * @param f The function used to combine all elements.
	 * 		    It is applied to an element "t" and the result of a previous application "r" using f.apply(t,r).
	 * @param initial The initial value used for the first application of f or as the result for an empty data structure.
	 *        It can also serve as an accumulator for recursive calls.
	 * @return
	 */
	<R> R flat(BiFunction<T, R, R> f, R initial);	
}
