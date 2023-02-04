import java.util.ArrayList;

public class Directory {

    String name;
    int filesSize;
    ArrayList<Directory> directories;

    Directory(String name){
        filesSize = 0;
        directories = new ArrayList<>();
        this.name = name;
    }

    public void addDirectory(String directoryName){
        for(Directory dir : directories){
            if(dir.name.equals(directoryName)){
                return;
            }
        }
        directories.add(new Directory(directoryName));
    }

    public int calculateDirectorySize(){
        int subdirectoriesTotalSize = 0;
        for(Directory dir : directories){
            subdirectoriesTotalSize += dir.calculateDirectorySize();
        }
        return filesSize + subdirectoriesTotalSize;
    }

    public Directory findSubdirectory(String directoryName){
        for(Directory subdirectory : directories){
            if(subdirectory.name.equals(directoryName)){
                return subdirectory;
            }
        }
        return null;
    }
}
