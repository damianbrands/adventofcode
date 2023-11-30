package days.day6.star1;

public class Lanternfish {
    int timer;

    public Lanternfish(){
        timer = 8;
    }

    public Lanternfish(int timer){
        this.timer = timer;
    }

    public boolean newDay(){
        if(timer == 0){
            timer = 6;
            return true;
        }
        timer--;
        return false;
    }

    @Override
    public String toString() {
        return String.valueOf(timer);
    }
}
