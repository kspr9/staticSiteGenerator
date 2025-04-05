import unittest
from ..leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("Hello, world!", "p")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
# Add more tests for different tag types.
    def test_leaf_to_html_a(self):
        node = LeafNode("Hello, world!", "a", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, world!</a>')
        
    def test_leaf_to_html_img(self):
        node = LeafNode("", "img", props={"src": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png", "alt": "Google"})
        self.assertEqual(node.to_html(), '<img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" alt="Google"></img>')
        
    def test_leaf_to_html_input(self):
        node = LeafNode("", "input", props={"type": "text", "name": "username"})
        self.assertEqual(node.to_html(), '<input type="text" name="username"></input>')
        
    def test_leaf_to_html_none(self):
        node = LeafNode("Some value")
        self.assertEqual(node.to_html(), "Some value")
        
        
        
