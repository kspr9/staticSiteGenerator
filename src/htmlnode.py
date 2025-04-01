class HTMLNode:
    '''
    have 4 data members set in the constructor:

    tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    children - A list of HTMLNode objects representing the children of this node
    props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    
    every data member should be optional and default to None
    An HTMLNode without a value will be assumed to have children
    An HTMLNode without children will be assumed to have a value
    '''
    def __init__(self, tag: str = None, value: str = None, children: list["HTMLNode"] = None, props: dict[str, str] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __str__(self):
        return f"{self.tag}: {self.value}"
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    def to_html(self):
        # should just raise a NotImplementedError. Child classes will override this method to render themselves as HTML.
        raise NotImplementedError("Subclasses must implement this method")
    
    def props_to_html(self):
        # should return a string that represents the HTML attributes of the node
        if self.props is None:
            return ""
        return "".join([f' {k}="{v}"' for k, v in self.props.items()])
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    