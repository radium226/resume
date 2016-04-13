package com.github.radium226;

import com.github.radium226.io.Resources;
import com.github.radium226.resume.Format;
import com.github.radium226.resume.GenerationException;
import com.github.radium226.resume.Generator;
import java.io.File;
import java.io.IOException;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.file.Files;
import java.util.Enumeration;
import java.util.Optional;
import java.util.jar.JarEntry;
import java.util.jar.JarFile;
import org.kohsuke.args4j.Argument;
import org.kohsuke.args4j.CmdLineException;
import org.kohsuke.args4j.CmdLineParser;
import org.kohsuke.args4j.Option;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class GenerateResume {

    final private static Logger LOGGER = LoggerFactory.getLogger(GenerateResume.class);
    
    public static enum Status {

        SUCCESS(0), FAILURE(1);

        private final int code;

        Status(int code) {
            this.code = code;
        }

        public int getCode() {
            return this.code;
        }

    }

    @Option(name = "--output-format", aliases = {"-f"}, metaVar = "FORMAT", usage = "Output format")
    private Format format;
    
    @Option(name = "--temp", aliases = {"-t"}, metaVar = "TEMP", usage = "Temp folder")
    private File tempFolder;

    @Option(name = "--color", aliases = {"-c"}, metaVar = "COLOR", usage = "Color")
    private String color = "#ff0000";
    
    @Option(name = "--display", aliases = {"-d"}, usage = "Display the generated resume")
    private boolean display = false;
    
    @Argument(index = 0, metaVar = "INPUT", required = true, usage = "Input file")
    private File inputFile;

    @Argument(index = 1, metaVar = "OUTPUT", required = true, usage = "Output file")
    private File outputFile;

    public Status execute() {
        Status status;
        try {
            LOGGER.debug("inputFile.getAbsoluteFilePath()={}", inputFile.getAbsolutePath());
            if (format == null) {
                format = Format.of(outputFile);
            }
            LOGGER.debug("format={}", format);
            Generator generator = format.getGenerator();
            generator.generate(inputFile, outputFile, color, Optional.ofNullable(tempFolder));
            if (display) {
                generator.display(outputFile);
            }
            status = Status.SUCCESS;
        } catch (GenerationException e) {
            e.printStackTrace(System.err);
            status = Status.FAILURE;
        }
        return status;
    }

    public static void main(String[] arguments) {
        Status status;
        GenerateResume generate = new GenerateResume();
        CmdLineParser parser = new CmdLineParser(generate);
        try {
            parser.parseArgument(arguments);
            status = generate.execute();
        } catch (CmdLineException e) {
            e.printStackTrace(System.err);
            parser.printUsage(System.err);
            status = Status.FAILURE;
        }
        exit(status);
    }

    public static void exit(Status status) {
        System.exit(status.getCode());
    }

}
