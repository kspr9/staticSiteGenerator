node = "This is text with a `code block` word"
delimiter = "`"
delimiter2 = "**"


print(len(delimiter2))
first_index = node.find(delimiter)
second_index = node.find(delimiter, first_index + 1)

print(f'first_index: {first_index}')
print(f'second_index: {second_index}')

print(f'node[first_index:second_index+1]: {node[first_index+1:second_index]}')

print(node[:first_index])
print(node[second_index+1:])

split_node = node.split(delimiter)
print(f'split_node: {split_node}')

print(f'split_node[0]: {split_node[0]}')
print(f'split_node[1]: {split_node[1]}')
print(f'split_node[2]: {split_node[2]}')
