import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Scanner;

public class Main {

    static boolean isUniqueChars(String input){
        HashSet<Character> chars = new HashSet<>();
        for(int i = 0; i < input.length(); i++){
            chars.add(input.charAt(i));
        }
        return chars.size() == input.length();
    }

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input.txt"));
        String data = scanner.nextLine();

        int lastCharPosition = 4;
        String code = "";
        while(lastCharPosition < data.length()){
            code = data.substring(lastCharPosition - 4, lastCharPosition);
            if(isUniqueChars(code)){
                break;
            }
            else{
                lastCharPosition++;
            }
        }
        System.out.println(lastCharPosition);
    }

}
