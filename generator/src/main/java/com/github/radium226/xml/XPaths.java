package com.github.radium226.xml;

import com.github.radium226.xml.dsl.SelectQuery;
import com.google.common.collect.BiMap;
import com.google.common.collect.ImmutableBiMap;

public final class XPaths {
    
    private XPaths() {
        super();
    }
    
    public static SelectQuery evaluate(String expression) {
        return new SelectQuery(expression);
    }
    
    public static BiMap<String, String> namespace(String prefix, String uri) {
        return ImmutableBiMap.<String, String>builder()
                .put(prefix, uri)
            .build();
    }
    
}
