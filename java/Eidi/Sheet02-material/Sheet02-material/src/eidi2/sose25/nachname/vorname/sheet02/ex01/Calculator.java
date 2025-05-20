package eidi2.sose25.nachname.vorname.sheet02.ex01;

import java.awt.Dimension;
import java.awt.BorderLayout;
import java.awt.Font;
import java.awt.GridLayout;

import javax.swing.*;


public class Calculator {

	// Names of all buttons on a basic calculator
	private final static String[] BUTTON_NAMES = {"(", ")", "Undo", "Clear", "7", "8", "9", "/", "4", "5", "6", "x", "1", "2", "3", "-", "0", ".", "=", "+"};
	
    private static JTextField output = null;

    public static void main(String[] args) {

        createGui();
    }

    private static void createGui() {

    	// Button Actions Controller
        CalculatorCtrl ctrl = new CalculatorCtrl();

        // Calculator window
        JFrame frame = new JFrame("Calculator");

        // "Default" Settings for window
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);// exit Application on window close
        frame.setPreferredSize(new Dimension(480, 640));// set size of window
        frame.setResizable(false);// prevent window from being resized
        frame.getContentPane().setLayout(new BorderLayout());// use BorderLayout as TopLevel layout for window

        // Create and add "display-area" of calculator
        output = new JTextField("0");
        output.setEditable(false);// prevent area from being edited
        output.setFont(new Font("Arial", Font.BOLD, 32));
        output.setHorizontalAlignment(SwingConstants.RIGHT);// align text within display-area to the right
        // add display-area to top row of BorderLayout in window
        frame.getContentPane().add(output, BorderLayout.NORTH);

        // Create and fill panel for calculator buttons
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(5, 4));

        //Replace all code from here
        // Create Button with functionality
        String[] buttonNames = {
            "{", "}", "Undo", "Clear",
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "*",
        };
        for(int ii = 0; ii < buttonNames.length; ii++){
            JButton button = new JButton(buttonNames[ii]);
            button.addActionListener(ctrl);
            button.setActionCommand(buttonNames[ii]);
            panel.add(button);
        }
        
        // Add button area to BorderPane of window
        frame.getContentPane().add(panel);

        // Start window
        frame.pack();
        frame.setVisible(true);

    }

    public static void setContent(double value){
        if((int) value == value){
            output.setText(""+(int) value);
        }else{
            output.setText(""+value);
        }
    }
    
    public static void setContent(String value){
        output.setText(value);
    }
}
