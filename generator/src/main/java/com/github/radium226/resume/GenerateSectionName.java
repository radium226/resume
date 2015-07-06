/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.github.radium226.resume;

import com.github.radium226.xml.XPaths;
import com.github.radium226.xml.XML;
import com.google.common.base.Joiner;
import com.google.common.base.Splitter;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.stream.Collectors;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactoryConfigurationException;
import net.sf.saxon.dom.DOMNodeWrapper;
import net.sf.saxon.expr.XPathContext;
import net.sf.saxon.lib.ExtensionFunctionCall;
import net.sf.saxon.lib.ExtensionFunctionDefinition;
import net.sf.saxon.om.Item;
import net.sf.saxon.om.LazySequence;
import net.sf.saxon.om.Sequence;
import net.sf.saxon.om.SequenceIterator;
import net.sf.saxon.om.StructuredQName;
import net.sf.saxon.trans.XPathException;
import net.sf.saxon.value.SequenceType;
import net.sf.saxon.value.StringValue;
import org.w3c.dom.DOMException;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import static com.github.radium226.xml.XPaths.*;
import java.util.concurrent.atomic.AtomicInteger;

/**
 *
 * @author adrien
 */
public class GenerateSectionName extends ExtensionFunctionDefinition {

    private AtomicInteger counter = new AtomicInteger(0);
    
    @Override
    public StructuredQName getFunctionQName() {
        return new StructuredQName("resume", "RESUME", "office-generate-section-name");
    }

    @Override
    public SequenceType[] getArgumentTypes() {
        return new SequenceType[] {};
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
                return new StringValue("Section_" + Integer.toString(counter.incrementAndGet()));
            }
            
        };
    }
    
}
