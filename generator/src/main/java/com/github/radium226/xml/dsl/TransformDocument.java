package com.github.radium226.xml.dsl;

import com.github.radium226.xml.Transformer;
import com.github.radium226.xml.XML;
import com.google.common.collect.Maps;
import java.io.File;
import java.util.Map;
import org.w3c.dom.Document;

public class TransformDocument {
    
    private Document sourceDocument;
    private File relativeToFolder;
    private Map<String, String> bindings = Maps.newHashMap();

    public TransformDocument(Document sourceDocument) {
        this.sourceDocument = sourceDocument;
    }

    public Document with(Document transformationDocument) {
        return new Transformer(transformationDocument).transform(sourceDocument, relativeToFolder, bindings);
    }
    
    public TransformDocument relativeTo(File folder) {
        this.relativeToFolder = folder;
        return this;
    }
    
    public Document with(File transformationFile) {
        return with(XML.parse(transformationFile));
    }
    
    public TransformDocument bind(String key, String value) {
        bindings.put(key, value);
        return this;
    }
    
    public TransformDocument bindAll(Map<String, String> variables) {
        bindings.putAll(variables);
        return this;
    }
    
}
