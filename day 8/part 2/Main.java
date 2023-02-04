import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

    public static int calculateScenicScore(int[][] treeHeights, int row, int col){
        int treeHeight = treeHeights[row][col];
        int n = treeHeights.length;
        int upScore = 0;
        int downScore = 0;
        int leftScore = 0;
        int rightScore = 0;

        for(int i = 1; row - i >= 0; i++){
            upScore++;
            if(treeHeights[row - i][col] >= treeHeight){
                break;
            }
        }
        for(int i = 1; col + i < n; i++){
            rightScore++;
            if(treeHeights[row][col + i] >= treeHeight){
                break;
            }
        }
        for(int i = 1; row + i < n; i++){
            downScore++;
            if(treeHeights[row + i][col] >= treeHeight){
                break;
            }
        }
        for(int i = 1; col - i >= 0; i++){
            leftScore++;
            if(treeHeights[row][col - i] >= treeHeight){
                break;
            }
        }

        return upScore * downScore * leftScore * rightScore;
    }

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

        int maxScenicScore = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                int score = calculateScenicScore(treeHeights, i, j);
                if(score > maxScenicScore){
                    maxScenicScore = score;
                }
            }
        }
        System.out.println(maxScenicScore);
    }
}