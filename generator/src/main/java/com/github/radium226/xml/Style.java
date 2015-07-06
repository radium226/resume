package com.github.radium226.xml;

import com.github.radium226.xml.Stylizer;
import javax.xml.transform.OutputKeys;

public enum Style {

    PRETTY(transformer -> {
        transformer.setOutputProperty(OutputKeys.METHOD, "xml");
        transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4");
        transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "no");
        transformer.setOutputProperty(OutputKeys.INDENT, "yes");
        transformer.setOutputProperty(OutputKeys.ENCODING, "UTF-8");
    });

    private final Stylizer stylizer;

    Style(Stylizer stylizer) {
        this.stylizer = stylizer;
    }

    public Stylizer getStylizer() {
        return this.stylizer;
    }

}
