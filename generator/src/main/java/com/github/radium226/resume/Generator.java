package com.github.radium226.resume;

import java.io.File;
import java.io.IOException;
import java.util.Optional;

public interface Generator {
    
    String defaultFileNameExtension();
    
    void generate(File inputFile, File outputFile, String color, Optional<File> tempFolder) throws GenerationException;
    
    default void display(File file) {
        try {
            Process process = new ProcessBuilder("exo-open", file.getAbsolutePath()).start();
            process.waitFor();
        } catch (IOException | InterruptedException e) {
            e.printStackTrace(System.err);
        }
    }
    
}
