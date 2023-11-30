package days.day2.star1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Star1 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new File("src/main/java/days/dag2/input.txt"));
        int horizontalPos = 0;
        int depth = 0;
        int aim = 0;
        while(sc.hasNextLine()) {
            String[] line = sc.nextLine().split(" ");
            if(line[0].equals("forward")){
                horizontalPos += Integer.parseInt(line[1]);
                depth += aim * Integer.parseInt(line[1]);
            }
            if(line[0].equals("down")){
                aim += Integer.parseInt(line[1]);
            }
            if(line[0].equals("up")){
                aim -= Integer.parseInt(line[1]);
            }
        }
        System.out.println(horizontalPos);
        System.out.println(depth);
        System.out.println(horizontalPos * depth);
    }
}
