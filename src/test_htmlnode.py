'''
Create some tests for the HTMLNode class (at least 3).
Create a few nodes and make sure the props_to_html method works as expected.
'''

import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_str_method(self):
        # Test __str__ method
        node = HTMLNode(tag="p", value="Hello, world!")
        self.assertEqual(str(node), "p: Hello, world!")
        
        # Test with None values
        node_no_tag = HTMLNode(value="Just text")
        self.assertEqual(str(node_no_tag), "None: Just text")
        
        node_no_value = HTMLNode(tag="div")
        self.assertEqual(str(node_no_value), "div: None")

    def test_repr_method(self):
        # Test __repr__ method
        node = HTMLNode(tag="p", value="Hello", children=[], props={"class": "greeting"})
        expected = "HTMLNode(tag=p, value=Hello, children=[], props={'class': 'greeting'})"
        self.assertEqual(repr(node), expected)
        
        # Test with None values
        node_none = HTMLNode()
        expected_none = "HTMLNode(tag=None, value=None, children=None, props=None)"
        self.assertEqual(repr(node_none), expected_none)

    def test_to_html_not_implemented(self):
        # Test that to_html raises NotImplementedError
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html_edge_cases(self):
        # Test with empty props dictionary
        node_empty = HTMLNode(props={})
        self.assertEqual(node_empty.props_to_html(), "")
        
        # Test with props containing special characters
        node_special = HTMLNode(props={"class": "my-class", "data-test": "test&value"})
        self.assertEqual(node_special.props_to_html(), ' class="my-class" data-test="test&value"')
        
        # Test with props containing spaces
        node_spaces = HTMLNode(props={"class": "my class", "title": "My Title"})
        self.assertEqual(node_spaces.props_to_html(), ' class="my class" title="My Title"')

    def test_simple_paragraph(self):
        # Test node1: Simple paragraph with text
        self.assertEqual(node1.tag, "p")
        self.assertEqual(node1.value, "Hello, world!")
        self.assertEqual(node1.children, None)
        self.assertEqual(node1.props, None)

    def test_div_with_children(self):
        # Test node2: Div with multiple children
        self.assertEqual(node2.tag, "div")
        self.assertEqual(node2.value, None)
        self.assertEqual(len(node2.children), 2)
        self.assertEqual(node2.children[0].tag, "p")
        self.assertEqual(node2.children[0].value, "First paragraph")
        self.assertEqual(node2.children[1].value, "Second paragraph")

    def test_link_with_props(self):
        # Test node3: Link with props
        self.assertEqual(node3.tag, "a")
        self.assertEqual(node3.value, "Click me")
        self.assertEqual(node3.children, None)
        self.assertEqual(node3.props, {
            "href": "https://example.com",
            "target": "_blank"
        })
        self.assertEqual(node3.props_to_html(), ' href="https://example.com" target="_blank"')

    def test_raw_text(self):
        # Test node4: Raw text without tag
        self.assertEqual(node4.tag, None)
        self.assertEqual(node4.value, "This is just raw text")
        self.assertEqual(node4.children, None)
        self.assertEqual(node4.props, None)

    def test_nested_structure(self):
        # Test node5: Complex nested structure
        self.assertEqual(node5.tag, "article")
        self.assertEqual(node5.value, None)
        self.assertEqual(len(node5.children), 2)
        self.assertEqual(node5.children[0].tag, "h1")
        self.assertEqual(node5.children[0].value, "Main Title")
        self.assertEqual(node5.children[1].tag, "div")
        self.assertEqual(len(node5.children[1].children), 2)

    def test_image_with_props(self):
        # Test node6: Image with props
        self.assertEqual(node6.tag, "img")
        self.assertEqual(node6.value, None)
        self.assertEqual(node6.children, None)
        self.assertEqual(node6.props, {
            "src": "https://example.com/image.jpg",
            "alt": "Example image",
            "width": "300",
            "height": "200"
        })
        expected_props = ' src="https://example.com/image.jpg" alt="Example image" width="300" height="200"'
        self.assertEqual(node6.props_to_html(), expected_props)

    def test_form_with_children(self):
        # Test node7: Form with multiple children and props
        self.assertEqual(node7.tag, "form")
        self.assertEqual(node7.value, None)
        self.assertEqual(len(node7.children), 2)
        self.assertEqual(node7.props, {
            "method": "POST",
            "action": "/submit"
        })
        self.assertEqual(node7.children[0].tag, "input")
        self.assertEqual(node7.children[1].tag, "button")
        self.assertEqual(node7.children[1].value, "Submit")

    def test_list_structure(self):
        # Test node8: List with multiple items
        self.assertEqual(node8.tag, "ul")
        self.assertEqual(node8.value, None)
        self.assertEqual(len(node8.children), 3)
        self.assertEqual(node8.children[0].tag, "li")
        self.assertEqual(node8.children[0].value, "First item")
        self.assertEqual(node8.children[1].value, "Second item")
        self.assertEqual(node8.children[2].value, "Third item")

    def test_table_structure(self):
        # Test node9: Table with nested structure
        self.assertEqual(node9.tag, "table")
        self.assertEqual(node9.value, None)
        self.assertEqual(len(node9.children), 2)
        self.assertEqual(node9.children[0].tag, "tr")
        self.assertEqual(len(node9.children[0].children), 2)
        self.assertEqual(node9.children[0].children[0].tag, "th")
        self.assertEqual(node9.children[0].children[0].value, "Header 1")

    def test_mixed_content(self):
        # Test node10: Section with mixed content
        self.assertEqual(node10.tag, "section")
        self.assertEqual(node10.value, None)
        self.assertEqual(len(node10.children), 3)
        self.assertEqual(node10.props, {"class": "content-section"})
        self.assertEqual(node10.children[0].tag, "h2")
        self.assertEqual(node10.children[1].tag, None)  # Raw text
        self.assertEqual(node10.children[2].tag, "div")
        self.assertEqual(node10.children[2].props, {"class": "highlight"})
        self.assertEqual(len(node10.children[2].children), 2)

