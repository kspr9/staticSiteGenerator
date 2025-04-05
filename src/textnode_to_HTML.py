from .textnode import TextNode, TextType
from .leafnode import LeafNode

def text_node_to_html_node(text_node: TextNode) -> LeafNode | ValueError:
    """Convert a TextNode to an HTMLNode based on its text type."""
    if text_node.text_type == TextType.NORMAL or text_node.text_type == TextType.TEXT:
        return LeafNode(text_node.text, None)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(text_node.text, "b")
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(text_node.text, "i")
    elif text_node.text_type == TextType.CODE:
        return LeafNode(text_node.text, "code")
    elif text_node.text_type == TextType.LINK:
        if text_node.url is None:
            raise ValueError("Link text node must have a URL")
        return LeafNode(text_node.text, "a", {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        if text_node.url is None:
            raise ValueError("Image text node must have a URL")
        return LeafNode("", "img", {"src": text_node.url, "alt": "Google"})
    else:
        raise ValueError(f"Invalid text type: {text_node.text_type}") 