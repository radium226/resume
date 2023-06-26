from lxml.etree import fromstring, tostring, Element

from radium226.resume_generator.append_child_nodes_to_parent_element import append_child_nodes_to_parent_element


def test_append_child_nodes_to_parent_element():
    p = Element("p")
    b = Element("b")
    b.text = "FooBar"
    append_child_nodes_to_parent_element(p, ["Foo", b, "Bar"])
    assert tostring(p, encoding=str) == "<p>Foo<b>FooBar</b>Bar</p>"