from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    '''
    constructor should differ from HTMLNode in that:
    The tag and children arguments are not optional
    It doesn't take a value argument
    props is optional   
    '''
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] = None):
        if tag is None:
            raise ValueError("ParentNode must have a tag")
        if children is None:
            raise ValueError("ParentNode must have children")
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        '''
        If the object doesn't have a tag, raise a ValueError.
        If children is a missing value, raise a ValueError with a different message.
        Otherwise, return a string representing the HTML tag of the node and its children. This should be a recursive method (each recursion being called on a nested child node). I iterated over all the children and called to_html on each, concatenating the results and injecting them between the opening and closing tags of the parent.
        '''
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")  
        if self.children is None:
            raise ValueError("ParentNode must have children")
        return f"<{self.tag}{self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"
        
        