package com.github.radium226.xml;

import com.github.radium226.xml.dsl.TransformDocument;
import com.github.radium226.xml.dsl.TransformFile;
import com.github.radium226.xml.dsl.PrintDocument;
import com.github.radium226.xml.dsl.SelectQuery;
import com.google.common.collect.Lists;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.StringWriter;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Optional;
import java.util.logging.Level;
import java.util.stream.Collectors;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.TransformerFactoryConfigurationError;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

public class XML {

    // select("//truc").with(namespace("", ""), defaultNamespace("")).
    
    final private static Logger LOGGER = LoggerFactory.getLogger(XML.class);
    
    private XML() {
        super();
    }
    
    public static TransformDocument transform(Document sourceDocument) {
        return new TransformDocument(sourceDocument);
    }
    
    public static TransformFile transform(File originFile) {
        return new TransformFile(originFile);
    }

    public static void swapNodeWithNodes(Node oneNode, Node... otherNodes) {
        Document document = oneNode.getOwnerDocument();
        List<Node> insertedNodes = Arrays.asList(otherNodes).stream().map(otherNode -> document.importNode(otherNode, true)).collect(Collectors.toList());
        Collections.reverse(insertedNodes);
        insertedNodes.forEach(insertedNode -> oneNode.getParentNode().insertBefore(insertedNode, oneNode));
        oneNode.getParentNode().removeChild(oneNode);
    }
    
    public static void swapNodeWithNodes(Node oneNode, List<Node> otherNodes) {
        swapNodeWithNodes(oneNode, otherNodes.toArray(new Node[otherNodes.size()]));
    }

    public static void swapNodeWithDocuments(Node oneNode, Document... otherDocuments) {
        int length = otherDocuments.length;
        Element[] rootElements = new Element[length];
        for (int i = 0; i < length; i++) {
            rootElements[i] = otherDocuments[i].getDocumentElement();
        }

        swapNodeWithNodes(oneNode, rootElements);
    }
    
    public static void swapNodeWithDocuments(Node node, List<Document> documents) {
        swapNodeWithDocuments(node, documents.toArray(new Document[documents.size()]));
    }

    public static String toString(Document document) {
        String string = null;
        try {
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            transformer.setOutputProperty(OutputKeys.METHOD, "xml");
            transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4");
            transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "no");
            transformer.setOutputProperty(OutputKeys.INDENT, "yes");
            transformer.setOutputProperty(OutputKeys.ENCODING, "UTF-8");
            StringWriter stringWriter = new StringWriter();
            transformer.transform(new DOMSource(document), new StreamResult(stringWriter));
            string = stringWriter.getBuffer().toString();
        } catch (IllegalArgumentException | TransformerException | TransformerFactoryConfigurationError e) {
            LOGGER.warn("Error while toString({})", document);
        }
        return string;
    }

    public static Document parseXML(InputStream inputStream) {
        Document document = null;
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            factory.setNamespaceAware(true);
            DocumentBuilder builder = factory.newDocumentBuilder();
            document = builder.parse(inputStream);
            return document;
        } catch (IOException | ParserConfigurationException | SAXException e) {
            LOGGER.warn("Unable to read InputStream {}", inputStream, e);
        }
        return document;
    }
    
    public static Document parse(File file) {
        Document document = null; 
        try {
            return parseXML(new FileInputStream(file));
        } catch (FileNotFoundException e) {
            LOGGER.warn("Unable to read File {}", file, e);
        }
        return document;
    }
    
    public static PrintDocument print(Document document) {
        return new PrintDocument(document);
    }
    
    public static Document create() {
        Document document = null; 
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            factory.setNamespaceAware(true);
            DocumentBuilder builder = factory.newDocumentBuilder();
            document = builder.newDocument();
            return document;
        } catch (ParserConfigurationException e) {
            LOGGER.warn("Unable to create empty XML", e);
        }
        return document;
    }
    
    public static List<Node> asList(NodeList nodeList) {
        List<Node> nodes = Lists.newArrayList();
        int count = nodeList.getLength();
        for (int index = 0; index < count; index++) {
            nodes.add(nodeList.item(index));
        }
        return nodes;
    }
    
    public static <T extends Node> Optional<T> first(NodeList nodeList) {
        return (Optional<T>) asList(nodeList).stream().findFirst();
    }
    
    public static Document clone(Document document) {
        Document clonedDocument = create();
        Node rootNode = document.getDocumentElement();

        Node clonedRootNode = clonedDocument.importNode(rootNode, true);
        clonedDocument.appendChild(clonedRootNode);
        
        return clonedDocument;
    }
    
    

}
