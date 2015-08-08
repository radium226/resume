<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:resume="RESUME" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:xforms="http://www.w3.org/2002/xforms" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:rpt="http://openoffice.org/2005/report" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:officeooo="http://openoffice.org/2009/office" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:css3t="http://www.w3.org/TR/css3-text/">    
    
    <xsl:import href="view.xslt" />
    
    <xsl:import href="author.xslt" />
    <xsl:import href="experience.xslt" />
    <xsl:import href="skills.xslt" />

    <xsl:param name="color1" />
    <xsl:param name="color2" />
    <xsl:param name="color3" />
    
    <xsl:template match="/resume:resume">
        <office:document-content office:version="1.2">
            <office:automatic-styles>
                <style:style style:name="Auteur_du_Curriculum_Vitae" style:family="table" style:master-page-name="A4_Page">
                    <style:table-properties style:width="18.002cm" style:page-number="auto" table:align="margins"/>
                </style:style>
                
                <style:style style:name="Skills_Domain" style:family="section">
                    <style:section-properties text:dont-balance-text-columns="false" style:editable="false">
                        <style:columns fo:column-count="3" fo:column-gap="0.497cm">
                            <style:column-sep style:width="0.001cm" style:height="100%" style:style="solid">
                                <xsl:attribute name="color" namespace="urn:oasis:names:tc:opendocument:xmlns:style:1.0">
                                    <xsl:value-of select="$color1" />
                                </xsl:attribute>
                            </style:column-sep>
                            <style:column style:rel-width="3402*" fo:start-indent="0cm" fo:end-indent="0.249cm"/>
                            <style:column style:rel-width="3402*" fo:start-indent="0.249cm" fo:end-indent="0.249cm"/>
                            <style:column style:rel-width="3402*" fo:start-indent="0.249cm" fo:end-indent="0cm"/>
                        </style:columns>
                    </style:section-properties>
                </style:style>
                
                <style:style style:name="Job" style:family="section">
                    <style:section-properties text:dont-balance-text-columns="false" style:editable="false">
                        <style:columns fo:column-count="2">
                            <style:column-sep style:width="0.001cm" style:height="100%" style:style="solid">
                                <xsl:attribute name="color" namespace="urn:oasis:names:tc:opendocument:xmlns:style:1.0">
                                    <xsl:value-of select="$color1" />
                                </xsl:attribute>
                            </style:column-sep>
                            <style:column style:rel-width="6235*" fo:start-indent="0cm" fo:end-indent="0.249cm"/>
                            <style:column style:rel-width="3970*" fo:start-indent="0.249cm" fo:end-indent="0cm"/>
                        </style:columns>
                    </style:section-properties>
                </style:style>
                
                <style:style style:name="Technical_Environement.Column_Break" style:family="paragraph" style:parent-style-name="Technical_Environement" style:list-style-name="Technical_Environement">
                    <style:paragraph-properties fo:break-before="column"/>
                </style:style>
                
                <style:style style:name="Skills.Domain.Group.Table" style:family="table">
                    <style:table-properties style:width="5.669cm" table:align="margins"/>
                </style:style>
                <style:style style:name="Skills.Domain.Group.Table.Left_Column" style:family="table-column">
                    <style:table-column-properties style:column-width="4.249cm" style:rel-column-width="2409*"/>
                </style:style>
                <style:style style:name="Skills.Domain.Group.Table.Right_Column" style:family="table-column">
                    <style:table-column-properties style:column-width="1.42cm" style:rel-column-width="805*"/>
                </style:style>
                
            </office:automatic-styles>
            <office:body>
                <office:text text:use-soft-page-breaks="true">
                    <xsl:apply-templates select="resume:author" />
                    <xsl:apply-templates select="resume:experience" />
                    <xsl:apply-templates select="resume:skills" />
                </office:text>
            </office:body>
        </office:document-content>
    </xsl:template>
    
</xsl:stylesheet>
