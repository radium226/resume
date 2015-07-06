package com.github.radium226.xml;

import com.github.radium226.resume.odf.FormatDate;
import com.github.radium226.resume.odf.FormatLocation;
import com.github.radium226.resume.GenerateSectionName;
import java.io.File;
import javax.xml.transform.Source;
import javax.xml.transform.TransformerException;
import javax.xml.transform.URIResolver;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamSource;
import net.sf.saxon.s9api.DOMDestination;
import net.sf.saxon.s9api.Processor;
import net.sf.saxon.s9api.SaxonApiException;
import net.sf.saxon.s9api.XdmNode;
import net.sf.saxon.s9api.XsltCompiler;
import net.sf.saxon.s9api.XsltExecutable;
import net.sf.saxon.s9api.XsltTransformer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.w3c.dom.Document;

public class Transformer {

    private static final Logger LOGGER = LoggerFactory.getLogger(Transformer.class);

    private Document transformation;
    
    public Transformer(Document transformation) {
        super();
        
        this.transformation = transformation;
    }
    
    public Document transform(Document source, File workingFolder) {
        Document destination = XML.create();
        try {
            Processor processor = new Processor(false);
            processor.registerExtensionFunction(new FormatDate());
            processor.registerExtensionFunction(new FormatLocation());
            processor.registerExtensionFunction(new GenerateSectionName());
            //XdmNode source = processor.newDocumentBuilder().build(new DOMSource(xmlSourceDocument));
            XsltCompiler compiler = processor.newXsltCompiler();
            compiler.setURIResolver(new URIResolver() {

                @Override
                public Source resolve(String href, String base) throws TransformerException {
                    return new StreamSource(new File(workingFolder, href));
                }
                
            });
            XsltExecutable executable = compiler.compile(new DOMSource(transformation));
            XsltTransformer transformer = executable.load();
            
            transformer.setDestination(new DOMDestination(destination));
            transformer.setSource(new DOMSource(source));
            transformer.transform();
            return destination;
        } catch (SaxonApiException e) {
            LOGGER.warn("Something happened while transforming document {}", source, e);
        }
        return source;
    }
    
}
