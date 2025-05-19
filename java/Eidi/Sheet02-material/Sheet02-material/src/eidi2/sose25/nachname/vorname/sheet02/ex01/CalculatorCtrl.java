package eidi2.sose25.nachname.vorname.sheet02.ex01;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Arrays;

// Listens for Actions (on Buttons in our case) and executes an operation based on Action
public class CalculatorCtrl implements ActionListener {

    Boolean currentNumberHasDot = false;
    Boolean waitingForNextNumber = false;

    private String[] appendable = {"7", "8", "9",
                                    "4", "5", "6",
                                    "1", "2", "3",
                                    "0", "."};
    private String[] operations = {"/", "*", "-", "*",};

    @Override
    public void actionPerformed(ActionEvent actionEvent) {
        // Retrieves action command contained in Event
        String cmd = actionEvent.getActionCommand();

            if(Arrays.stream(appendable).anyMatch(cmd::equals)){
                if(cmd == ".")
                    if(currentNumberHasDot) return;
                    else currentNumberHasDot = true;
                Calculator.setContent(Calculator.getContent() + cmd);
            }
            else if(Arrays.stream(operations).anyMatch(cmd::equals)){
                waitingForNextNumber = true;
//        System.out.println("You clicked the GUI element with ActionCommand: " + cmd);
//
//        Calculator.setContent("Clicks: " + n);
    }
}
