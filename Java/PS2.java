package Java;
/*
There are three lines of input:

        The first line contains an integer.
        The second line contains a double.
        The third line contains a String.
*/
import java.util.Scanner;

public class PS2 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();

        // Write your code here.
        double d = scan.nextDouble();
        scan.nextLine();
        String s = scan.nextLine();
        scan.close();

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}