package days.day3.star2;

import javax.management.ObjectName;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Star2 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new File("src/main/java/days/day3/input.txt"));

        ArrayList<String> binaryList = new ArrayList<>();

        String oxygenValue;
        String co2scrubber;
        int length;

        while(sc.hasNextLine()){
            binaryList.add(sc.nextLine());
        }
        length = binaryList.get(0).length();

        for(int i = 0 ; i < length ; i++){
            int zeroCount = 0;
            int oneCount = 0;
            ArrayList<String> zeroList = new ArrayList<>();
            ArrayList<String> oneList = new ArrayList<>();
            for(String line : binaryList){
                if(line.charAt(i) == '0'){
                    zeroCount += 1;
                    zeroList.add(line);
                }else{
                    oneCount += 1;
                    oneList.add(line);
                }
            }
            if(oneCount >= zeroCount){
                binaryList.removeAll(zeroList);
            }else{
                binaryList.removeAll(oneList);
            }
        }
        System.out.println(binaryList);
        oxygenValue = binaryList.get(0);

        binaryList.clear();

        Scanner sc2 = new Scanner(new File("src/main/java/days/day3/input.txt"));
        while(sc2.hasNextLine()){
            binaryList.add(sc2.nextLine());
        }


        for(int i = 0 ; i < length ; i++){
            int zeroCount = 0;
            int oneCount = 0;
            ArrayList<String> zeroList = new ArrayList<>();
            ArrayList<String> oneList = new ArrayList<>();
            for(String line : binaryList){
                if(line.charAt(i) == '0'){
                    zeroCount += 1;
                    zeroList.add(line);
                }else{
                    oneCount += 1;
                    oneList.add(line);
                }
            }
            if(binaryList.size() == 1){
                break;
            }
            if(zeroCount <= oneCount){
                binaryList.removeAll(oneList);
            }else{
                binaryList.removeAll(zeroList);
            }
        }
        System.out.println(binaryList);
        co2scrubber = binaryList.get(0);

        System.out.println(oxygenValue);
        int gamma = Integer.parseInt(String.valueOf(oxygenValue),2);

        System.out.println(co2scrubber);
        int epsilon = Integer.parseInt(String.valueOf(co2scrubber), 2);
        System.out.println(gamma);
        System.out.println(epsilon);
        System.out.println(gamma * epsilon);
    }
}
