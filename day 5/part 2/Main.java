import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Stack;
import java.util.ArrayList;
import static java.lang.Math.*;

public class Main {

    static int numberOfStacks = 9;

    public static void main(String[] args) {

        ArrayList<Stack<Character>> crateStacks = new ArrayList<>();
        for(int i = 0; i < numberOfStacks; i++){
            crateStacks.add(new Stack<>());
        }
        crateStacks.get(0).push('C');
        crateStacks.get(0).push('Z');
        crateStacks.get(0).push('N');
        crateStacks.get(0).push('B');
        crateStacks.get(0).push('M');
        crateStacks.get(0).push('W');
        crateStacks.get(0).push('Q');
        crateStacks.get(0).push('V');

        crateStacks.get(1).push('H');
        crateStacks.get(1).push('Z');
        crateStacks.get(1).push('R');
        crateStacks.get(1).push('W');
        crateStacks.get(1).push('C');
        crateStacks.get(1).push('B');

        crateStacks.get(2).push('F');
        crateStacks.get(2).push('Q');
        crateStacks.get(2).push('R');
        crateStacks.get(2).push('J');

        crateStacks.get(3).push('Z');
        crateStacks.get(3).push('S');
        crateStacks.get(3).push('W');
        crateStacks.get(3).push('H');
        crateStacks.get(3).push('F');
        crateStacks.get(3).push('N');
        crateStacks.get(3).push('M');
        crateStacks.get(3).push('T');

        crateStacks.get(4).push('G');
        crateStacks.get(4).push('F');
        crateStacks.get(4).push('W');
        crateStacks.get(4).push('L');
        crateStacks.get(4).push('N');
        crateStacks.get(4).push('Q');
        crateStacks.get(4).push('P');

        crateStacks.get(5).push('L');
        crateStacks.get(5).push('P');
        crateStacks.get(5).push('W');

        crateStacks.get(6).push('V');
        crateStacks.get(6).push('B');
        crateStacks.get(6).push('D');
        crateStacks.get(6).push('R');
        crateStacks.get(6).push('G');
        crateStacks.get(6).push('C');
        crateStacks.get(6).push('Q');
        crateStacks.get(6).push('J');

        crateStacks.get(7).push('Z');
        crateStacks.get(7).push('Q');
        crateStacks.get(7).push('N');
        crateStacks.get(7).push('B');
        crateStacks.get(7).push('W');

        crateStacks.get(8).push('H');
        crateStacks.get(8).push('L');
        crateStacks.get(8).push('F');
        crateStacks.get(8).push('C');
        crateStacks.get(8).push('G');
        crateStacks.get(8).push('T');
        crateStacks.get(8).push('J');

        Scanner scanner = null;
        try{
            scanner = new Scanner(new File("input.txt"));
        } catch (FileNotFoundException e){
            e.printStackTrace();
        }

        for(int i = 0; i < 10; i++){
            scanner.nextLine();
        }

        while(scanner.hasNextLine()){
            String line = scanner.nextLine();
            int startStack = Integer.parseInt(line.split(" ")[3]) - 1;
            int endStack = Integer.parseInt(line.split(" ")[5]) - 1;
            int numberOfCrates = min(Integer.parseInt(line.split(" ")[1]), crateStacks.get(startStack).size());

            Stack<Character> helperStack = new Stack<>();
            for(int i = 0; i < numberOfCrates; i++){
                char crate = crateStacks.get(startStack).pop();
                helperStack.push(crate);
            }
            for(int i = 0; i < numberOfCrates; i++){
                char crate = helperStack.pop();
                crateStacks.get(endStack).push(crate);
            }
        }

        StringBuilder stackTop = new StringBuilder();
        for(int i = 0; i < numberOfStacks; i++){
            stackTop.append(crateStacks.get(i).peek());
        }
        System.out.println(stackTop.toString());
    }
}
