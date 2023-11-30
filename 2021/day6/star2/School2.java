package days.day6.star2;

import java.util.ArrayList;

public class School2 {
    long amount0;
    long amount1;
    long amount2;
    long amount3;
    long amount4;
    long amount5;
    long amount6;
    long amount7;
    long amount8;

    public School2(int zero, int one, int two, int three, int four, int five, int six, int seven, int eight){
        amount0 = zero;
        amount1 = one;
        amount2 = two;
        amount3 = three;
        amount4 = four;
        amount5 = five;
        amount6 = six;
        amount7 = seven;
        amount8 = eight;
    }

    public long getTotalFish(){
        System.out.println("0: " + amount0);
        System.out.println("1: " + amount1);
        System.out.println("2: " + amount2);
        System.out.println("3: " + amount3);
        System.out.println("4: " + amount4);
        System.out.println("5: " + amount5);
        System.out.println("6: " + amount6);
        System.out.println("7: " + amount7);
        System.out.println("8: " + amount8);
        return amount0 + amount1 + amount2 + amount3 + amount4 + amount5 + amount6 + amount7 + amount8;
    }

    public void newDay(){
        long newCycleFish = amount0;
        amount0 = amount1;
        amount1 = amount2;
        amount2 = amount3;
        amount3 = amount4;
        amount4 = amount5;
        amount5 = amount6;
        amount6 = amount7;
        amount7 = amount8;
        amount8 = newCycleFish;
        amount6 += newCycleFish;
    }
}
