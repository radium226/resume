<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:view="VIEW" xmlns:resume="RESUME" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:xforms="http://www.w3.org/2002/xforms" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:rpt="http://openoffice.org/2005/report" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:officeooo="http://openoffice.org/2009/office" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:css3t="http://www.w3.org/TR/css3-text/">    
    
    <xsl:template match="view:paragraph">
        <xsl:param name="paragraph-style" />
        <xsl:param name="column-break-paragraph-style" />
        
        <xsl:param name="item-depth" select="1" />
        <xsl:param name="item-position" select="1" />
        
        <text:p>
            <xsl:attribute name="style-name" namespace="urn:oasis:names:tc:opendocument:xmlns:text:1.0" >
                <xsl:choose>
                    <xsl:when test="$item-depth = 1 and $item-position = 1 and $column-break-paragraph-style != ''">
                        <xsl:value-of select="$column-break-paragraph-style" />
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of select="$paragraph-style" />
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:apply-templates select="view:*|text()" />
        </text:p>
    </xsl:template>
    
    <xsl:template match="view:list">
        <xsl:param name="paragraph-style"/>
        <xsl:param name="column-break-paragraph-style" />
        
        <xsl:param name="item-depth" select="1" />
        
        <text:list>
            <xsl:for-each select="view:item">
                <xsl:variable name="item-position" select="position()" />
                <xsl:apply-templates select=".">
                    <xsl:with-param name="paragraph-style" select="$paragraph-style" />
                    <xsl:with-param name="column-break-paragraph-style" select="$column-break-paragraph-style"/>
                    
                    <xsl:with-param name="item-position" select="$item-position" />
                    <xsl:with-param name="item-depth" select="$item-depth + 1" />
                </xsl:apply-templates>
            </xsl:for-each>
        </text:list>
    </xsl:template>
    
    <xsl:template match="view:emphasis">
        <xsl:param name="paragraph-style" tunnel="yes"/>
        <text:span text:style-name="Emphasis">
            <xsl:apply-templates select="view:*|text()" />
        </text:span>
    </xsl:template>
    
    <xsl:template match="view:item">
        <xsl:param name="paragraph-style"/>
        <xsl:param name="column-break-paragraph-style" />
        
        <xsl:param name="item-depth" select="1" />
        <xsl:param name="item-position" select="1" />
        
        <text:list-item>
<!--            <xsl:choose>
                <xsl:when test="node()[position() = 1 and self::text()]">
                    <text:p>
                        <xsl:attribute name="style-name" namespace="urn:oasis:names:tc:opendocument:xmlns:text:1.0" >
                            <xsl:choose>
                                <xsl:when test="$item-depth = 1 and $item-position = 1 and $column-break-paragraph-style != ''">
                                    <xsl:value-of select="$column-break-paragraph-style" />
                                </xsl:when>
                                <xsl:otherwise>
                                    <xsl:value-of select="$paragraph-style" />
                                </xsl:otherwise>
                            </xsl:choose>
                        </xsl:attribute>
                        <xsl:apply-templates select="view:*|text()" />
                    </text:p>
                </xsl:when>
                <xsl:otherwise>-->
                    <xsl:apply-templates select="view:*|text()">
                        <xsl:with-param name="paragraph-style" select="$paragraph-style" />
                        <xsl:with-param name="column-break-paragraph-style" select="$column-break-paragraph-style"/>
                    
                        <xsl:with-param name="item-position" select="$item-position" />
                        <xsl:with-param name="item-depth" select="$item-depth" />
                    </xsl:apply-templates>
<!--                </xsl:otherwise>
            </xsl:choose>-->
        </text:list-item>
    </xsl:template>
    
</xsl:stylesheet>
