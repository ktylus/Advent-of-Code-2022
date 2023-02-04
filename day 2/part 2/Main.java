import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;

public class Main {

    static HashMap<Character, Integer> scoring = new HashMap<>();

    static int grantPoints(char expectedPlay, char intendedResult){

        if(intendedResult == 'Z'){
            if(expectedPlay == 'A') return 8;
            if(expectedPlay == 'B') return 9;
            else return 7;
        }
        if(intendedResult == 'Y'){
            if(expectedPlay == 'A') return 4;
            if(expectedPlay == 'B') return 5;
            else return 6;
        }
        else{
            if(expectedPlay == 'A') return 3;
            if(expectedPlay == 'B') return 1;
            else return 2;
        }
    }

    public static void main(String[] args) {
        int totalPoints = 0;
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