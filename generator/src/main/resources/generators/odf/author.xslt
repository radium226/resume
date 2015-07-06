<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:view="VIEW" xmlns:resume="RESUME" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:xforms="http://www.w3.org/2002/xforms" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:rpt="http://openoffice.org/2005/report" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:officeooo="http://openoffice.org/2009/office" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:css3t="http://www.w3.org/TR/css3-text/">    
    <xsl:template match="resume:author">
        <table:table table:name="Auteur_du_Curriculum_Vitae" table:style-name="Auteur_du_Curriculum_Vitae">
            <table:table-column table:number-columns-repeated="2"/>
            <table:table-column />
            <table:table-row>
                <table:table-cell office:value-type="string">
                    <text:p>
                        <text:span>
                            <xsl:value-of select="resume:contact/resume:address/resume:street" />
                        </text:span>
                        <text:line-break/>
                        <text:span>
                            <text:span>
                                <xsl:value-of select="resume:contact/resume:address/resume:city/resume:code" />
                            </text:span>
                            <text:span>
                                <xsl:value-of select="resume:contact/resume:address/resume:city/resume:name" />
                            </text:span>
                        </text:span>
                    </text:p>
                    <text:p>
                        <text:span>
                            <xsl:value-of select="resume:contact/resume:phone" />
                        </text:span>
                    </text:p>
                    <text:p>
                        <text:span>
                            <xsl:value-of select="resume:contact/resume:email" />
                        </text:span>
                    </text:p>
                </table:table-cell>
                <table:table-cell table:style-name="Titre.B1" office:value-type="string">
                    <text:p text:style-name="Title">
                        <text:span>
                            <xsl:value-of select="resume:name/resume:first" />
                        </text:span>
                        <text:span>
                            <xsl:value-of select="resume:name/resume:last" />
                        </text:span>
                    </text:p>
                    <text:p text:style-name="Subtitle">
                        <text:span>
                            <xsl:value-of select="../resume:title" />
                        </text:span>
                    </text:p>
                </table:table-cell>
                <table:table-cell office:value-type="string">
                    <text:p>Né le <xsl:value-of select="resume:date-format(resume:birth/resume:date)"/>
                        <text:line-break/> à <xsl:value-of select="resume:location-format(resume:birth/resume:location)"/>
                    </text:p>
                    <text:p>Nationalité <xsl:value-of select="lower-case(resume:nationality)" /></text:p>
                </table:table-cell>
            </table:table-row>
        </table:table>
    </xsl:template>
</xsl:stylesheet>
