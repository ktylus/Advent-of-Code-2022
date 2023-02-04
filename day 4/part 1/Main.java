import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

    public static boolean isContained(int lowerBound1, int upperBound1, int lowerBound2, int upperBound2){
        if(lowerBound1 >= lowerBound2 && upperBound1 <= upperBound2) {
            return true;
        }
        return lowerBound2 >= lowerBound1 && upperBound2 <= upperBound1;
    }

    public static void main(String[] args) {
        Scanner scanner = null;
        try{
            scanner = new Scanner(new File("input.txt"));
        } catch (FileNotFoundException e){
            e.printStackTrace();
        }

        int pairsWithContainedIntervals = 0;
        while(scanner.hasNextLine()){
            String line = scanner.nextLine();
            int firstElfLowerBound = Integer.parseInt(line.split(",")[0].split("-")[0]);
            int firstElfUpperBound = Integer.parseInt(line.split(",")[0].split("-")[1]);
            int secondElfLowerBound = Integer.parseInt(line.split(",")[1].split("-")[0]);
            int secondElfUpperBound = Integer.parseInt(line.split(",")[1].split("-")[1]);

            if(isContained(firstElfLowerBound, firstElfUpperBound, secondElfLowerBound, secondElfUpperBound)){
                pairsWithContainedIntervals++;
            }
        }
        System.out.println(pairsWithContainedIntervals);
    }

}
