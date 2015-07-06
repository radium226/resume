package com.github.radium226.xml.dsl;

import com.github.radium226.xml.Transformer;
import java.io.File;
import static com.github.radium226.xml.XML.*;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import javax.xml.transform.TransformerException;
import org.w3c.dom.Document;

public class TransformFile {

    public class WithFile {

        private File transformationFile;

        public WithFile(File transformationFile) {
            super();
            this.transformationFile = transformationFile;
        }

        public void to(File outputFile) throws TransformerException, IOException {
            try (OutputStream outputStream = new FileOutputStream(outputFile)) {
                to(outputStream);
            }
        }

        public void to(OutputStream outputStream) throws TransformerException {
            Document inputDocument = parse(inputFile);
            Document transformationDocument = parse(transformationFile);
            Document outputDocument = transform(inputDocument).with(transformationDocument);
            print(outputDocument).to(outputStream);
        }
    }
    private File inputFile;

    public TransformFile(File inputFile) {
        super();
        this.inputFile = inputFile;
    }

    public WithFile with(File transformationFile) {
        return new WithFile(transformationFile);
    }

}
