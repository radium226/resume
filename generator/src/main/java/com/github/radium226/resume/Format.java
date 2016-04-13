package com.github.radium226.resume;

import com.github.radium226.resume.docx.OpenXMLGenerator;
import com.github.radium226.resume.odt.OpenDocumentGenerator;
import com.github.radium226.resume.pdf.PortableDocumentGenerator;
import com.google.common.io.Files;
import java.io.File;
import java.util.Optional;
import java.util.stream.Stream;

public enum Format {
    
    ODT(new OpenDocumentGenerator()), PDF(new PortableDocumentGenerator()), DOCX(new OpenXMLGenerator());
    
    private final Generator generator;
    
    Format(Generator generator) {
        this.generator = generator;
    }
    
    public Generator getGenerator() {
        return generator;
    }
    
    public static Format ofFileName(String fileName) {
        String fileNameExtension = Files.getFileExtension(fileName);
        return ofFileNameExtension(fileNameExtension);
    }
    
    public static Format ofFileNameExtension(String fileNameExtension) {
        Optional<Format> optionalFormat = Stream.of(values()).filter(format -> format.getGenerator().defaultFileNameExtension().equalsIgnoreCase(fileNameExtension)).findFirst();
        if (!optionalFormat.isPresent()) {
            throw new UnsupportedOperationException("Unable to find appropriate format for " + fileNameExtension + " extension");
        }
        return optionalFormat.get();
    }
    
    public static Format ofFile(File file) {
        return ofFileName(file.getName());
    }
    
    public static Format of(File file) {
        return ofFile(file);
    }
    
}
