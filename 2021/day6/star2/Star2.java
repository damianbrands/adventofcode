package days.day6.star2;

import days.day6.star1.School;

import java.io.File;
import java.io.FileNotFoundException;
import java.lang.reflect.Array;
import java.util.*;

public class Star2 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new File("src/main/java/days/day6/input.txt"));

        String[] fish = sc.nextLine().split(",");
        int[] internalTimers = new int[fish.length];
        for (int i = 0; i < fish.length; i++) {
            internalTimers[i] = Integer.parseInt(fish[i]);
        }

        Arrays.sort(internalTimers);

        int [] fr = new int [internalTimers.length];
        int visited = -1;

        for(int i = 0; i < internalTimers.length; i++){
            int count = 1;
            for(int j = i+1; j < internalTimers.length; j++){
                if(internalTimers[i] == internalTimers[j]){
                    count++;
                    fr[j] = visited;
                }
            }
            if(fr[i] != visited)
                fr[i] = count;
        }

        ArrayList<Integer> newfr = new ArrayList<>();

        for(int i : fr){
            if(!(i == -1)){
                newfr.add(i);
            }
        }

        School2 school = new School2(0, newfr.get(0), newfr.get(1), newfr.get(2), newfr.get(3), newfr.get(4),0, 0, 0);

        for(int i = 0; i < 257; i++){
            System.out.println("\nAfter " + i + " days:");
            System.out.println("Total amount of fish: " + school.getTotalFish());
            school.newDay();
        }
    }
}
