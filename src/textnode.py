from enum import Enum
from leafnode import LeafNode


class TextType(Enum):
    # 
    '''should cover all the text types that can be used in a text node
        Normal text
        **Bold text**
        _Italic text_
        `Code text`
        Links, in this format: [anchor text](url)
        Images, in this format: ![alt text](url)
    '''
    TEXT = "text"
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    '''
    A text node is a node that contains text.
    It can be a normal text, a bold text, an italic text, a code text, a link, or an image.
    '''
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    # def __str__(self):
    #     return self.text
    
    def __eq__(self, value: object) -> bool:
        #returns True if all of the properties of two TextNode objects are equal
        if not isinstance(value, TextNode):
            return False
        return self.text == value.text and self.text_type == value.text_type and self.url == value.url
    
    def __repr__(self):
        # returns a string representation of the TextNode object
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
