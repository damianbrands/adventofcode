package days.day4.star1;

import java.util.ArrayList;

public class Bingo {
    ArrayList<BingoCard> bingoCards = new ArrayList<>();
    ArrayList<Integer> drawnNumbers = new ArrayList<>();

    public Bingo(){}

    public boolean checkBingo(){
        for(BingoCard bingoCard : bingoCards){
            if(bingoCard.checkWin(drawnNumbers)){
                return true;
            }
        }
        return false;
    }

    public void addDrawn(int numberDrawn){
        drawnNumbers.add(numberDrawn);
        System.out.println(drawnNumbers);
    }

    public void addBingoCard(int[] row1, int[] row2, int[] row3, int[] row4, int[] row5){
        ArrayList<int[]> rows = new ArrayList<>();
        rows.add(row1);
        rows.add(row2);
        rows.add(row3);
        rows.add(row4);
        rows.add(row5);
        BingoCard bingoCard = new BingoCard(rows);
        bingoCards.add(bingoCard);
    }

    @Override
    public String toString() {
        return "Bingo{" +
                "bingoCards=" + bingoCards +
                '}';
    }
}
