import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;


public class Main {

    static Directory root = new Directory("/");

    public static ArrayList<Integer> getAllRelevantDirectorySizes(){
        ArrayList<Integer> sizes = new ArrayList<>();
        helper(root, sizes);
        return sizes;
    }

    private static void helper(Directory currentDirectory, ArrayList<Integer> sizes) {
        int size = currentDirectory.calculateDirectorySize();
        if (size <= 100000){
            sizes.add(size);
        }
        for(Directory dir : currentDirectory.directories){
            helper(dir, sizes);
        }
    }

    public static Directory getCurrentDirectory(String currentDirectory){
        String[] pathToDirectory = currentDirectory.split("/");
        Directory current = root;

        for(String directoryName : pathToDirectory){
            if(!directoryName.equals("")){
                current = current.findSubdirectory(directoryName);
            }
        }
        return current;
    }

    public static String parseCommand(String currentDirectory, String line){
        String command = line.substring(2);
        if(command.equals("ls")){
            return currentDirectory;
        }
        if(command.equals("cd ..")){
            int secondToLastSlashIndex = 0;
            for(int i = currentDirectory.length() - 1; i >= 0; i--){
                if(currentDirectory.charAt(i) == '/' && i < currentDirectory.length() - 1){
                    secondToLastSlashIndex = i;
                    break;
                }
            }
            return currentDirectory.substring(0, secondToLastSlashIndex + 1);
        }
        if(command.equals("cd /")){
            return "/";
        }
        return currentDirectory + command.substring(3) + "/";
    }

    public static void main(String[] args) {
        Scanner scanner = null;
        try{
            scanner = new Scanner(new File("input.txt"));
        } catch (FileNotFoundException e){
            e.printStackTrace();
        }

        String currentDirectoryName = "";
        while(scanner.hasNextLine()){
            String line = scanner.nextLine();
            if(line.charAt(0) == '$'){
                currentDirectoryName = parseCommand(currentDirectoryName, line);
                continue;
            }

            Directory currentDirectory = getCurrentDirectory(currentDirectoryName);
            if(line.startsWith("dir")){
                String directoryName = line.substring(4);
                currentDirectory.addDirectory(directoryName);
            }
            else{
                int fileSize = Integer.parseInt(line.split(" ")[0]);
                currentDirectory.filesSize += fileSize;
            }
        }

        ArrayList<Integer> sizes = getAllRelevantDirectorySizes();
        System.out.println(sizes);
        int sum = 0;
        for(int size : sizes){
            sum += size;
        }
        System.out.println(sum);
    }

}
