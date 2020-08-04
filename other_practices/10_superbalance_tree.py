# Write a function to see if a binary tree ↴ is "superbalanced" (a new tree property we just made up).
# A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_superbalance(root):
    depths = []
    nodes_stack = []
    nodes_stack.append((root, 1))


    while len(nodes_stack):
        # Pop a node and its depth from the top of our stack
        node, depth = nodes_stack.pop()

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
                nodes_stack.append((node.left, depth + 1))
            if node.right:
                nodes_stack.append((node.right, depth + 1))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

is_superbalance(root)

# time complexity: O(n)
# space complexity: O(n)

