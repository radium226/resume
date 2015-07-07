package com.github.radium226.libreoffice;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;

public class LibreOffice {

    private LibreOffice() {
        super();
    }
    
    public static void convertTo(File inputFile, String format, File outputFile) throws IOException, InterruptedException {
        String inputFilePath = inputFile.getAbsolutePath();
        File tempFolder = Files.createTempDirectory("libreoffice-").toFile();
        String tempFolderPath = tempFolder.getAbsolutePath();
        
        System.out.println(" format = " + format);
        
        ProcessBuilder processBuilder = new ProcessBuilder("libreoffice", "--headless", "--convert-to", format, inputFilePath, "--outdir", tempFolderPath).inheritIO();
        Process process = processBuilder.start();
        process.waitFor();

        File tempFilePath = tempFolder.listFiles()[0];
        Files.copy(tempFilePath.toPath(), outputFile.toPath(), StandardCopyOption.REPLACE_EXISTING);
    }
    
}
