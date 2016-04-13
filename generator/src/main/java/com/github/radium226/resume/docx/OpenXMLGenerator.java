/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.github.radium226.resume.docx;

import com.github.radium226.libreoffice.LibreOffice;
import com.github.radium226.resume.Format;
import com.github.radium226.resume.GenerationException;
import com.github.radium226.resume.Generator;
import java.io.File;
import java.io.IOException;
import java.util.Optional;

/**
 *
 * @author adrien
 */
public class OpenXMLGenerator implements Generator {

    public static final String DEFAULT_FILE_NAME_EXTENSION = "docx";
    
    @Override
    public String defaultFileNameExtension() {
        return DEFAULT_FILE_NAME_EXTENSION;
    }

    @Override
    public void generate(File inputFile, File outputFile, String color, Optional<File> tempFolder) throws GenerationException {
        try {
            Generator odtGenerator = Format.ODT.getGenerator();
            File tempOpenDocumentFile = File.createTempFile("resume-", "." + odtGenerator.defaultFileNameExtension(), tempFolder.orElse(null));
            odtGenerator.generate(inputFile, tempOpenDocumentFile, color, tempFolder);
            LibreOffice.convertTo(tempOpenDocumentFile, DEFAULT_FILE_NAME_EXTENSION, outputFile);
        } catch (IOException | InterruptedException e) {
            throw new GenerationException(e);
        }
    }
    
}
