package com.github.radium226;

import com.github.radium226.io.Resources;
import com.github.radium226.resume.Format;
import com.github.radium226.resume.GenerationException;
import java.io.File;
import java.io.IOException;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.file.Files;
import java.util.Enumeration;
import java.util.jar.JarEntry;
import java.util.jar.JarFile;
import org.kohsuke.args4j.Argument;
import org.kohsuke.args4j.CmdLineException;
import org.kohsuke.args4j.CmdLineParser;
import org.kohsuke.args4j.Option;

public class GenerateResume {

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

    @Argument(index = 0, metaVar = "INPUT", required = true, usage = "Input file")
    private File inputFile;

    @Argument(index = 1, metaVar = "OUTPUT", required = true, usage = "Output file")
    private File outputFile;

    public Status execute() {
        Status status;
        try {
            System.out.println(" --> " + inputFile.getAbsolutePath());
            if (format == null) {
                format = Format.of(outputFile);
            }
            System.out.println(format);
            format.getGenerator().generate(inputFile, outputFile);
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
