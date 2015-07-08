/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.github.radium226.resume.odt;

import com.github.radium226.xml.XML;
import com.google.common.base.Joiner;
import com.google.common.base.Splitter;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.stream.Collectors;
import net.sf.saxon.dom.DOMNodeWrapper;
import net.sf.saxon.dom.ElementOverNodeInfo;
import net.sf.saxon.expr.XPathContext;
import net.sf.saxon.lib.ExtensionFunctionCall;
import net.sf.saxon.lib.ExtensionFunctionDefinition;
import net.sf.saxon.om.Item;
import net.sf.saxon.om.LazySequence;
import net.sf.saxon.om.NodeInfo;
import net.sf.saxon.om.Sequence;
import net.sf.saxon.om.SequenceIterator;
import net.sf.saxon.om.StructuredQName;
import net.sf.saxon.trans.XPathException;
import net.sf.saxon.tree.tiny.TinyElementImpl;
import net.sf.saxon.value.SequenceType;
import net.sf.saxon.value.StringValue;
import org.w3c.dom.Element;
import org.w3c.dom.Node;

/**
 *
 * @author adrien
 */
public class FormatDate extends ExtensionFunctionDefinition {

    public FormatDate() {
        super();
    }
    
    @Override
    public StructuredQName getFunctionQName() {
        return new StructuredQName("resume", "RESUME", "date-format");
    }

    @Override
    public SequenceType[] getArgumentTypes() {
        return new SequenceType[] {SequenceType.SINGLE_NODE};
    }

    @Override
    public SequenceType getResultType(SequenceType[] suppliedArgumentTypes) {
        return SequenceType.STRING_SEQUENCE;
    }

    @Override
    public ExtensionFunctionCall makeCallExpression() {
        return new ExtensionFunctionCall() {

            @Override
            public Sequence call(XPathContext context, Sequence[] arguments) throws XPathException {
                SequenceIterator sequenceIterator = arguments[0].iterate();
                for (Item item = sequenceIterator.next(); item !=null; item = sequenceIterator.next()) {
                    
                    System.out.println("item = " + item.toString());
                    
                    NodeInfo node = (NodeInfo) item;
                    
                    if (node.getLocalPart().equals("date")) {
                        Element dateElement = (Element) ElementOverNodeInfo.wrap(node);
                        
                        
                        String yearAsText = XML.first(dateElement.getElementsByTagNameNS("RESUME", "year")).get().getTextContent();
                        String monthAsText = XML.first(dateElement.getElementsByTagNameNS("RESUME", "month")).get().getTextContent();
                        Node dayNode = XML.first(dateElement.getElementsByTagNameNS("RESUME", "day")).orElse(null);
                        if (dayNode != null) {
                            String dayAsText = dayNode.getTextContent();
                            DateFormat inputDateFormat = new SimpleDateFormat("yyyyMMdd");
                            DateFormat outputDateFormat = new SimpleDateFormat("dd MMMM yyyy", Locale.FRENCH);
                            Date date = null; 
                            try {
                                date = inputDateFormat.parse(yearAsText + monthAsText + dayAsText);
                                String formattedDate = outputDateFormat.format(date);
                                return new StringValue(capitalize(formattedDate));
                            } catch (ParseException e) {
                                throw new XPathException(e);
                            }
                        } else {
                            DateFormat inputDateFormat = new SimpleDateFormat("yyyyMM");
                            DateFormat outputDateFormat = new SimpleDateFormat("MMMM yyyy", Locale.FRENCH);
                            Date date = null; 
                            try {
                                date = inputDateFormat.parse(yearAsText + monthAsText);
                                String formattedDate = outputDateFormat.format(date);
                                return new StringValue(capitalize(formattedDate));
                            } catch (ParseException e) {
                                throw new XPathException(e);
                            }
                        }
                    } else {
                        return new StringValue("aujourd'hui");
                    }
                }
                throw new XPathException("Empty iterator! ");
            }
            
        };
    }
    
    public static String capitalize(String text) {
        return Joiner.on(" ").join(Splitter.on(" ").splitToList(text).stream()
                .map(word -> word.substring(0, 1).toUpperCase() + word.substring(1))
            .collect(Collectors.toList()));
    }
    
}
