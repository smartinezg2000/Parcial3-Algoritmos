class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, letter, code):
        if self.root is None:
            self.root = Node(letter)
        else:
            current_node = self.root
            for symbol in code:
                if symbol == ".":
                    if current_node.left is None:
                        current_node.left = Node(letter)
                    current_node = current_node.left
                elif symbol == "-":
                    if current_node.right is None:
                        current_node.right = Node(letter)
                    current_node = current_node.right

    def translate(self,code):

        current = self.root
        for character in code:
            if character == '.':
                current = current.left
            else:
                current = current.right
        return current.value





tree = BinarySearchTree()
tree.insert('e','.')
tree.insert('i ','.')
tree.insert('a ','-')
tree.insert('s','..')
tree.insert('v','..-')
# tree.insert('','')
# tree.insert('','')
# tree.insert('','')
# tree.insert('','')
# tree.insert('','')
# tree.insert('','')
# tree.insert('','')
# tree.insert('r ','-.')

print(tree.translate('..-'))
print(tree.root.left.left.value)