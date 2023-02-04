import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = null;
        int n = 0;

        try{
            scanner = new Scanner(new File("input.txt"));
            n = scanner.nextLine().length();
            scanner = new Scanner(new File("input.txt"));
        } catch (FileNotFoundException e){
            e.printStackTrace();
        }

        boolean[][] visibleTrees = new boolean[n][n];
        int[][] treeHeights = new int[n][n];

        int row = 0;
        while(scanner.hasNextLine()){
            String line = scanner.nextLine();
            for(int col = 0; col < n; col++){
                treeHeights[row][col] = line.charAt(col) - '0';
            }
            row++;
        }

        int currentMaxHeight = -1;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(treeHeights[i][j] > currentMaxHeight){
                    currentMaxHeight = treeHeights[i][j];
                    visibleTrees[i][j] = true;
                }
            }
            currentMaxHeight = -1;
        }

        for(int i = 0; i < n; i++){
            for(int j = n-1; j >= 0; j--){
                if(treeHeights[i][j] > currentMaxHeight){
                    currentMaxHeight = treeHeights[i][j];
                    visibleTrees[i][j] = true;
                }
            }
            currentMaxHeight = -1;
        }

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(treeHeights[j][i] > currentMaxHeight){
                    currentMaxHeight = treeHeights[j][i];
                    visibleTrees[j][i] = true;
                }
            }
            currentMaxHeight = -1;
        }

        for(int i = 0; i < n; i++){
            for(int j = n-1; j >= 0; j--){
                if(treeHeights[j][i] > currentMaxHeight){
                    currentMaxHeight = treeHeights[j][i];
                    visibleTrees[j][i] = true;
                }
            }
            currentMaxHeight = -1;
        }

        int visibleTreesCount = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(visibleTrees[i][j]){
                    visibleTreesCount++;
                }
            }
        }
        System.out.println(visibleTreesCount);
    }
}
