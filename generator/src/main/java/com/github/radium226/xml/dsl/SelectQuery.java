package com.github.radium226.xml.dsl;

import com.github.radium226.xml.XML;
import com.google.common.collect.BiMap;
import com.google.common.collect.HashBiMap;
import com.google.common.collect.ImmutableBiMap;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.Iterators;
import java.util.Iterator;
import java.util.List;
import javax.xml.XMLConstants;
import javax.xml.namespace.NamespaceContext;
import javax.xml.namespace.QName;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;
import javax.xml.xpath.XPathFactoryConfigurationException;
import net.sf.saxon.lib.NamespaceConstant;
import net.sf.saxon.xpath.XPathFactoryImpl;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class SelectQuery {

    public class WithNamespaces {
        
        private BiMap<String, String> namespaces = HashBiMap.create();
        
        public WithNamespaces(BiMap<String, String> namespaces) {
            super();
            
            this.namespaces = namespaces;
        }
        
        public OnNode on(Node node) {
            return new OnNode(this.namespaces, node);
        }
        
    }
    
    public class OnNode {
    
        private Node node;
        private BiMap<String, String> uriByPrefix;
        
        public OnNode(BiMap<String, String> namespaces, Node node) {
            super();
            
            this.node = node;
            this.uriByPrefix = namespaces;
        }
        
        public <T> T as(QName qName) throws XPathExpressionException {
            XPathFactory factory = XPathFactory.newInstance(); //NamespaceConstant.OBJECT_MODEL_SAXON);
            XPath xPath = factory.newXPath();
            xPath.setNamespaceContext(new NamespaceContext() {

                @Override
                public String getNamespaceURI(String prefix) {
                    System.out.println("prefix = " + prefix);
                    String uri = XMLConstants.NULL_NS_URI;
                    if (uriByPrefix.containsKey(prefix)) {
                        uri = uriByPrefix.get(prefix);
                    }
                    return uri;
                }

                @Override
                public String getPrefix(String uri) {
                    System.out.println("uri = " + uri);
                    BiMap<String, String> prefixByURI = uriByPrefix.inverse();
                    String prefix  = null; 
                    if (prefixByURI.containsKey(uri)) {
                        prefix = prefixByURI.get(uri);
                    }
                    return prefix;
                }

                @Override
                public Iterator getPrefixes(String namespaceURI) {
                   return Iterators.singletonIterator(getPrefix(namespaceURI));
                }
            });
            XPathExpression expression = xPath.compile(SelectQuery.this.expression);
            T result = (T) expression.evaluate(this.node, qName);
            return result;
        }
        
        public Node asNode() throws XPathExpressionException, XPathFactoryConfigurationException {
            return as(XPathConstants.NODE);
        }
        
        public List<Node> asNodes() throws XPathExpressionException {
            return XML.asList(asNodeList());
        }
        
        public NodeList asNodeList() throws XPathExpressionException {
            return as(XPathConstants.NODESET);
        }
    
    }
    
    private String expression;
    
    public SelectQuery(String expression) {
        super();
        
        this.expression = expression;
    }
    
    public WithNamespaces using(BiMap<String, String>... namespaces) {
        ImmutableBiMap.Builder<String, String> builder = ImmutableBiMap.<String, String>builder();
        for (BiMap<String, String> namespace : namespaces) {
            builder.putAll(namespace);
        }
        return new WithNamespaces(builder.build());
    }
    
    public OnNode on(Node node) {
        return new OnNode(HashBiMap.create(), node);
    }
    
}
