package eidi2.sose25.nachname.vorname.sheet06.ex02;

import java.util.HashMap;
import java.util.Optional;

public class GradeOverview {
	private final HashMap<String, Pair<Double, Integer>> GRADEOVERVIEW = new HashMap<>();
	
	public void addTestResult(String lectureName, Pair<Double, Integer> gradeAndECTS) {
		// ToDo a)
	}
	
	public int currentECTS() {
		// ToDo b)
		return 0;
	}
	
	public Optional<Pair<Double, Integer>> getExamResult(String lectureName) {
		// ToDo c)
		return Optional.empty();
	}
	
	public double totalGradeAverage() {
		// ToDo d)
		return 0;
	}
}
