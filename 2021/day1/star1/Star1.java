package days.day1.star1;

import java.io.*;
import java.util.Scanner;

public class Star1 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(new File("src/main/java/days/day1/input.txt"));
        int total = 0;
        int previous = Integer.parseInt(sc.nextLine());
        while(sc.hasNextLine()) {
            int line = Integer.parseInt(sc.nextLine());
            if (line > previous){
                total += 1;
                System.out.println(line + " > " + previous);
                System.out.println(total);
            }
            previous = line;
        }
        System.out.println(total);
    }
}
