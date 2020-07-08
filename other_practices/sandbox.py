
class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def is_superbalanced(self):
        pass


root = BinaryTreeNode(5)
node1 = root.insert_left(3)
node2 = root.insert_right(8)
print(root.is_superbalanced())
