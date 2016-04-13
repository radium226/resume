package com.github.radium226.xml.dsl;

import com.github.radium226.util.ThrowableThrower;
import com.github.radium226.xml.Style;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import javax.xml.transform.Result;
import javax.xml.transform.Source;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Document;

public class PrintDocument {

    
    private Document document;
    
    public PrintDocument(Document document) {
        super();
        
        this.document = document;
    }
    
    public void to(File file, Style style) throws TransformerException, IOException {
        try (OutputStream outputStream = new FileOutputStream(file)) {
            to(outputStream, style);
        }
    }
    
    public void to(File file) throws TransformerException, IOException {
        to(file, Style.PRETTY);
    }
    
    public void to(OutputStream outputStream) throws TransformerException {
        to(outputStream, Style.PRETTY);
    }
    
    public void to(OutputStream outputStream, Style style) throws TransformerException {
        TransformerFactory transformerFactory = TransformerFactory.newInstance();
        Transformer transformer = transformerFactory.newTransformer();
        style.getStylizer().stylize(transformer);
        Source source = new DOMSource(this.document);
        Result result = new StreamResult(outputStream);
        transformer.transform(source, result);
    }
    
    @Override
    public String toString() {
        try {
            return toString(Style.PRETTY);
        } catch (TransformerException e) {
            ThrowableThrower.throwThrowable(e);
            return null;
        }
    }
    
    public String toString(Style style) throws TransformerException {
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        to(byteArrayOutputStream, style);
        return byteArrayOutputStream.toString();
    }
    
}
