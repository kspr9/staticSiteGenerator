import unittest
from ..markup_methods import split_nodes_delimiter
from ..textnode import TextNode, TextType

class TestMarkupMethods(unittest.TestCase):
    def test_split_nodes_delimiter_simple(self):
        """Test basic splitting with a single delimiter pair"""
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is text with a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("code block", TextType.CODE))
        self.assertEqual(new_nodes[2], TextNode(" word", TextType.TEXT))
    
    def test_split_nodes_delimiter_no_delimiters(self):
        """Test when there are no delimiters in the text"""
        node = TextNode("This is plain text without any delimiters", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0], TextNode("This is plain text without any delimiters", TextType.TEXT))
    
    def test_split_nodes_delimiter_multiple_pairs(self):
        """Test splitting with multiple delimiter pairs"""
        node = TextNode("This is `code1` and this is `code2`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0], TextNode("This is ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("code1", TextType.CODE))
        self.assertEqual(new_nodes[2], TextNode(" and this is ", TextType.TEXT))
        self.assertEqual(new_nodes[3], TextNode("code2", TextType.CODE))
        self.assertEqual(new_nodes[4], TextNode("", TextType.TEXT))
    
    def test_split_nodes_delimiter_non_text_node(self):
        """Test when the node is not of type TEXT"""
        node = TextNode("This is already a code node", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.BOLD)
        
        # The method should return the original node unchanged
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0], TextNode("This is already a code node", TextType.CODE))
    
    def test_split_nodes_delimiter_multiple_nodes(self):
        """Test splitting multiple nodes in the input list"""
        node1 = TextNode("This is `code`", TextType.TEXT)
        node2 = TextNode("This is not code", TextType.TEXT)
        node3 = TextNode("This is also `code`", TextType.TEXT)
        
        new_nodes = split_nodes_delimiter([node1, node2, node3], "`", TextType.CODE)
        
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0], TextNode("This is ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("code", TextType.CODE))
        self.assertEqual(new_nodes[2], TextNode("This is not code", TextType.TEXT))
        self.assertEqual(new_nodes[3], TextNode("This is also ", TextType.TEXT))
        self.assertEqual(new_nodes[4], TextNode("code", TextType.CODE))
    
    def test_split_nodes_delimiter_empty_text(self):
        """Test with empty text"""
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0], TextNode("", TextType.TEXT))
    
    def test_split_nodes_delimiter_different_delimiters(self):
        """Test with different delimiter types"""
        node = TextNode("This is **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("bold", TextType.BOLD))
        self.assertEqual(new_nodes[2], TextNode(" text", TextType.TEXT))
    
    def test_split_nodes_delimiter_unmatched_delimiters(self):
        """Test with unmatched delimiters (should not split)"""
        node = TextNode("This is `code without closing delimiter", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        # Should not split if delimiters are unmatched
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0], TextNode("This is `code without closing delimiter", TextType.TEXT))
    
    def test_split_nodes_delimiter_empty_list(self):
        """Test with an empty list of nodes"""
        new_nodes = split_nodes_delimiter([], "`", TextType.CODE)
        
        self.assertEqual(len(new_nodes), 0)

if __name__ == "__main__":
    unittest.main()
