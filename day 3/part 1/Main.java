import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Scanner;

public class Main {

    public static int getItemPriority(char item){
        if(item >= 'a' && item <= 'z'){
            return item - 'a' + 1;
        }
        else{
            return item - 'A' + 27;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = null;
        
        try{
            scanner = new Scanner(new File("input.txt"));
        } catch (FileNotFoundException e){
            e.printStackTrace();
        }

        int totalItemPriority = 0;
        while (scanner.hasNextLine()){
            HashSet<Character> firstRucksackItems = new HashSet<>();
            HashSet<Character> secondRucksackItems = new HashSet<>();
            String line = scanner.nextLine();
            String firstRucksack = line.substring(0, line.length() / 2);
            String secondRucksack = line.substring(line.length() / 2);

            for(int i = 0; i < firstRucksack.length(); i++){
                firstRucksackItems.add(firstRucksack.charAt(i));
                secondRucksackItems.add(secondRucksack.charAt(i));
            }

            char commonItem;
            for(char c : firstRucksackItems){
                if(secondRucksackItems.contains(c)){
                    commonItem = c;
                    totalItemPriority += getItemPriority(commonItem);
                    break;
                }
            }

        }
        System.out.println(totalItemPriority);
    }
    
}
