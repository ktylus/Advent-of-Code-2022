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
        int groupMember = 1;
        char commonItem = 0;
        HashSet<Character> firstElfItems = new HashSet<>();
        HashSet<Character> secondElfItems = new HashSet<>();
        HashSet<Character> thirdElfItems = new HashSet<>();

        while (scanner.hasNextLine()){
            String line = scanner.nextLine();

            if(groupMember == 4){
                firstElfItems = new HashSet<>();
                secondElfItems = new HashSet<>();
                thirdElfItems = new HashSet<>();
                groupMember = 1;
            }

            if(groupMember == 1){
                for(int i = 0; i < line.length(); i++){
                    firstElfItems.add(line.charAt(i));
                }
            }
            if(groupMember == 2){
                for(int i = 0; i < line.length(); i++){
                    secondElfItems.add(line.charAt(i));
                }
            }
            if(groupMember == 3){
                for(int i = 0; i < line.length(); i++){
                    thirdElfItems.add(line.charAt(i));
                }
                for(char c : firstElfItems){
                    if(secondElfItems.contains(c) && thirdElfItems.contains(c)){
                        commonItem = c;
                        break;
                    }
                }
                totalItemPriority += getItemPriority(commonItem);
            }
            groupMember++;

        }
        System.out.println(totalItemPriority);
    }

}