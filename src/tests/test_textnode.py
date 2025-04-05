import unittest

from ..textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_normal(self):
        node1 = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertEqual(node1, node2)

    def test_eq_bold(self):
        node1 = TextNode("This is bold text", TextType.BOLD)
        node2 = TextNode("This is bold text", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq_italic(self):
        node1 = TextNode("This is italic text", TextType.ITALIC)
        node2 = TextNode("This is italic text", TextType.ITALIC)
        self.assertEqual(node1, node2)

    def test_eq_code(self):
        node1 = TextNode("This is code text", TextType.CODE)
        node2 = TextNode("This is code text", TextType.CODE)
        self.assertEqual(node1, node2)

    def test_eq_link(self):
        node1 = TextNode("This is a link", TextType.LINK, "https://example.com")
        node2 = TextNode("This is a link", TextType.LINK, "https://example.com")
        self.assertEqual(node1, node2)

    def test_eq_image(self):
        node1 = TextNode("This is an image", TextType.IMAGE, "https://example.com/image.jpg")
        node2 = TextNode("This is an image", TextType.IMAGE, "https://example.com/image.jpg")
        self.assertEqual(node1, node2)

    def test_not_eq_different_text(self):
        node1 = TextNode("First text", TextType.NORMAL)
        node2 = TextNode("Second text", TextType.NORMAL)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_type(self):
        node1 = TextNode("Same text", TextType.NORMAL)
        node2 = TextNode("Same text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_url(self):
        node1 = TextNode("Same text", TextType.LINK, "https://example1.com")
        node2 = TextNode("Same text", TextType.LINK, "https://example2.com")
        self.assertNotEqual(node1, node2)

    def test_not_eq_without_url(self):
        node1 = TextNode("Same text", TextType.LINK, "https://example.com")
        node2 = TextNode("Same text", TextType.LINK)
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = TextNode("Test text", TextType.NORMAL)
        self.assertEqual(repr(node), "TextNode(Test text, normal, None)")

    def test_repr_with_url(self):
        node = TextNode("Test text", TextType.LINK, "https://example.com")
        self.assertEqual(repr(node), "TextNode(Test text, link, https://example.com)")

    

if __name__ == "__main__":
    unittest.main()
