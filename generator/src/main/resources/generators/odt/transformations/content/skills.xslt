<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:view="VIEW" xmlns:resume="RESUME" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:xforms="http://www.w3.org/2002/xforms" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:rpt="http://openoffice.org/2005/report" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:officeooo="http://openoffice.org/2009/office" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:css3t="http://www.w3.org/TR/css3-text/">    
    <xsl:param name="color1" />
    <xsl:param name="color2" />
    <xsl:param name="color3" />
    
    <xsl:template match="resume:skills">
        <text:h text:outline-level="1" style:name="Heading_1">Compétences</text:h>
        <xsl:apply-templates select="resume:domain" />
    </xsl:template>
    
    <xsl:template match="resume:domain">
        <text:h text:outline-level="2" style:name="Heading_2">
            <xsl:value-of select="resume:name" />
        </text:h>
        <text:section text:style-name="Skills_Domain">
            <xsl:attribute name="name" namespace="urn:oasis:names:tc:opendocument:xmlns:text:1.0" >
                <xsl:value-of select="resume:office-generate-section-name()" />
            </xsl:attribute>
            <xsl:apply-templates select="resume:group" />
        </text:section>
    </xsl:template>
    
    <xsl:template match="resume:group">
        
        <text:p text:style-name="Standard">
            <draw:frame draw:style-name="Skills_Domain_Group" draw:name="Frame2" text:anchor-type="as-char" svg:width="8.5cm" style:rel-width="100%" draw:z-index="1">
                <draw:text-box fo:min-height="0.499cm">
                    <text:h text:style-name="Skills_Domain_Group_Heading" text:outline-level="3">
                        <xsl:value-of select="resume:name" />
                    </text:h>
                    <table:table table:style-name="Skills.Domain.Group.Table">
                        <table:table-column table:style-name="Skills.Domain.Group.Table.Left_Column"/>
                        <table:table-column table:style-name="Skills.Domain.Group.Table.Right_Column"/>
                        <xsl:for-each select="resume:skill">
                            <table:table-row>
                                <table:table-cell office:value-type="string">
                                    <text:list>
                                        <text:list-item>
                                            <text:p>
                                                <text:span>
                                                    <xsl:value-of select="resume:name" />
                                                </text:span>
                                            </text:p>
                                            <xsl:if test="count(resume:details/resume:detail) > 0">
                                                <text:list>
                                                    <xsl:for-each select="resume:details/resume:detail">
                                                        <text:list-item>
                                                            <text:p>
                                                                <xsl:value-of select="." />
                                                            </text:p>
                                                        </text:list-item>
                                                    </xsl:for-each>
                                                </text:list>
                                            </xsl:if>
                                        </text:list-item>
                                    </text:list>
                                </table:table-cell>
                                <table:table-cell>
                                    <text:p>
                                        <text:span text:style-name="Skills_Domain_Group_Skill_Note">
                                            <xsl:for-each select="1 to resume:note"></xsl:for-each>
                                        </text:span>
                                    </text:p>
                                </table:table-cell>
                            </table:table-row>
                        </xsl:for-each>
                    </table:table>
                </draw:text-box>
            </draw:frame> 
        </text:p>
    </xsl:template>
</xsl:stylesheet>
