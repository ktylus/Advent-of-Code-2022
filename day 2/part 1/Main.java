import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;

public class Main {

    static HashMap<Character, Character> toABC = new HashMap<>();
    static HashMap<Character, Integer> scoring = new HashMap<>();

    static boolean isWin(char expectedPlay, char myPlay){
        if(myPlay == 'A'){
            if(expectedPlay == 'B') return false;
            if(expectedPlay == 'C') return true;
        }
        if(myPlay == 'B'){
            if(expectedPlay == 'A') return true;
            if(expectedPlay == 'C') return false;
        }
        if(myPlay == 'C'){
            if(expectedPlay == 'A') return false;
            if(expectedPlay == 'B') return true;
        }
        return false;
    }

    static int grantPoints(char expectedPlay, char myPlay){
        myPlay = toABC.get(myPlay);


        if(myPlay == expectedPlay){
            return 3 + scoring.get(myPlay);
        }
        if(isWin(expectedPlay, myPlay)){
            return 6 + scoring.get(myPlay);
        }
        else{
            return scoring.get(myPlay);
        }
    }

    public static void main(String[] args) {
        int totalPoints = 0;
        toABC.put('X', 'A');
        toABC.put('Y', 'B');
        toABC.put('Z', 'C');
        scoring.put('A', 1);
        scoring.put('B', 2);
        scoring.put('C', 3);

        try{
            Scanner scanner = new Scanner(new File("input.txt"));
            while(scanner.hasNextLine()){
                String line = scanner.nextLine();
                char expectedPlay = line.split(" ")[0].charAt(0);
                char myPlay = line.split(" ")[1].charAt(0);

                totalPoints += grantPoints(expectedPlay, myPlay);
            }
        } catch (FileNotFoundException e){
            e.printStackTrace();
        }
        System.out.println(totalPoints);
    }

}