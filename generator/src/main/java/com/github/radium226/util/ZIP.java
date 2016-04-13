package com.github.radium226.util;

import com.google.common.collect.Lists;
import java.io.File;
import java.io.IOException;
import java.io.OutputStream;
import java.nio.file.FileSystem;
import java.nio.file.FileSystems;
import java.nio.file.FileVisitResult;
import java.nio.file.FileVisitor;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.function.Predicate;
import java.util.zip.CRC32;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;

public class ZIP {
    
    @FunctionalInterface
    public static interface MethodByPathMapper {
        
        int mapMethodByPath(Path baseFolderPath, Path FilePath);
        
    } 
    
    public static void zip(File folder, OutputStream outputStream, MethodByPathMapper methodByPathMapper) throws IOException {
        zip(folder.toPath(), outputStream, methodByPathMapper);
    }
    
    public static void zip(Path folderPath, OutputStream outputStream, MethodByPathMapper methodByPathMapper) throws IOException {
        ZipOutputStream zipOutputStream = new ZipOutputStream(outputStream);
        
        List<Path> filePaths = Lists.newArrayList();
        
        Files.walkFileTree(folderPath, new FileVisitor<Path>() {

            @Override
            public FileVisitResult preVisitDirectory(Path visitedFolderPath, BasicFileAttributes attributes) throws IOException {
                return FileVisitResult.CONTINUE;
            }

            @Override
            public FileVisitResult visitFile(Path visitedFilePath, BasicFileAttributes attributes) throws IOException {
                filePaths.add(visitedFilePath);
                return FileVisitResult.CONTINUE;
            }

            @Override
            public FileVisitResult visitFileFailed(Path visitedFilePath, IOException exception) throws IOException {
                return FileVisitResult.CONTINUE;
            }

            @Override
            public FileVisitResult postVisitDirectory(Path visitedFolderPath, IOException exception) throws IOException {
                return FileVisitResult.CONTINUE;
            }
            
        });
        
        Collections.sort(filePaths, (Path onePath, Path otherPath) -> {
            String oneName = folderPath.relativize(onePath).toString();
            String otherName = folderPath.relativize(otherPath).toString();
            if (oneName.equals("mimetype") || otherName.equals("mimetype")) {
                return -1;
            } else {
                return onePath.compareTo(otherPath);
            }
        });
        
        for (Path filePath : filePaths) {
            String name = folderPath.relativize(filePath).toString();
            ZipEntry zipEntry = new ZipEntry(name);
            int method = methodByPathMapper.mapMethodByPath(folderPath, filePath);
            if (method == ZipEntry.STORED) {
                zipEntry.setMethod(method);
                CRC32 crc32 = new CRC32();
                byte[] bytes = Files.readAllBytes(filePath);
                crc32.update(bytes);
                zipEntry.setCrc(crc32.getValue());
                zipEntry.setSize(bytes.length);
                zipEntry.setCompressedSize(bytes.length);
                
            }
            zipOutputStream.putNextEntry(zipEntry);
            Files.copy(filePath, zipOutputStream);
            zipOutputStream.closeEntry();
        }
        
        zipOutputStream.finish();
    }
    
}
