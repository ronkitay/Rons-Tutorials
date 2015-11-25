package org.ronkitay.tutorials.imagedupcleaner;

import org.apache.commons.io.FileUtils;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

/**
 * @author Ron Kitay
 * @since 14/09/15
 */
public class Main {

    static boolean realRun = false;
    static Collection<String> pathsToDelete = new ArrayList<String>();
    static String pathToMoveTo = "/Users/rkitay/Pictures/_Duplicates_To_Be_Deleted";
    static String imagesDir = "/Users/rkitay/Pictures/Sort_From_Home";
    private static int countOfFilesToBeDeleted;

    public static void main(String[] args) throws IOException {
        String duplicateMd5File = imagesDir + "/files_to_delete";

//        pathsToDelete.add("/Users/rkitay/Pictures/Sort_From_Home/zzzzzzzzzzzzzzzz");
//        pathsToDelete.add("/Users/rkitay/Pictures/Sort_From_Home/___Much More to Sort");
//        pathsToDelete.add("/Users/rkitay/Pictures/Sort_From_Home/__________________Ron's Phone - probably duplicates (Old)");
//        pathsToDelete.add("/Users/rkitay/Pictures/Sort_From_Home/____Even More to Sort");
//        pathsToDelete.add("/Users/rkitay/Pictures/Sort_From_Home/___Ron's Phone - to sort");
//        pathsToDelete.add("/Users/rkitay/Pictures/Sort_From_Home/Unsorted Camara Phothos");
//        pathsToDelete.add("/Users/rkitay/Pictures/Sort_From_Home/_Ron To Sort - from DropBox");
//        pathsToDelete.add("/Users/rkitay/Pictures/Sort_From_Home/__Print for Grandma");
//
//        pathsToDelete.add("/Users/rkitay/Pictures/Sort_From_Home/_Sanfrancisco - To sort");


        final List<String> lines = FileUtils.readLines(new File(duplicateMd5File));

        final List<File> filesToDeleteForTheCurrentMd5 = new ArrayList<File>();

        for (String line : lines) {
            if (line.equals("---------------------------------------------------")) {
                deleteIfThereAreValidDuplicates(filesToDeleteForTheCurrentMd5);
                filesToDeleteForTheCurrentMd5.clear();
            }
            else if (line.startsWith("./")) {
                addFile(filesToDeleteForTheCurrentMd5, imagesDir, line);
            }
            else {
                System.out.printf("Working on MD5 <%s>\n", line);
            }
        }

        if (realRun) {
            System.out.printf("Files deleted <%s>\n", countOfFilesToBeDeleted);
        }
        else {
            System.out.printf("Files that would have been deleted <%s>\n", countOfFilesToBeDeleted);
        }
    }

    private static void addFile(List<File> filesToDeleteForTheCurrentMd5, String imagesDir, String relativePath) {
        relativePath = relativePath.substring(1).replace("\\", "");
        File file = new File(imagesDir + relativePath);
        if (file.exists()) { // Add only existing files
            filesToDeleteForTheCurrentMd5.add(file);
        }
    }

    private static void deleteIfThereAreValidDuplicates(List<File> filesToDeleteForTheCurrentMd5) throws IOException {
        List<File> filesToDelete = new ArrayList<File>();
        List<File> filesToKeep = new ArrayList<File>();
        for (File file : filesToDeleteForTheCurrentMd5) {
            if (fileIsInPathToDelete(file)) {
                filesToDelete.add(file);
            }
            else {
                filesToKeep.add(file);
            }
        }

        if (filesToDelete.size() > 0 && filesToKeep.size() > 0) {
            for (File file : filesToDelete) {
                countOfFilesToBeDeleted++;
                System.out.printf("I'm planning to DELETE <%s>\n", file.getAbsolutePath());
                if (realRun) {
                    moveFile(file);
                }
//                FileUtils.deleteQuietly(file);
            }
            for (File file : filesToKeep) {
                System.out.printf("I'm planning to KEEP <%s>\n", file.getAbsolutePath());
            }
        }
    }

    private static void moveFile(File file) throws IOException {
        final String relativePathToFile = file.getAbsolutePath().substring(imagesDir.length());
        File newFile = new File(pathToMoveTo + "/" + relativePathToFile);
        final File directoryToMoveTo = newFile.getParentFile();
        FileUtils.forceMkdir(directoryToMoveTo);
        FileUtils.moveFile(file, newFile);
    }

    private static boolean fileIsInPathToDelete(File file) {
        for (String pathToDelete : pathsToDelete) {
            if (file.getAbsolutePath().contains(pathToDelete)) {
                return true;
            }
        }
        return false;
    }
}
