<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:resume="RESUME" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:xforms="http://www.w3.org/2002/xforms" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:rpt="http://openoffice.org/2005/report" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:officeooo="http://openoffice.org/2009/office" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:css3t="http://www.w3.org/TR/css3-text/">    
    <xsl:param name="color1" />
    <xsl:param name="color2" />
    <xsl:param name="color3" />
    
    <xsl:template name="experience-styles">
        <!-- Environnement technique -->
        <text:list-style style:name="Technical_Environement_List" style:display-name="Environnement technique">
            <text:list-level-style-bullet text:level="1" text:style-name="Technical_Environement_Bullet" text:bullet-char="▪">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment" fo:text-align="center">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="0.499cm" fo:text-indent="-0.249cm" fo:margin-left="0.499cm"/>
                </style:list-level-properties>
                <style:text-properties style:font-name="OpenSymbol"/>
            </text:list-level-style-bullet>
            <text:list-level-style-bullet text:level="2" text:style-name="Technical_Environement_Bullet" text:bullet-char="">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment" fo:text-align="center">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="0.762cm" fo:text-indent="-0.254cm" fo:margin-left="1.016cm"/>
                </style:list-level-properties>
                <style:text-properties style:font-name="OpenSymbol"/>
            </text:list-level-style-bullet>
            <text:list-level-style-number text:level="3" style:num-suffix="." style:num-format="1">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="2.54cm" fo:text-indent="-0.635cm" fo:margin-left="2.54cm"/>
                </style:list-level-properties>
            </text:list-level-style-number>
            <text:list-level-style-number text:level="4" style:num-suffix="." style:num-format="1">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="3.175cm" fo:text-indent="-0.635cm" fo:margin-left="3.175cm"/>
                </style:list-level-properties>
            </text:list-level-style-number>
            <text:list-level-style-number text:level="5" style:num-suffix="." style:num-format="1">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="3.81cm" fo:text-indent="-0.635cm" fo:margin-left="3.81cm"/>
                </style:list-level-properties>
            </text:list-level-style-number>
            <text:list-level-style-number text:level="6" style:num-suffix="." style:num-format="1">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="4.445cm" fo:text-indent="-0.635cm" fo:margin-left="4.445cm"/>
                </style:list-level-properties>
            </text:list-level-style-number>
            <text:list-level-style-number text:level="7" style:num-suffix="." style:num-format="1">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="5.08cm" fo:text-indent="-0.635cm" fo:margin-left="5.08cm"/>
                </style:list-level-properties>
            </text:list-level-style-number>
            <text:list-level-style-number text:level="8" style:num-suffix="." style:num-format="1">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="5.715cm" fo:text-indent="-0.635cm" fo:margin-left="5.715cm"/>
                </style:list-level-properties>
            </text:list-level-style-number>
            <text:list-level-style-number text:level="9" style:num-suffix="." style:num-format="1">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="6.35cm" fo:text-indent="-0.635cm" fo:margin-left="6.35cm"/>
                </style:list-level-properties>
            </text:list-level-style-number>
            <text:list-level-style-number text:level="10" style:num-suffix="." style:num-format="1">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="6.985cm" fo:text-indent="-0.635cm" fo:margin-left="6.985cm"/>
                </style:list-level-properties>
            </text:list-level-style-number>
        </text:list-style>
        <style:style style:name="Technical_Environement" style:display-name="Environnement technique" style:family="paragraph" style:parent-style-name="Text_Body" style:list-style-name="Technical_Environement"/>
        <style:style style:name="Technical_Environement_First" style:display-name="Début de l&apos;environnement technique" style:family="paragraph" style:parent-style-name="Environnement_20_technique"/>
        <style:style style:name="Technical_Environement_Next" style:display-name="Environnement technique suivant" style:family="paragraph" style:parent-style-name="Environnement_20_technique"/>
        <style:style style:name="Technical_Environement_Last" style:display-name="Dernier environnement technique" style:family="paragraph" style:parent-style-name="Environnement_20_technique"/>
        <style:style style:name="Technical_Environement_Bullet" style:family="text" style:parent-style-name="Bullet_Symbols">
            <style:text-properties fo:font-size="7pt" fo:font-weight="bold" style:font-size-asian="10.5pt">
                <xsl:attribute name="color" namespace="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0">
                    <xsl:value-of select="$color2" />
                </xsl:attribute>
            </style:text-properties>
        </style:style>
        <style:style style:name="Job" style:display-name="Mission" style:family="text"/>
        <style:style style:name="Job_Period" style:display-name="Période de la mission" style:family="text" style:parent-style-name="Job">
            <style:text-properties fo:text-transform="lowercase" fo:font-size="8pt" style:font-size-asian="10.5pt"/>
        </style:style>
        <style:style style:name="Job_Project" style:display-name="Projet de la mission" style:family="text" style:parent-style-name="Job">
            <style:text-properties fo:letter-spacing="0.018cm" fo:font-weight="bold" style:font-size-asian="10.5pt"/>
        </style:style>
        <style:style style:name="Job_Customer" style:display-name="Client de la mission" style:family="text" style:parent-style-name="Job">
            <style:text-properties fo:font-variant="small-caps" fo:font-size="8pt" style:font-size-asian="10.5pt"/>
        </style:style>
        <style:style style:name="Job_Table.Left_Column.Paragraph" style:family="paragraph" style:parent-style-name="Text_Body">
            <style:paragraph-properties fo:margin-left="0cm" fo:margin-top="0cm" fo:margin-bottom="0cm" loext:contextual-spacing="false" fo:text-indent="0cm" style:auto-text-indent="false" style:shadow="none">
                <style:tab-stops/>
            </style:paragraph-properties>
            <style:text-properties fo:font-size="8pt"/>
        </style:style>
        
        <style:style style:name="Job.Summary" style:family="paragraph" style:parent-style-name="Job_Table.Left_Column.Paragraph" />
        <style:style style:name="Job.Involvement.Paragraph" style:family="paragraph" style:parent-style-name="Job_Table.Left_Column.Paragraph" style:list-style-name="Job.Involvement.List">
            <style:paragraph-properties fo:margin-left="0.5cm" fo:margin-top="0cm" fo:margin-bottom="0cm" loext:contextual-spacing="false" fo:text-indent="-0.25cm" style:auto-text-indent="false" style:shadow="none">
                <style:tab-stops/>
            </style:paragraph-properties>
            <style:text-properties fo:font-size="8pt"/>
        </style:style>
        <style:style style:name="Job.Involvement" style:family="text" style:parent-style-name="Bullet_Symbols">
            <style:text-properties fo:font-size="7pt" fo:font-weight="bold" style:font-size-asian="10.5pt">
                <xsl:attribute name="color" namespace="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0">
                    <xsl:value-of select="$color2" />
                </xsl:attribute>
            </style:text-properties>
        </style:style>
        <text:list-style style:name="Job.Involvement.List" style:display-name="Tâches principales">
            <text:list-level-style-bullet text:level="1" text:style-name="Technical_Environement_Bullet" text:bullet-char="▪">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment" fo:text-align="center">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="0.499cm" fo:text-indent="-0.249cm" fo:margin-left="0.499cm"/>
                </style:list-level-properties>
                <style:text-properties style:font-name="OpenSymbol"/>
            </text:list-level-style-bullet>
            <text:list-level-style-bullet text:level="2" text:style-name="Technical_Environement_Bullet" text:bullet-char="">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment" fo:text-align="center">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="0.762cm" fo:text-indent="-0.254cm" fo:margin-left="1.016cm"/>
                </style:list-level-properties>
                <style:text-properties style:font-name="OpenSymbol"/>
            </text:list-level-style-bullet>
            <text:list-level-style-number text:level="3" style:num-suffix="." style:num-format="1">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="2.54cm" fo:text-indent="-0.635cm" fo:margin-left="2.54cm"/>
                </style:list-level-properties>
            </text:list-level-style-number>
            <text:list-level-style-number text:level="4" style:num-suffix="." style:num-format="1">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="3.175cm" fo:text-indent="-0.635cm" fo:margin-left="3.175cm"/>
                </style:list-level-properties>
            </text:list-level-style-number>
            <text:list-level-style-number text:level="5" style:num-suffix="." style:num-format="1">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="3.81cm" fo:text-indent="-0.635cm" fo:margin-left="3.81cm"/>
                </style:list-level-properties>
            </text:list-level-style-number>
            <text:list-level-style-number text:level="6" style:num-suffix="." style:num-format="1">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="4.445cm" fo:text-indent="-0.635cm" fo:margin-left="4.445cm"/>
                </style:list-level-properties>
            </text:list-level-style-number>
            <text:list-level-style-number text:level="7" style:num-suffix="." style:num-format="1">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="5.08cm" fo:text-indent="-0.635cm" fo:margin-left="5.08cm"/>
                </style:list-level-properties>
            </text:list-level-style-number>
            <text:list-level-style-number text:level="8" style:num-suffix="." style:num-format="1">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="5.715cm" fo:text-indent="-0.635cm" fo:margin-left="5.715cm"/>
                </style:list-level-properties>
            </text:list-level-style-number>
            <text:list-level-style-number text:level="9" style:num-suffix="." style:num-format="1">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="6.35cm" fo:text-indent="-0.635cm" fo:margin-left="6.35cm"/>
                </style:list-level-properties>
            </text:list-level-style-number>
            <text:list-level-style-number text:level="10" style:num-suffix="." style:num-format="1">
                <style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
                    <style:list-level-label-alignment text:label-followed-by="listtab" text:list-tab-stop-position="6.985cm" fo:text-indent="-0.635cm" fo:margin-left="6.985cm"/>
                </style:list-level-properties>
            </text:list-level-style-number>
        </text:list-style>
    </xsl:template>
    
    <xsl:template name="experience-automatic-styles">
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
        
    </xsl:template>
    
</xsl:stylesheet>