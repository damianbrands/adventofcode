package days.day5.star1and2;

public class Coord {
    int x;
    int y;
    int lines;

    public Coord(int x, int y){
        this.x = x;
        this.y = y;
        lines = 1;
    }

    public void addLine(){
        lines += 1;
    }

    @Override
    public String toString() {
        if(lines == 0){
            return ".";
        }
        else{
            return "{" + x + "," + y + "," + lines + "}";
        }
    }
}
