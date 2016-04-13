package com.github.radium226.xml;

import com.google.common.collect.Lists;
import java.io.File;
import java.io.FileInputStream;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.traversal.DocumentTraversal;
import org.w3c.dom.traversal.NodeFilter;
import org.w3c.dom.traversal.NodeIterator;

public class IncludeResolver {

    public static final String NAMESPACE_URI = "INCLUDE";

    public static enum ElementName {

        INCLUDE_FRAGMENTS("include-fragments"), 
        INCLUDE_FRAGMENT("include-fragment");

        private final String name;

        ElementName(String name) {
            this.name = name;
        }

        public String getName() {
            return this.name;
        }

        public static ElementName byName(String name) {
            return Arrays.asList(ElementName.values()).stream().filter(tag -> tag.getName().equals(name)).findFirst().get();
        }

        public static ElementName of(Node node) {
            return byName(node.getLocalName());
        }

    }

    private File workingFolder;

    public IncludeResolver(File workingFolder) {
        super();

        this.workingFolder = workingFolder;
    }

    public Document resolveIncludes(Document inputDocument) {
        Document outputDocument = XML.clone(inputDocument);
        
        DocumentTraversal documentTraversal = (DocumentTraversal) outputDocument;
        NodeIterator nodeIterator = documentTraversal.createNodeIterator(outputDocument, NodeFilter.SHOW_ELEMENT, node -> {
            String namespaceURI = node.getNamespaceURI();
            return namespaceURI != null && namespaceURI.equals(NAMESPACE_URI) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
        }, false);

        for (Node node = nodeIterator.nextNode(); node != null; node = nodeIterator.nextNode()) {
            Element element = (Element) node;
            switch (ElementName.of(element)) {
                case INCLUDE_FRAGMENTS:
                    String folderPath = element.getAttribute("folder-path");
                    File folder = new File(workingFolder, folderPath);
                    List<Document> fragmentDocuments = Arrays.asList(folder.listFiles((parentFolder, fileName) -> fileName.endsWith("xml"))).stream().map(file -> XML.parse(file)).collect(Collectors.toList());
                    List<Node> fragmentNodes = Lists.newArrayList();
                    fragmentDocuments.forEach((Document fragmentDocument) -> fragmentNodes.addAll(XML.asList(fragmentDocument.getDocumentElement().getChildNodes())));
                    XML.swapNodeWithNodes(element, fragmentNodes);
                    break;
                case INCLUDE_FRAGMENT:
                    String filePath = element.getAttribute("file-path");
                    Document fragmentDocument = XML.parse(new File(workingFolder, filePath));
                    XML.swapNodeWithNodes(element, XML.asList(fragmentDocument.getDocumentElement().getChildNodes()));
                    break;
            }
        }
        
        return outputDocument;
    }

}
