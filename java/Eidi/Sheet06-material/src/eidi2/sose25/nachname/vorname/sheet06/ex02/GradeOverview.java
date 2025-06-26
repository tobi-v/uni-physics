package eidi2.sose25.nachname.vorname.sheet06.ex02;

import java.util.HashMap;
import java.util.Optional;

public class GradeOverview {
	private final HashMap<String, Pair<Double, Integer>> GRADEOVERVIEW = new HashMap<>();
	
	public void addTestResult(String lectureName, Pair<Double, Integer> gradeAndECTS) {
		GRADEOVERVIEW.put(lectureName, gradeAndECTS);
	}
	
	public int currentECTS() {
		int accumulatedECTS = 0;
		for(Pair<Double, Integer> p : GRADEOVERVIEW.values())
			accumulatedECTS += p.second;
		return accumulatedECTS;
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
