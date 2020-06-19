# A Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties
# - The left sub-tree of a node has a key less than or equal to its parent node's key.
# - The right sub-tree of a node has a key greater than to its parent node's key.

# Inserting into a Tree
# To insert into a tree we use the same node class created above and add a insert class to it.
# The insert class compares the value of the node to the parent node and decides to add it as
# a left node or a right node. Finally the PrintTree class is used to print the tree.


class Node:
    def __init__(self, data):
        self.left = None        # node
        self.right = None       # node
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def findval(self, val):
        if val < self.data:
            if self.left:
                return self.left.findval(val)
            else:
                print('value not found!')
        elif val > self.data:
            if self.right:
                return self.right.findval(val)
            else:
                print('value not found!')
        else:
            print('{} is found!'.format(val))

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.print_tree()
root.findval(7)
root.findval(14)