if __name__ == "__main__":
    unittest.main()

# Generate a variety of HTMLnodes that cover the different ways the HTMLNode class can be used. 
# No tests, just nodes as dummy data
# An HTMLNode without a tag will just render as raw text
# An HTMLNode without a value will be assumed to have children
# An HTMLNode without children will be assumed to have a value
# An HTMLNode without props simply won't have any attributes

# 1. A simple paragraph with text
node1 = HTMLNode(tag="p", value="Hello, world!")

# 2. A div with multiple children
node2 = HTMLNode(
    tag="div",
    children=[
        HTMLNode(tag="p", value="First paragraph"),
        HTMLNode(tag="p", value="Second paragraph")
    ]
)

# 3. A link with props (attributes)
node3 = HTMLNode(
    tag="a",
    value="Click me",
    props={"href": "https://example.com", "target": "_blank"}
)

# 4. Raw text without a tag
node4 = HTMLNode(value="This is just raw text")

# 5. A complex nested structure
node5 = HTMLNode(
    tag="article",
    children=[
        HTMLNode(tag="h1", value="Main Title"),
        HTMLNode(
            tag="div",
            children=[
                HTMLNode(tag="p", value="First section"),
                HTMLNode(tag="p", value="Second section")
            ]
        )
    ]
)

# 6. An image with props
node6 = HTMLNode(
    tag="img",
    props={
        "src": "https://example.com/image.jpg",
        "alt": "Example image",
        "width": "300",
        "height": "200"
    }
)

# 7. A form with multiple children and props
node7 = HTMLNode(
    tag="form",
    props={"method": "POST", "action": "/submit"},
    children=[
        HTMLNode(tag="input", props={"type": "text", "name": "username"}),
        HTMLNode(tag="button", value="Submit")
    ]
)

# 8. A list with multiple items
node8 = HTMLNode(
    tag="ul",
    children=[
        HTMLNode(tag="li", value="First item"),
        HTMLNode(tag="li", value="Second item"),
        HTMLNode(tag="li", value="Third item")
    ]
)

# 9. A table with nested structure
node9 = HTMLNode(
    tag="table",
    children=[
        HTMLNode(
            tag="tr",
            children=[
                HTMLNode(tag="th", value="Header 1"),
                HTMLNode(tag="th", value="Header 2")
            ]
        ),
        HTMLNode(
            tag="tr",
            children=[
                HTMLNode(tag="td", value="Cell 1"),
                HTMLNode(tag="td", value="Cell 2")
            ]
        )
    ]
)

# 10. A section with mixed content
node10 = HTMLNode(
    tag="section",
    props={"class": "content-section"},
    children=[
        HTMLNode(tag="h2", value="Section Title"),
        HTMLNode(value="Some raw text in the middle"),
        HTMLNode(
            tag="div",
            props={"class": "highlight"},
            children=[
                HTMLNode(tag="p", value="Highlighted content"),
                HTMLNode(tag="p", value="More highlighted content")
            ]
        )
    ]
)

