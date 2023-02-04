import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import static java.lang.Math.*;

public class Main {

    public static void main(String[] args) {
        int maxCalories = 0;
        int secondToMaxCalories = 0;
        int thirdToMaxCalories = 0;
        int currentCalories = 0;

        try{
            Scanner sc = new Scanner(new File("input.txt"));
            while(sc.hasNextLine()){
                String line = sc.nextLine();
                if(line.equals("")){
                    if(currentCalories >= maxCalories){
                        thirdToMaxCalories = secondToMaxCalories;
                        secondToMaxCalories = maxCalories;
                        maxCalories = currentCalories;
                    }
                    else if(currentCalories >= secondToMaxCalories){
                        thirdToMaxCalories = secondToMaxCalories;
                        secondToMaxCalories = currentCalories;
                    }
                    else if(currentCalories >= thirdToMaxCalories){
                        thirdToMaxCalories = currentCalories;
                    }
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

        System.out.println(maxCalories + secondToMaxCalories + thirdToMaxCalories);
    }

}
