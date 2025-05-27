package eidi2.sose25.nachname.vorname.sheet02.ex01;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.Arrays;

// Listens for Actions (on Buttons in our case) and executes an operation based on Action
public class CalculatorCtrl implements ActionListener {

    private Boolean currentNumberHasDot = false;
    private Boolean waitingForNextNumber = false;
    private String currentOperation = null;
    private ArrayList<Object>[] expression;
    private Double operand1;
    private Double operand2;

    private final String[] appendable = {"7", "8", "9",
                                    "4", "5", "6",
                                    "1", "2", "3",
                                    "0", "."};
    private final String[] operations = {"/", "*", "-", "+",};

    private void evaluate() {
        operand2 = Double.parseDouble(Calculator.getContent());
        switch(currentOperation){
            case "+":
                Calculator.setContent(operand1 + operand2); break;
            case "*":
                Calculator.setContent(operand1 * operand2); break;
            case "-":
                Calculator.setContent(operand1 - operand2); break;
            case "/":
                Calculator.setContent(operand1 / operand2);
        }
        operand1 = Double.parseDouble(Calculator.getContent());
    }

    @Override
    public void actionPerformed(ActionEvent actionEvent) {
        // Retrieves action command contained in Event
        String cmd = actionEvent.getActionCommand();

            if(Arrays.asList(appendable).contains(cmd)){
                if(waitingForNextNumber){
                    Calculator.setContent("");
                    System.out.println("Set waitingfornextnumber to false");
                    waitingForNextNumber = false;
                }
                if(cmd.equals("."))
                    if(currentNumberHasDot) return;
                    else currentNumberHasDot = true;
                Calculator.setContent(Calculator.getContent() + cmd);
            }
            else if(Arrays.asList(operations).contains(cmd)){
                if(!waitingForNextNumber && currentOperation != null){

                }
                waitingForNextNumber = true;
                System.out.println("Set watingfornumber true");
                operand1 = Double.parseDouble(Calculator.getContent());
                currentNumberHasDot = false;
                currentOperation = cmd;
            }
            else if(cmd.equals("=")){
                if(currentOperation == null)
                    return;
                evaluate();
                currentOperation = null;
            }
    }

    private void AddNumberToExpression(String number){
    }

    private void AddOperationToExpression(String operation){

    }
}
