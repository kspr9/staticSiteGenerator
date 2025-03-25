from textnode import TextNode, TextType

def main():
    #The function should create a new TextNode object with some dummy values
    text_node = TextNode("Hello, world!", TextType.NORMAL)
    print(text_node)

if __name__ == "__main__":
    main()