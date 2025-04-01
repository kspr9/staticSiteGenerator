import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_node_basic(self):
        node = ParentNode(
            "div",
            [
                LeafNode("First paragraph", "p"),
                LeafNode("Second paragraph", "p")
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<div><p>First paragraph</p><p>Second paragraph</p></div>"
        )

    def test_parent_node_with_props(self):
        node = ParentNode(
            "div",
            [
                LeafNode("First paragraph", "p"),
                LeafNode("Second paragraph", "p")
            ],
            {"class": "container"}
        )
        self.assertEqual(
            node.to_html(),
            '<div class="container"><p>First paragraph</p><p>Second paragraph</p></div>'
        )

    def test_parent_node_no_children(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_parent_node_nested(self):
        node = ParentNode(
            "article",
            [
                LeafNode("Title", "h1"),
                ParentNode(
                    "div",
                    [
                        LeafNode("Inner paragraph", "p"),
                        LeafNode("Inner span", "span")
                    ]
                ),
                LeafNode("Outer paragraph", "p")
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<article><h1>Title</h1><div><p>Inner paragraph</p><span>Inner span</span></div><p>Outer paragraph</p></article>"
        )

    def test_parent_node_deeply_nested(self):
        inner_inner = ParentNode(
            "span",
            [LeafNode("Deep content", "p")]
        )
        inner = ParentNode(
            "div",
            [inner_inner]
        )
        outer = ParentNode(
            "section",
            [inner]
        )
        self.assertEqual(
            outer.to_html(),
            "<section><div><span><p>Deep content</p></span></div></section>"
        )

    def test_parent_node_mixed_content(self):
        node = ParentNode(
            "div",
            [
                LeafNode("Raw text"),  # Raw text as LeafNode with no tag
                LeafNode("Paragraph", "p"),
                ParentNode(
                    "span",
                    [LeafNode("Nested content", "p")]
                )
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<div>Raw text<p>Paragraph</p><span><p>Nested content</p></span></div>"
        )

    def test_parent_node_with_props_nested(self):
        node = ParentNode(
            "section",
            [
                ParentNode(
                    "div",
                    [LeafNode("Inner content", "p")],
                    {"class": "inner"}
                )
            ],
            {"class": "outer"}
        )
        self.assertEqual(
            node.to_html(),
            '<section class="outer"><div class="inner"><p>Inner content</p></div></section>'
        )

    def test_parent_node_empty_children(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_parent_node_single_child(self):
        node = ParentNode(
            "div",
            [LeafNode("Single child", "p")]
        )
        self.assertEqual(node.to_html(), "<div><p>Single child</p></div>")

    def test_parent_node_all_raw_text(self):
        node = ParentNode(
            "div",
            [
                LeafNode("First text"),
                LeafNode("Second text"),
                LeafNode("Third text")
            ]
        )
        self.assertEqual(node.to_html(), "<div>First textSecond textThird text</div>")

    def test_parent_node_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("Content", "p")])

    def test_parent_node_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

if __name__ == "__main__":
    unittest.main()