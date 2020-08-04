
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
        if self.value is None:
            return True

        # We short-circuit as soon as we find more than 2
        depths = []

        # We'll treat this list as a stack that will store tuples of (node, depth)
        nodes = []
        nodes.append((self, 0))

        while len(nodes):
            # Pop a node and its depth from the top of our stack
            node, depth = nodes.pop()

            # Case: we found a leaf
            if (not node.left) and (not node.right):
                # We only care if it's a new depth
                if depth not in depths:
                    depths.append(depth)

                    # Two ways we might now have an unbalanced tree:
                    #   1) more than 2 different leaf depths
                    #   2) 2 leaf depths that are more than 1 apart
                    if ((len(depths) > 2) or
                            (len(depths) == 2 and abs(depths[0] - depths[1]) > 1)):
                        return False
            else:
                # Case: this isn't a leaf - keep stepping down
                if node.left:
                    nodes.append((node.left, depth + 1))
                if node.right:
                    nodes.append((node.right, depth + 1))

        return True



root = BinaryTreeNode(5)
node1 = root.insert_left(3)
node2 = root.insert_right(8)
print(root.is_superbalanced())
