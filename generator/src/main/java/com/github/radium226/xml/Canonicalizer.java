package com.github.radium226.xml;

import com.google.common.base.Strings;
import com.google.common.collect.HashMultimap;
import com.google.common.collect.Iterables;
import com.google.common.collect.Lists;
import com.google.common.collect.Maps;
import com.google.common.collect.Multimap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.traversal.DocumentTraversal;
import org.w3c.dom.traversal.NodeFilter;
import org.w3c.dom.traversal.NodeIterator;

public class Canonicalizer {

    public Canonicalizer() {
        super();
    }
    
    public Document canonicalize(Document document) {
        Document canonicalizedDocument = XML.clone(document);
        
        Map<String, String> prefixByNamespace = mapPrefixesByNamespace(canonicalizedDocument);
        DocumentTraversal documentTraversal = (DocumentTraversal) canonicalizedDocument;
        NodeIterator nodeIterator = documentTraversal.createNodeIterator(canonicalizedDocument, NodeFilter.SHOW_ELEMENT, null, false);
        for (Node node = nodeIterator.nextNode(); node != null; node = nodeIterator.nextNode()) {
            String namespace = node.getNamespaceURI();
            String prefix = Strings.nullToEmpty(prefixByNamespace.get(namespace));
            String name = node.getLocalName();
            
            if (!prefix.isEmpty()) {
                name = prefix + ":" + name;
            }
            
            canonicalizedDocument.renameNode(node, namespace, name);
            
            NamedNodeMap attributes = node.getAttributes();
            int attributeCount = attributes.getLength();
            List<String> attributeNames = Lists.newArrayList();
            for (int index = 0; index < attributeCount; index++) {
                Node attribute = attributes.item(index);
                String attributeName = attribute.getNodeName();
                if (attributeName.startsWith("xmlns")) {
                    attributeNames.add(attributeName);
                }
            }
            attributeNames.forEach(attributeName -> attributes.removeNamedItem(attributeName));
        }
        
        //element.setAttributeNS("http://www.w3.org/2000/xmlns/", "xmlns:acme", "http://www.acme.com/schemas");
        Element rootElement = canonicalizedDocument.getDocumentElement();
        for (Map.Entry<String, String> entry : prefixByNamespace.entrySet()) {
            String name = "xmlns";
            String prefix = entry.getValue();
            if (!prefix.isEmpty()) {
                name = name + ":" + prefix;
            }
            String namespace = entry.getKey();
            rootElement.setAttributeNS("http://www.w3.org/2000/xmlns/", name, namespace);
        }
        
        NodeIterator textNodeIterator = documentTraversal.createNodeIterator(canonicalizedDocument, NodeFilter.SHOW_TEXT, null, false);
        for (Node textNode = textNodeIterator.nextNode(); textNode != null; textNode = textNodeIterator.nextNode()) {
            String content = textNode.getTextContent();
            if (Strings.nullToEmpty(content).trim().isEmpty()) {
                textNode.getParentNode().removeChild(textNode);
            }
        }
        
        return canonicalizedDocument;
    }
    
    protected Map<String, String> mapPrefixesByNamespace(Document document) {
        Multimap<String, String> prefixesByNamespace = HashMultimap.create();
        DocumentTraversal documentTraversal = (DocumentTraversal) document;
        NodeIterator nodeIterator = documentTraversal.createNodeIterator(document, NodeFilter.SHOW_ALL, null, false);
        for (Node node = nodeIterator.nextNode(); node != null; node = nodeIterator.nextNode()) {
            String namespace = Strings.nullToEmpty(node.getNamespaceURI());
            String prefix = Strings.nullToEmpty(node.getPrefix());
            prefixesByNamespace.put(namespace, prefix);
        }
        
        Set<String> namespaces = prefixesByNamespace.entries().stream()
                .filter(entry -> !entry.getKey().isEmpty())
                .filter(entry -> !entry.getValue().isEmpty())
                .map(entry -> entry.getKey())
            .collect(Collectors.toSet());
        
        prefixesByNamespace.remove("", "");
        
        // TODO: Be more intelligent while choosing prefix
        namespaces.forEach(namespace -> prefixesByNamespace.remove(namespace, "")); 
        Map<String, String> prefixByNamespace = Maps.transformEntries(prefixesByNamespace.asMap(), (namespace, prefixes) -> Iterables.get(prefixes, 0));
       
        return prefixByNamespace;
    }
    
}
