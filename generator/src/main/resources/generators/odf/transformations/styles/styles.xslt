<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:resume="RESUME" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:xforms="http://www.w3.org/2002/xforms" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:rpt="http://openoffice.org/2005/report" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:officeooo="http://openoffice.org/2009/office" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:css3t="http://www.w3.org/TR/css3-text/">    
    
    <xsl:import href="../commons/author.xslt" />
    <xsl:import href="../commons/skills.xslt" />
    <xsl:import href="../commons/experience.xslt" />
    
    <xsl:param name="color1" />
    <xsl:param name="color2" />
    <xsl:param name="color3" />
    
    <xsl:template match="/resume:resume">
        <office:document-styles xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:rpt="http://openoffice.org/2005/report" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:officeooo="http://openoffice.org/2009/office" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:css3t="http://www.w3.org/TR/css3-text/" office:version="1.2">
            <office:font-face-decls>
                <style:font-face style:name="Ubuntu" svg:font-family="Ubuntu" style:font-adornments="Normal" style:font-pitch="variable"/>
            </office:font-face-decls>
            <office:styles>
                <!-- Headings -->
                <style:style style:name="Heading" style:family="paragraph" style:parent-style-name="Standard" style:next-style-name="Text_Body" style:class="text" style:master-page-name="">
                    <style:paragraph-properties fo:margin-top="0cm" fo:margin-bottom="0.131cm" loext:contextual-spacing="false" fo:text-align="start" style:justify-single-word="false" style:page-number="auto" style:shadow="none">
                        <style:tab-stops/>
                    </style:paragraph-properties>
                    <style:text-properties fo:font-size="8pt" style:font-size-asian="10.5pt"/>
                </style:style>
                <style:style style:name="Heading_1" style:display-name="Heading 1" style:family="paragraph" style:parent-style-name="Heading" style:next-style-name="Text_Body" style:default-outline-level="1" style:class="text" style:master-page-name="">
                    <style:paragraph-properties fo:margin-left="-0.379cm" fo:margin-right="-0.131cm" fo:margin-top="0.25cm" fo:margin-bottom="0.131cm" loext:contextual-spacing="false" fo:text-align="start" style:justify-single-word="false" fo:text-indent="0cm" style:auto-text-indent="false" style:page-number="auto" fo:padding="0.131cm" fo:border-left="none" fo:border-right="none" fo:border-top="none" style:shadow="none" fo:keep-with-next="always">
                        <xsl:attribute name="border-bottom" namespace="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0">
                            <xsl:value-of select="concat('0.26pt solid ', $color2)" />
                        </xsl:attribute>
                        <style:tab-stops/>
                    </style:paragraph-properties>
                    <style:text-properties fo:text-transform="uppercase" fo:letter-spacing="0.071cm" fo:font-weight="bold" style:font-size-asian="10.5pt"/>
                </style:style>
                <style:style style:name="Heading_2" style:display-name="Heading 2" style:family="paragraph" style:parent-style-name="Heading" style:next-style-name="Text_Body" style:default-outline-level="2" style:class="text" style:master-page-name="">
                    <style:paragraph-properties fo:margin-left="-0.25cm" fo:margin-right="-0.25cm" fo:margin-top="0.131cm" fo:margin-bottom="0.131cm" loext:contextual-spacing="false" fo:keep-together="always" fo:text-indent="0cm" style:auto-text-indent="false" style:page-number="auto" fo:padding="0.131cm" fo:border-left="none" fo:border-right="none" fo:border-top="none" fo:border-bottom="0.26pt solid #f5f591" style:shadow="none" fo:keep-with-next="always">
                        <style:tab-stops/>
                    </style:paragraph-properties>
                    <style:text-properties fo:text-transform="uppercase" fo:font-size="8pt" fo:letter-spacing="0.071cm" fo:font-weight="bold" style:font-size-asian="10.5pt"/>
                </style:style>
                <style:style style:name="Heading_3" style:display-name="Heading 3" style:family="paragraph" style:parent-style-name="Heading" style:next-style-name="Text_Body" style:default-outline-level="3" style:class="text" style:master-page-name="">
                    <style:paragraph-properties fo:margin-left="-0.131cm" fo:margin-right="0cm" fo:margin-top="0cm" fo:margin-bottom="0.131cm" loext:contextual-spacing="false" fo:keep-together="always" fo:text-indent="0cm" style:auto-text-indent="false" style:page-number="auto" fo:padding="0cm" fo:border="none" style:shadow="none" fo:keep-with-next="always">
                        <style:tab-stops>
                            <style:tab-stop style:position="11cm" style:type="center"/>
                            <style:tab-stop style:position="18cm" style:type="right"/>
                        </style:tab-stops>
                    </style:paragraph-properties>
                    <style:text-properties style:font-size-asian="10.5pt"/>
                </style:style>
        
                <!-- Titles -->
                <style:style style:name="Title" style:family="paragraph" style:parent-style-name="Heading" style:next-style-name="Subtitle" style:class="chapter">
                    <style:paragraph-properties fo:text-align="center" style:justify-single-word="false" fo:padding="0.131cm" fo:border-left="none" fo:border-right="none" fo:border-top="none" fo:border-bottom="0.26pt solid #f5f591" style:shadow="none"/>
                    <style:text-properties fo:font-size="12pt" fo:font-weight="bold" style:font-size-asian="18pt" style:font-weight-asian="bold" style:font-size-complex="18pt" style:font-weight-complex="bold"/>
                </style:style>
                <style:style style:name="Subtitle" style:family="paragraph" style:parent-style-name="Heading" style:next-style-name="Text_20_body" style:class="chapter">
                    <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
                    <style:text-properties fo:font-size="9pt" style:font-size-asian="10.5pt"/>
                </style:style>
        
                <!-- Lists -->
                <style:style style:name="List" style:family="paragraph" style:parent-style-name="Text_Body" style:class="list">
                    <style:text-properties style:font-size-asian="12pt" style:font-name-complex="Mangal1" style:font-family-complex="Mangal"/>
                </style:style>
                <style:style style:name="Bullet_Symbols" style:display-name="Bullet Symbols" style:family="text">
                    <style:text-properties style:font-name="OpenSymbol1" fo:font-family="OpenSymbol" style:font-name-asian="OpenSymbol1" style:font-family-asian="OpenSymbol" style:font-name-complex="OpenSymbol1" style:font-family-complex="OpenSymbol"/>
                </style:style>
        
                <!-- Frames -->
                <style:style style:name="Frame_Content" style:display-name="Frame contents" style:family="paragraph" style:parent-style-name="Standard" style:class="extra"/>
                <style:style style:name="Frame" style:family="graphic">
                    <style:graphic-properties text:anchor-type="paragraph" svg:x="0cm" svg:y="0cm" fo:margin-left="0.201cm" fo:margin-right="0.201cm" fo:margin-top="0.201cm" fo:margin-bottom="0.201cm" style:wrap="parallel" style:number-wrapped-paragraphs="no-limit" style:wrap-contour="false" style:vertical-pos="top" style:vertical-rel="paragraph-content" style:horizontal-pos="center" style:horizontal-rel="paragraph-content" fo:padding="0.15cm" fo:border="0.06pt solid #000000"/>
                </style:style>    
         
                <!-- Paragraphs -->
                <style:style style:name="Text_Body" style:display-name="Text Body" style:family="paragraph" style:parent-style-name="Standard" style:class="text">
                    <style:paragraph-properties fo:margin-top="0cm" fo:margin-bottom="0.212cm" loext:contextual-spacing="false"/>
                </style:style>
                <style:style style:name="Standard" style:display-name="Standard" style:family="paragraph" style:class="text">
                    <style:paragraph-properties fo:text-align="justify" style:justify-single-word="false"/>
                    <style:text-properties style:font-name="Ubuntu" fo:font-family="Ubuntu" style:font-style-name="Normal" style:font-pitch="variable" fo:font-size="8pt" style:font-size-asian="10.5pt"/>
                </style:style>
        
                <!-- Characters -->
                <style:style style:name="Emphasis" style:family="text">
                    <style:text-properties style:font-size-asian="10.5pt">
                        <xsl:attribute name="color" namespace="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0">
                            <xsl:value-of select="$color2" />
                        </xsl:attribute>
                    </style:text-properties>
                </style:style>
        
                <!-- Skills + Experience + Author -->
                <xsl:call-template name="skills-styles" />
                <xsl:call-template name="experience-styles" />
                <xsl:call-template name="author-styles" />
        
            </office:styles>
            <office:automatic-styles>
                <style:page-layout style:name="A4_Page_Layout">
                    <style:page-layout-properties fo:page-width="21cm" fo:page-height="29.7cm" style:num-format="1" style:print-orientation="portrait" fo:margin-top="1.5cm" fo:margin-bottom="1.5cm" fo:margin-left="1.5cm" fo:margin-right="1.5cm" style:shadow="none" style:writing-mode="lr-tb" draw:fill-image-width="0cm" draw:fill-image-height="0cm" style:footnote-max-height="0cm">
                        <style:columns fo:column-count="1" fo:column-gap="0cm"/>
                        <style:footnote-sep style:width="0.018cm" style:distance-before-sep="0.101cm" style:distance-after-sep="0.101cm" style:line-style="solid" style:adjustment="left" style:rel-width="25%" style:color="#000000"/>
                    </style:page-layout-properties>
                    <style:header-style/>
                    <style:footer-style/>
                </style:page-layout>
            </office:automatic-styles>
            <office:master-styles>
                <style:master-page style:name="A4_Page" style:display-name="Page A4" style:page-layout-name="A4_Page_Layout"/>
            </office:master-styles>
        </office:document-styles>
    </xsl:template>
    
</xsl:stylesheet>
