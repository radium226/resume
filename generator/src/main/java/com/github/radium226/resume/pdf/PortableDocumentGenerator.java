package com.github.radium226.resume.pdf;

import com.github.radium226.libreoffice.LibreOffice;
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

public class PortableDocumentGenerator implements Generator {
    
    public static final String DEFAULT_FILE_EXTENSION = "pdf";
    
    public PortableDocumentGenerator() {
        super();
    }
    
    @Override
    public void generate(File inputFile, File outputFile) throws GenerationException {
        try {
            File tempOpenDocumentFile = File.createTempFile("resume-", ".odf");
            Format.ODF.getGenerator().generate(inputFile, tempOpenDocumentFile);
            LibreOffice.convertTo(tempOpenDocumentFile, DEFAULT_FILE_EXTENSION, outputFile);
        } catch (IOException | InterruptedException e) {
            throw new GenerationException(e);
        }
        
    }

    @Override
    public String defaultFileNameExtension() {
        return DEFAULT_FILE_EXTENSION;
    }
    
}
