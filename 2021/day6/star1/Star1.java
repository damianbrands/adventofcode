package days.day6.star1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;

public class Star1 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new File("src/main/java/days/day6/input.txt"));
        School school = new School();
        String[] fish = sc.nextLine().split(",");
        int[] internalTimers = new int[fish.length];
        for (int i = 0; i < fish.length; i++) {
            internalTimers[i] = Integer.parseInt(fish[i]);
        }
        Arrays.sort(internalTimers);
        for(int internalTimer : internalTimers){
            school.oldFish(internalTimer);
        }

        for(int i = 0; i < 81; i++){
            System.out.println("\nAfter " + i + " days:");
            System.out.println("Totaal aantal vissen: " + school.lanternfishList.size());
//            System.out.println(school.lanternfishList);
            school.newDay();
        }
    }
}
