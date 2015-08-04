package com.github.radium226.resume;

import java.io.File;
import java.util.Optional;

public interface Generator {
    
    String defaultFileNameExtension();
    
    void generate(File inputFile, File outputFile, String color, Optional<File> tempFolder) throws GenerationException;
    
}
