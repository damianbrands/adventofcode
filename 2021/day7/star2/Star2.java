package days.day7.star2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class Star2 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new File("src/main/java/days/day7/input.txt"));
        String[] scn = sc.nextLine().split(",");
        int[] crabs = new int[scn.length];
        for (int i = 0; i < scn.length; i++) {
            crabs[i] = Integer.parseInt(scn[i]);
        }
        System.out.println(Arrays.toString(crabs));


        int sum = 0;
        for(int crab : crabs){
            sum += crab;
        }
        int avg = sum / (crabs.length);
        int fuelFinal = 999999999;

        for(int i = (avg - 250); i < (avg + 250); i++){
            int fuel = 0;
            for (int crab : crabs) {
                int distance = Math.abs(crab - i);
                int fuelSum = 0;
                for(int i2 = 0; i2 < distance; i2++){
                    fuelSum += i2 + 1;
                }
                fuel += fuelSum;
            }
            if(fuel < fuelFinal){
                fuelFinal = fuel;
            }
        }
        System.out.println(avg);
        System.out.println(fuelFinal);
    }
}
