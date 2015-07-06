<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:view="VIEW" xmlns:resume="RESUME" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:xforms="http://www.w3.org/2002/xforms" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:rpt="http://openoffice.org/2005/report" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:officeooo="http://openoffice.org/2009/office" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:css3t="http://www.w3.org/TR/css3-text/">    
    <xsl:template match="resume:highlight">
        <xsl:param name="style" tunnel="yes"/>
        <text:list-item>
            <xsl:apply-templates select="view:*|text()">
                <xsl:with-param name="style" select="$style" tunnel="yes" />
            </xsl:apply-templates>
        </text:list-item>
    </xsl:template>
    
    <xsl:template match="resume:job">
        <text:section> <!-- Container -->
            <xsl:attribute name="name" namespace="urn:oasis:names:tc:opendocument:xmlns:text:1.0" >
                <xsl:value-of select="resume:office-generate-section-name()" />
            </xsl:attribute>
                
            <text:h text:outline-level="3">
                <text:span text:style-name="Job_Period">De <xsl:value-of select="resume:date-format(resume:period/resume:from/resume:*[1])"/> à <xsl:value-of select="resume:date-format(resume:period/resume:to/resume:*[1])" /></text:span>
                <text:tab/> 
                <text:span text:style-name="Job_Project">
                    <xsl:value-of select="resume:project" />
                </text:span>
                <text:tab/> 
                <text:span text:style-name="Job_Customer">
                    <xsl:value-of select="resume:customer"/>
                </text:span>
            </text:h>
        
            <table:table>
                <table:table-column table:number-columns-repeated="2"/>
                <table:table-row>
                    <!-- Résumé -->
                    <table:table-cell office:value-type="string">
                        <xsl:apply-templates select="resume:summary" />
                    </table:table-cell>
                    <!-- Environnement technique -->
                    <table:table-cell table:number-rows-spanned="2" office:value-type="string">
                        <text:list text:style-name="Technical_Environement_List">
                            <xsl:for-each select="resume:highlights/resume:highlight[@type = 'technical']">
                                <xsl:variable name="paragraph-style">Technical_Environement</xsl:variable>
                                <xsl:apply-templates select=".">
                                    <xsl:with-param name="paragraph-style" select="$paragraph-style" tunnel="yes"/> 
                                </xsl:apply-templates>
                            </xsl:for-each>
                        </text:list>
                    </table:table-cell>
                </table:table-row>
                <table:table-row>
                    <!-- Participation -->
                    <table:table-cell office:value-type="string">
                        <text:list text:style-name="Involvement">
                            <xsl:apply-templates select="resume:highlights/resume:highlight[@type = 'involvement']">
                                <xsl:with-param name="paragraph-style" select="Involvement" tunnel="yes"/> 
                            </xsl:apply-templates>
                        </text:list>
                    </table:table-cell>
                    <table:covered-table-cell/>
                </table:table-row>
            </table:table>
        </text:section>
    </xsl:template>
    
    <xsl:template match="resume:summary">
        <xsl:choose>
            <xsl:when test="node()[position() = 1 and not(self::view:paragraph)]">
                <text:p>
                    <xsl:apply-templates select="view:*|text()" />
                </text:p>
            </xsl:when>
            <xsl:otherwise>
                <xsl:apply-templates select="view:*|text()" />
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
    
    <xsl:template name="loop-until-other-employer">
        <xsl:param name="position" />
        <xsl:param name="employer" />
        <xsl:param name="jobs" />
        
        <!-- We recursively go on -->
        <xsl:if test="$jobs/resume:job[$position]/resume:employer/text() = $employer">
            <xsl:apply-templates select="$jobs/resume:job[$position]" />
            <xsl:if test="$position &lt; count($jobs/resume:job) ">
            
                <xsl:call-template name="loop-until-other-employer">
                    <xsl:with-param name="jobs" select="$jobs" />
                    <xsl:with-param name="position" select="$position + 1" />
                    <xsl:with-param name="employer" select="$employer" />
                </xsl:call-template>
            </xsl:if>
        </xsl:if>
    </xsl:template>

    <xsl:template name="group-jobs-by-period-and-employer">
        <xsl:param name="jobs" />

        <!-- We sort by period/from -->
        <xsl:variable name="sorted-jobs">
            <xsl:for-each select="$jobs/resume:job">
                <xsl:sort select="resume:period/resume:from/resume:date/resume:year" order="descending"/>
                <xsl:copy-of select="current()"/>
            </xsl:for-each>
        </xsl:variable>

        <!-- We call the loop-until-different-employer template for each distinct employer -->
        <xsl:for-each select="$sorted-jobs/resume:job">
            <xsl:variable name="next-employer" select="(preceding-sibling::resume:job[1]/resume:employer/text(), '')[1]" />
            <xsl:choose>
                <xsl:when test="$next-employer != resume:employer/text()">
                    <text:h text:outline-level="2" style:name="Heading_2">
                        <xsl:value-of select="resume:employer"/>
                    </text:h>
                    <text:section>
                        <xsl:attribute name="name" namespace="urn:oasis:names:tc:opendocument:xmlns:text:1.0" >
                            <xsl:value-of select="resume:office-generate-section-name()" />
                        </xsl:attribute>
                    
                    <xsl:call-template name="loop-until-other-employer">
                        <xsl:with-param name="jobs" select="$sorted-jobs" />
                        <xsl:with-param name="position" select="position()" />
                        <xsl:with-param name="employer" select="resume:employer/text()" />
                    </xsl:call-template>
                    </text:section>
                </xsl:when>
            </xsl:choose>
        </xsl:for-each>

    </xsl:template>

    <xsl:template match="resume:experience">
        <text:h text:outline-level="1" style:name="Heading_1">Expérience professionnelle</text:h>
        <xsl:call-template name="group-jobs-by-period-and-employer">
            <xsl:with-param name="jobs" select="current()" />
        </xsl:call-template>
    </xsl:template>
    
</xsl:stylesheet>
