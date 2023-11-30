package days.day4.star2;

import java.util.ArrayList;
import java.util.Arrays;

public class BingoCard2 {
    ArrayList<int[]> rows = new ArrayList<>();

    public BingoCard2(ArrayList<int[]> rows){
        this.rows = rows;
    }

    public void drawnNumber(int number){

    }

    public Boolean checkWin(ArrayList<Integer> drawnNumbers){
        boolean win = true;
        for(int[] row : rows){
            int flinkeW = 0;
            for(int i : row){
                if(drawnNumbers.contains(i)){
                    flinkeW += 1;
                }
                if(flinkeW == 5){
                    System.out.println("Rij: " + Arrays.toString(row));
                    System.out.println("Horizontale W.");
                    calculateScore(drawnNumbers);
                    return true;
                }
            }
        }
        for (int i = 0; i < rows.size(); i++) {
            int flinkeW = 0;
            ArrayList<Integer> column = new ArrayList<>();
            for (int[] row : rows) {
                column.add(row[i]);
            }
            for(int i2 : column){
                if (drawnNumbers.contains(i2)) {
                    flinkeW += 1;
                }
                if(flinkeW == 5){
                    System.out.println("Kolom: " + column);
                    System.out.println("Verticale W.");
                    calculateScore(drawnNumbers);
                    return true;
                }
            }
        }
        return false;
    }

    public int calculateScore(ArrayList<Integer> drawnNumbers){
        ArrayList<Integer> unusedNumbers = new ArrayList<>();

        int lastDrawn = drawnNumbers.get(drawnNumbers.size() -1);
        int sum = 0;
        for(int[] row : rows){
            for(int number : row){
                if(!drawnNumbers.contains(number)){
                    unusedNumbers.add(number);
                }
            }
        }
        for(int number : unusedNumbers){
            sum += number;
        }
        System.out.println("BingoCard{\n" +
                Arrays.toString(rows.get(0)) + "\n" +
                Arrays.toString(rows.get(1)) + "\n" +
                Arrays.toString(rows.get(2)) + "\n" +
                Arrays.toString(rows.get(3)) + "\n" +
                Arrays.toString(rows.get(4)) +
                "}\n");
        System.out.println(unusedNumbers);
        System.out.println(lastDrawn);
        System.out.println(sum);
        System.out.println(lastDrawn * sum);
        return(lastDrawn * sum);
    }

    public ArrayList<int[]> getRows() {
        return rows;
    }

    @Override
    public String toString() {
        return "BingoCard{\n" +
                Arrays.toString(rows.get(0)) + "\n" +
                Arrays.toString(rows.get(1)) + "\n" +
                Arrays.toString(rows.get(2)) + "\n" +
                Arrays.toString(rows.get(3)) + "\n" +
                Arrays.toString(rows.get(4)) +
                "}\n";
    }
}
