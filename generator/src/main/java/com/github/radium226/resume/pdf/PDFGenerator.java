package com.github.radium226.resume.pdf;

import com.github.radium226.resume.Format;
import com.github.radium226.resume.GenerationException;
import com.github.radium226.resume.Generator;
import java.io.File;
import java.io.IOException;
import java.nio.file.CopyOption;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;
import java.util.logging.Level;
import java.util.logging.Logger;

public class PDFGenerator implements Generator {
    
    public PDFGenerator() {
        super();
    }
    
    @Override
    public void generate(File inputFile, File outputFile) throws GenerationException {
        try {
            File tempODFFile = File.createTempFile("resume-", ".odf");
            File tempPDFFolder = Files.createTempDirectory("resume-").toFile();
            Format.ODF.getGenerator().generate(inputFile, tempODFFile);
            
            ProcessBuilder processBuilder = new ProcessBuilder("libreoffice", "--headless", "--convert-to", "pdf", tempODFFile.getAbsolutePath(), "--outdir", tempPDFFolder.getAbsolutePath()).inheritIO();
            Process process = processBuilder.start();
            process.waitFor();
            
            System.out.println(" --> " + tempPDFFolder.getAbsolutePath());
            
            File tempPDFFile = tempPDFFolder.listFiles()[0];
            Files.copy(tempPDFFile.toPath(), outputFile.toPath(), StandardCopyOption.REPLACE_EXISTING);
            
            //soffice --headless --convert-to txt filename.doc
            
        } catch (IOException e) {
            throw new GenerationException(e);
        } catch (InterruptedException e) {
            throw new GenerationException(e);
        }
        
    }
    
}
