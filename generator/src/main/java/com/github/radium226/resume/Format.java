package com.github.radium226.resume;

import com.github.radium226.resume.odf.ODFGenerator;
import com.github.radium226.resume.pdf.PDFGenerator;

public enum Format {
    
    ODF(new ODFGenerator()), PDF(new PDFGenerator());
    
    private final Generator generator;
    
    Format(Generator generator) {
        this.generator = generator;
    }
    
    public Generator getGenerator() {
        return generator;
    }
    
}
