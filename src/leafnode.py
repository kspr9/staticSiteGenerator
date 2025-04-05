from .htmlnode import HTMLNode


class LeafNode(HTMLNode):
    '''
    It should not allow for any children
    The value data member should be required (and tag even though the tag's value may be None)
    '''
    def __init__(self, value: str, tag: str = None, props: dict[str, str] = None):
        super().__init__(tag, value, None, props)
        if self.children is not None:
            raise ValueError("LeafNode cannot have children")
            
    def to_html(self):
        '''
        If the leaf node has no value, it should raise a ValueError. All leaf nodes must have a value.
        If there is no tag (e.g. it's None), the value should be returned as raw text.
        Otherwise, it should render an HTML tag. 
        '''
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value})"
        
