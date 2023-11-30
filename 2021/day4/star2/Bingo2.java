package days.day4.star2;

import days.day4.star1.BingoCard;

import java.util.ArrayList;

public class Bingo2 {
    ArrayList<BingoCard2> bingoCards = new ArrayList<>();
    ArrayList<Integer> drawnNumbers = new ArrayList<>();

    public Bingo2(){}

    public boolean checkBingo(){
        ArrayList<BingoCard2> completed = new ArrayList<>();
        for(BingoCard2 bingoCard : bingoCards){
            if(bingoCard.checkWin(drawnNumbers)){
                completed.add(bingoCard);
            }
        }
        for(BingoCard2 completedCard : completed){
            removeBingoCard(completedCard);
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
        BingoCard2 bingoCard = new BingoCard2(rows);
        bingoCards.add(bingoCard);
    }

    public void removeBingoCard(BingoCard2 bingoCard){
        bingoCards.remove(bingoCard);
    }

    @Override
    public String toString() {
        return "Bingo{" +
                "bingoCards=" + bingoCards +
                '}';
    }
}
