package days.day3.star1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Star1 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new File("src/main/java/days/day3/input.txt"));
        StringBuilder binaryGamma = new StringBuilder();
        StringBuilder binaryEpsilon = new StringBuilder();
        String line1 = sc.nextLine();
        int zeroCount = 0;
        int oneCount = 0;
        for(int i = 0 ; i < line1.length(); i++ ){
            Scanner scLoop = new Scanner(new File("src/main/java/days/day3/input.txt"));
            while(scLoop.hasNextLine()) {
                String line = scLoop.nextLine();
                char ch = line.charAt(i);
                if (ch == '0') {
                    zeroCount += 1;
                } else {
                    oneCount += 1;
                }
            }
            if(zeroCount > oneCount){
                binaryGamma.append(0);
                binaryEpsilon.append(1);
            }else{
                binaryGamma.append(1);
                binaryEpsilon.append(0);
            }
            zeroCount = 0;
            oneCount = 0;
        }
        System.out.println(binaryGamma);
        int gamma = Integer.parseInt(String.valueOf(binaryGamma),2);

        System.out.println(binaryEpsilon);
        int epsilon = Integer.parseInt(String.valueOf(binaryEpsilon), 2);
        System.out.println(gamma);
        System.out.println(epsilon);
        System.out.println(gamma * epsilon);
    }
}
