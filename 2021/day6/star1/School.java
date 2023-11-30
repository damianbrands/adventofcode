package days.day6.star1;

import java.util.ArrayList;

public class School {
    ArrayList<Lanternfish> lanternfishList = new ArrayList<>();

    public School(){}

    public void addFish(Lanternfish lanternfish){
        lanternfishList.add(lanternfish);
    }

    public void newFish(){
        Lanternfish lanternfish = new Lanternfish();
        addFish(lanternfish);
    }

    public void oldFish(int timer){
        Lanternfish lanternfish = new Lanternfish(timer);
        addFish(lanternfish);
    }

    public void newDay(){
        int count = 0;
        for(Lanternfish lanternfish : lanternfishList){
            if(lanternfish.newDay()){
                count++;
            }
        }
        for(int i = 0; i < count; i++){
            newFish();
        }
    }
}
