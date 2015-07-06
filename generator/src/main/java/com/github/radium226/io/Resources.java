package com.github.radium226.io;

import com.google.common.io.ByteStreams;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.file.FileVisitResult;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.Enumeration;
import java.util.jar.JarEntry;
import java.util.jar.JarFile;

public class Resources {

    public static void copyResources(String inputFolderPath, File outputFolder) throws IOException {
        final File fileOrFolder = new File(Resources.class.getProtectionDomain().getCodeSource().getLocation().getPath());
        if (fileOrFolder.isFile()) {
            try (JarFile jarFile = new JarFile(fileOrFolder)) {
                final Enumeration<JarEntry> jarEntries = jarFile.entries(); //gives ALL entries in jar
                while (jarEntries.hasMoreElements()) {
                    JarEntry jarEntry = jarEntries.nextElement();
                    final String jarEntryFileOrFolderName = jarEntry.getName();
                    if (jarEntryFileOrFolderName.startsWith(inputFolderPath + "/")) { //filter according to the path
                        if (!jarEntryFileOrFolderName.endsWith("/")) {
                            String filePath = jarEntryFileOrFolderName.substring(inputFolderPath.length());
                            File outputFile = new File(outputFolder.getAbsoluteFile() + "/" + filePath);
                            outputFile.getParentFile().mkdirs();
                            ByteStreams.copy(jarFile.getInputStream(jarEntry), new FileOutputStream(outputFile));
                        }
                    }
                }
            }
        } else {
            final URL url = com.google.common.io.Resources.getResource(inputFolderPath);
            if (url != null) {
                try {
                    final Path targetPath = outputFolder.toPath();
                    final Path sourcePath = Paths.get(url.toURI());
                    Files.walkFileTree(sourcePath, new SimpleFileVisitor<Path>() {

                        @Override
                        public FileVisitResult preVisitDirectory(final Path dir, final BasicFileAttributes attrs) throws IOException {
                            Files.createDirectories(targetPath.resolve(sourcePath.relativize(dir)));
                            return FileVisitResult.CONTINUE;
                        }

                        @Override
                        public FileVisitResult visitFile(final Path file, final BasicFileAttributes attrs) throws IOException {
                            Files.copy(file, targetPath.resolve(sourcePath.relativize(file)));
                            return FileVisitResult.CONTINUE;
                        }

                    });
                } catch (URISyntaxException e) {

                }
            }
        }
    }

}
