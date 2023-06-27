"""
<draw:frame draw:style-name="fr1" draw:name="Image8" text:anchor-type="as-char" svg:width="0.0591in" svg:height="0.0591in" draw:z-index="6">
                                            <draw:image xlink:href="Pictures/1000067500003505000035051046D2E1734B0441.svg" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" draw:mime-type="image/svg+xml"/>
                                            <draw:image xlink:href="Pictures/100000010000020100000201A53263065CD4FFF3.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" draw:mime-type="image/png"/>
                                        </draw:frame>
                                        <text:s/>
                                        <draw:frame draw:style-name="fr1" draw:name="Image5" text:anchor-type="as-char" svg:width="0.0591in" svg:height="0.0591in" draw:z-index="7">
                                            <draw:image xlink:href="Pictures/100000FF0000350500003505CAD4341EDB328597.svg" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" draw:mime-type="image/svg+xml"/>
                                            <draw:image xlink:href="Pictures/100000010000020100000201F77EBC869B8BCCF5.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" draw:mime-type="image/png"/>
                                        </draw:frame>
                                        <text:s/>
                                        <draw:frame draw:style-name="fr1" draw:name="Image6" text:anchor-type="as-char" svg:width="0.0591in" svg:height="0.0591in" draw:z-index="8">
                                            <draw:image xlink:href="Pictures/100000FF0000350500003505CAD4341EDB328597.svg" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" draw:mime-type="image/svg+xml"/>
                                            <draw:image xlink:href="Pictures/100000010000020100000201F77EBC869B8BCCF5.png" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad" draw:mime-type="image/png"/>
                                        </draw:frame>
"""

from lxml.etree import Element

from ...xml import create_element


def frame(
    *,
    name: str | None = None,
    style_name: str | None = None,
    width: str | None = None,
    height: str | None = None,
    anchor_type: str = "as-char",
    **kwargs,
) -> Element:
    return create_element(
        tag="draw:frame",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "draw:style-name": style_name,
            "draw:name": name,
            "text:anchor-type": anchor_type,
            "svg:width": width,
            "svg:height": height,
        } },
    )