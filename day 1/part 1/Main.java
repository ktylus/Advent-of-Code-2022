import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import static java.lang.Math.*;

public class Main {

    public static void main(String[] args) {
        int maxCalories = 0;
        int currentCalories = 0;

        try{
            Scanner sc = new Scanner(new File("input.txt"));
            while(sc.hasNextLine()){
                String line = sc.nextLine();
                if(line.equals("")){
                    maxCalories = max(maxCalories, currentCalories);
                    currentCalories = 0;
                }
                else{
                    int caloriesInLine = Integer.parseInt(line);
                    currentCalories += caloriesInLine;
                }
            }
        } catch (FileNotFoundException e){
            e.printStackTrace();
        }

        System.out.println(maxCalories);
    }

}
