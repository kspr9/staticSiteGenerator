from enum import Enum

from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    '''
    It takes a list of "old nodes", a delimiter, and a text type. 
    It should return a new list of nodes, where any "text" type nodes in the input list are 
    (potentially) split into multiple nodes based on the syntax. 
    e.g.
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    new_nodes becomes -->
    [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.TEXT),
    ]   
    '''
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        # Find all delimiter pairs
        parts = []
        current_text = node.text
        
        while delimiter in current_text:
            first_index = current_text.find(delimiter)
            second_index = current_text.find(delimiter, first_index + 1)
            
            # If no closing delimiter found, treat the rest as text
            if second_index == -1:
                parts.append(TextNode(current_text, TextType.TEXT))
                break
                
            # Add text before the first delimiter
            if first_index > 0:
                parts.append(TextNode(current_text[:first_index], TextType.TEXT))
                
            # Add text between delimiters with the specified text type
            parts.append(TextNode(current_text[first_index+1:second_index], text_type))
            
            # Continue with the rest of the text
            current_text = current_text[second_index+1:]
            
        # Add any remaining text
        if current_text:
            parts.append(TextNode(current_text, TextType.TEXT))
            
        # If no delimiters were found, add the original node
        if not parts:
            new_nodes.append(node)
        else:
            new_nodes.extend(parts)
            
    return new_nodes
    