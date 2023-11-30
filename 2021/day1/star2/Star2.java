package days.day1.star2;

import java.io.*;
import java.util.Scanner;

public class Star2 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(new File("src/main/java/days/day1/input.txt"));
        int total = 0;
        int number1 = 0;
        int number2 = 0;
        int number3 = 0;
        while(sc.hasNextLine()) {
            int number4 = Integer.parseInt(sc.nextLine());
            if((number4 + number3 + number2) > (number3 + number2 + number1) && number1 != 0){
                total += 1;
            }
            number1 = number2;
            number2 = number3;
            number3 = number4;
        }
        System.out.println(total);
    }
}