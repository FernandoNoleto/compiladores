package sample;


import javax.swing.*;

public class Main{

    public static void main(String[] args) {
        JFrame frame = new JFrame("First Follow");
        frame.setLocationRelativeTo(null);
        frame.setContentPane(new FirstFollowGUI().panelMain);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }
}
