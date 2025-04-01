import unittest

from textnode import TextNode, TextType
from textnode_to_HTML import text_node_to_html_node

class TestTextNodeToHTML(unittest.TestCase):
    def test_normal_text_node(self):
        text_node = TextNode("Hello, world!", TextType.NORMAL)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node.tag, None)
        self.assertEqual(leaf_node.value, "Hello, world!")
    
    def test_text(self):
        text_node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_text_node(self):
        text_node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic_text_node(self):
        text_node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")

    def test_code_text_node(self):
        text_node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")

    def test_link_text_node(self):
        text_node = TextNode("This is a link text node", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_image_text_node(self):
        text_node = TextNode("", TextType.IMAGE, "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png", "alt": "Google"})

    def test_invalid_text_node(self):
        node = TextNode("This is an invalid text node", "invalid")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()