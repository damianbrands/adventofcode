package days.day5.star1and2;

import java.util.ArrayList;

public class Coords {
    ArrayList<Coord> coords = new ArrayList<>();

    public Coords(){}

    public Coord newCoord(int x, int y){
        Coord coord = new Coord(x, y);
        coords.add(coord);
        return coord;
    }

    public void addCoord(Coord coord){
       coords.add(coord);
    }

    public Coord coordExists(int x, int y){
        for(Coord coord : coords){
            if(coord.x == x && coord.y == y){
                return coord;
            }
        }
        return null;
    }

    public Coord findCoordAddLine(int x, int y){
        for(Coord coord : coords){
            if(coord.x == x && coord.y == y){
                coord.addLine();
                return coord;
            }
        }
        return null;
    }

    @Override
    public String toString() {
        return "Coords{" +
                "coords=" + coords +
                '}';
    }
}
