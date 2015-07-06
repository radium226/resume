package com.github.radium226.resume;

import java.io.File;

public interface Generator {
    
    void generate(File inputFile, File outputFile) throws GenerationException;
    
}
