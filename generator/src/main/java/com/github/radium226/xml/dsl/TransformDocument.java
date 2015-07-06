package com.github.radium226.xml.dsl;

import com.github.radium226.xml.Transformer;
import com.github.radium226.xml.XML;
import java.io.File;
import org.w3c.dom.Document;

public class TransformDocument {
    
    private Document sourceDocument;
    private File relativeToFolder;

    public TransformDocument(Document sourceDocument) {
        this.sourceDocument = sourceDocument;
    }

    public Document with(Document transformationDocument) {
        return new Transformer(transformationDocument).transform(sourceDocument, relativeToFolder);
    }
    
    public TransformDocument relativeTo(File folder) {
        this.relativeToFolder = folder;
        return this;
    }
    
    public Document with(File transformationFile) {
        return with(XML.parse(transformationFile));
    }
    
}
