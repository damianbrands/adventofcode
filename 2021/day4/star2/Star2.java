package days.day4.star2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Star2 {
    public static void main(String[] args) throws FileNotFoundException {
        Bingo2 bingo = new Bingo2();
        int round = 1;

        Scanner sc = new Scanner(new File("src/main/java/days/day4/input.txt"));
        String[] drawnNumbersString = sc.nextLine().split(",");
        int[] drawnNumbers = new int[drawnNumbersString.length];
        for (int i = 0; i < drawnNumbersString.length; i++) {
            drawnNumbers[i] = Integer.parseInt(drawnNumbersString[i]);
        }

        while(sc.hasNextLine()){
            sc.nextLine();
            int[] row1 = rowCreator(sc.nextLine());
            int[] row2 = rowCreator(sc.nextLine());
            int[] row3 = rowCreator(sc.nextLine());
            int[] row4 = rowCreator(sc.nextLine());
            int[] row5 = rowCreator(sc.nextLine());

            bingo.addBingoCard(row1, row2, row3, row4, row5);
        }

        int drawnNumbersLength = drawnNumbers.length;
        System.out.println(bingo);
        for (int drawnNumber : drawnNumbers) {
            System.out.println("\nRound: " + round);
            bingo.addDrawn(drawnNumber);
            bingo.checkBingo();
            round += 1;
        }
        System.out.println("End of bingo.");
    }

    public static int[] rowCreator(String numbers){
        if(numbers.startsWith(" ")){
            numbers = numbers.trim();
        }
        String [] nrStringList = numbers.split("\\s+");
        int[] rowIntList = new int[nrStringList.length];
        for (int i = 0; i < nrStringList.length; i++) {
            rowIntList[i] = Integer.parseInt(nrStringList[i]);
        }
        return rowIntList;
    }
}
