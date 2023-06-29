from lxml.etree import _Element
from functools import partial

from ..models import Publication
from ..open_document import text

from .render_paragraph import render_paragraph


"""
<table:table table:name="Tableau14" table:style-name="Tableau14">
            <table:table-row table:style-name="Tableau14.1">
                <table:table-cell table:style-name="Tableau14.A1" table:number-rows-spanned="2" office:value-type="string">
                    <text:h text:style-name="P15" text:outline-level="2">
                        <text:span text:style-name="T31">Talk </text:span>
                        <text:span text:style-name="Titre_20_de_20_publication">Démystifions Apache Spark !</text:span>
                    </text:h>
                </table:table-cell>
                <table:table-cell table:style-name="Tableau14.B1" office:value-type="string">
                    <text:p text:style-name="Standard">
                        <text:span text:style-name="Format_20_de_20_publication">PerfUG #61</text:span>
                    </text:p>
                </table:table-cell>
                <table:table-cell table:style-name="Tableau14.B1" office:value-type="string">
                    <text:p text:style-name="Standard">
                        <text:span text:style-name="Période_20_de_20_publication">
                            <text:span text:style-name="T23">M</text:span>
                        </text:span>
                        <text:span text:style-name="Période_20_de_20_publication">ars 2019</text:span>
                    </text:p>
                </table:table-cell>
            </table:table-row>
            <table:table-row table:style-name="Tableau14.1">
                <table:covered-table-cell table:style-name="Tableau14.A1"/>
                <table:table-cell table:style-name="Tableau14.A1" office:value-type="string">
                    <text:p text:style-name="Standard">
                        <text:span text:style-name="Format_20_de_20_publication">Devoxx</text:span>
                    </text:p>
                </table:table-cell>
                <table:table-cell table:style-name="Tableau14.A1" office:value-type="string">
                    <text:p text:style-name="Standard">
                        <text:span text:style-name="Période_20_de_20_publication">
                            <text:span text:style-name="T23">a</text:span>
                        </text:span>
                        <text:span text:style-name="Période_20_de_20_publication">vril 2018</text:span>
                    </text:p>
                </table:table-cell>
            </table:table-row>
            <table:table-row table:style-name="Tableau14.1">
                <table:table-cell table:style-name="Tableau14.A1" office:value-type="string">
                    <text:h text:style-name="P15" text:outline-level="2">
                        <text:span text:style-name="T31">Article </text:span>
                        <text:span text:style-name="Titre_20_de_20_publication">Ansible Container: Chronic of a Death Foretold</text:span>
                    </text:h>
                </table:table-cell>
                <table:table-cell table:style-name="Tableau14.A1" office:value-type="string">
                    <text:p text:style-name="Standard">
                        <text:span text:style-name="Format_20_de_20_publication">OCTO Talk!</text:span>
                    </text:p>
                </table:table-cell>
                <table:table-cell table:style-name="Tableau14.A1" office:value-type="string">
                    <text:p text:style-name="Standard">
                        <text:span text:style-name="Période_20_de_20_publication">Juin 2018</text:span>
                    </text:p>
                </table:table-cell>
            </table:table-row>
            <table:table-row table:style-name="Tableau14.1">
                <table:table-cell table:style-name="Tableau14.A1" office:value-type="string">
                    <text:h text:style-name="P15" text:outline-level="2">Articles <text:span text:style-name="Titre_20_de_20_publication">MythBuster: Apache Spark</text:span>
                    </text:h>
                </table:table-cell>
                <table:table-cell table:style-name="Tableau14.A1" office:value-type="string">
                    <text:p text:style-name="Standard">
                        <text:span text:style-name="Format_20_de_20_publication">OCTO Talk!</text:span>
                    </text:p>
                </table:table-cell>
                <table:table-cell table:style-name="Tableau14.A1" office:value-type="string">
                    <text:p text:style-name="Standard">
                        <text:span text:style-name="Période_20_de_20_publication">
                            <text:span text:style-name="T32">De </text:span>
                        </text:span>
                        <text:span text:style-name="Période_20_de_20_publication">août </text:span>
                        <text:span text:style-name="Période_20_de_20_publication">
                            <text:span text:style-name="T32">à </text:span>
                        </text:span>
                        <text:span text:style-name="Période_20_de_20_publication">novembre 2017</text:span>
                    </text:p>
                </table:table-cell>
            </table:table-row>
            <table:table-row table:style-name="Tableau14.1">
                <table:table-cell table:style-name="Tableau14.A1" office:value-type="string">
                    <text:h text:style-name="P15" text:outline-level="2">Article <text:span text:style-name="Titre_20_de_20_publication">5 services que systemd m’a déjà rendu</text:span>
                        <text:span text:style-name="Titre_20_de_20_publication">
                            <text:span text:style-name="T40">s</text:span>
                        </text:span>
                    </text:h>
                </table:table-cell>
                <table:table-cell table:style-name="Tableau14.A1" office:value-type="string">
                    <text:p text:style-name="Standard">
                        <text:span text:style-name="Format_20_de_20_publication">OCTO Talk!</text:span>
                    </text:p>
                </table:table-cell>
                <table:table-cell table:style-name="Tableau14.A1" office:value-type="string">
                    <text:p text:style-name="Standard">
                        <text:span text:style-name="Période_20_de_20_publication">Juillet 2017</text:span>
                    </text:p>
                </table:table-cell>
            </table:table-row>
        </table:table>
"""



def render_publications(publications: list[Publication]) -> list[_Element]:

    def render_publication_as_table_row(publication: Publication) -> _Element:
        print(publication)
        return text.table_row(
            children=[
                text.table_cell(
                    children=render_paragraph(
                        publication.title,
                        style_name="Publication",
                        create_element=partial(text.h, outline_level=2),
                    ),
                ),
                text.table_cell(
                    children=[
                        text.p(
                            children=[f"{publication.medium.name}" if publication.medium else "XXXXXX"],
                        ),
                    ],
                ),
                text.table_cell(
                    children=[
                        text.p(
                            children=[publication.date.format("MMMM YYYY", locale="fr") if publication.date else "XXXXXX"],
                        ),
                    ],
                ),
            ],
        )


    return [
        text.table(
            name="Publications",
            children=(
                [
                    text.table_column(),
                    text.table_column(),
                    text.table_column(),
                ] + 
                [
                    render_publication_as_table_row(publication) 
                    for publication in publications
                ]
            ),
        )
    ]