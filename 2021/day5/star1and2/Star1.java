package days.day5.star1and2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Star1 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new File("src/main/java/days/day5/input.txt"));
        ArrayList<Line> lines = new ArrayList<>();
        Coords coords = new Coords();

        while(sc.hasNextLine()){
            String replace = sc.nextLine().replace(" -> ", ",");
            String[] valuesString = replace.split(",");
            int[] values = new int[valuesString.length];
            for (int i = 0; i < valuesString.length; i++) {
                values[i] = Integer.parseInt(valuesString[i]);
            }
            Line line = new Line(values[0], values[1], values[2], values[3]);
            lines.add(line);
        }

        for(Line line : lines){
            int x1 = line.x1;
            int x2 = line.x2;
            int y1 = line.y1;
            int y2 = line.y2;

            System.out.println("x " + x1 + ", " + x2 + " - y " + y1 + ", " + y2);

            //Vertical
            if(x1 == x2){
                System.out.println("Veritcal");
                int length;
                if(y1 > y2){
                    length = y1 - y2 + 1;
                }else{
                    length = y2 - y1 + 1;
                }
                for(int i = 0; i < length; i++){
                    if(y1 > y2){
                        Coord coord = coords.coordExists(x1, y1 - i);
                        if(coord != null){
                            coord.addLine();
                        }else{
                            coords.newCoord(x1, y1 - i);
                        }
                    }else{
                        Coord coord = coords.coordExists(x1, y2 - i);
                        if(coord != null){
                            coord.addLine();
                        }else{
                            coords.newCoord(x1, y2 - i);
                        }
                    }
                }
            }

            //Horizontal
            if(y1 == y2){
                System.out.println("Horizontal");
                int length;
                if(x1 > x2){
                    length = x1 - x2 + 1;
                }else{
                    length = x2 - x1 + 1;
                }
                for(int i = 0; i < length; i++){
                    if(x1 > x2){
                        Coord coord = coords.coordExists(x1 - i, y1);
                        if(coord != null){
                            coord.addLine();
                        }else{
                            coords.newCoord(x1 - i, y1);
                        }
                    }else{
                        Coord coord = coords.coordExists(x2 - i, y1);
                        if(coord != null){
                            coord.addLine();
                        }else{
                            coords.newCoord(x2 - i, y1);
                        }
                    }
                }
            }

            //Diagonal
            if(Math.abs(x1 - x2) == Math.abs(y1 - y2)){
                System.out.println("Diagonal line");

                int length;
                if(x1 > x2){
                    length = x1 - x2 + 1;
                }else{
                    length = x2 - x1 + 1;
                }

                if (x1 > x2 && y1 > y2) {
                    for(int i = 0; i < length; i++) {
                        Coord coord = coords.coordExists(x1 - i, y1 - i);
                        if (coord != null) {
                            coord.addLine();
                        } else {
                            coords.newCoord(x1 - i, y1 - i);
                        }
                    }
                }else if (x2 > x1 && y1 > y2) {
                    for(int i = 0; i < length; i++) {
                        Coord coord = coords.coordExists(x1 + i, y1 - i);
                        if (coord != null) {
                            coord.addLine();
                        } else {
                            coords.newCoord(x1 + i, y1 - i);
                        }
                    }
                }else if (x1 > x2) {
                    for(int i = 0; i < length; i++) {
                        Coord coord = coords.coordExists(x1 - i, y1 + i);
                        if (coord != null) {
                            coord.addLine();
                        } else {
                            coords.newCoord(x1 - i, y1 + i);
                        }
                    }
                }else {
                    for(int i = 0; i < length; i++) {
                        Coord coord = coords.coordExists(x1 + i, y1 + i);
                        if (coord != null) {
                            coord.addLine();
                        } else {
                            coords.newCoord(x1 + i, y1 + i);
                        }
                    }
                }
            }
        }

        System.out.println(coords.coords);

        int count = 0;


        for(Coord coord : coords.coords){
            if(coord.lines > 1){
                count++;
            }
        }

        System.out.println(count);
    }
}
