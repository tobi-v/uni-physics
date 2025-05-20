package eidi2.sose25.nachname.vorname.sheet02.ex01;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

// Listens for Actions (on Buttons in our case) and executes an operation based on Action
public class CalculatorCtrl implements ActionListener{
	
	int n = 0;
	
    @Override
    public void actionPerformed(ActionEvent actionEvent) {
    	// Retrieves action command contained in Event
        String cmd = actionEvent.getActionCommand();
        
        // Just some functionality, replace all this with actual calculator functionality 
        n++;
        System.out.println("You clicked the GUI element with ActionCommand: " + cmd);
        
        Calculator.setContent("Clicks: " + n);
    }
}
