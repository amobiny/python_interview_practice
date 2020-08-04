# https://www.geeksforgeeks.org/print-level-order-traversal-line-line/?ref=lbp


# https://www.geeksforgeeks.org/level-order-tree-traversal/?ref=lbp
# https://www.youtube.com/watch?v=86g8jAQug04

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


# Iterative method to do level order traversal
# line by line
def printLevelOrder(root):
    # Base case
    if root is None:
        return
    # Create an empty queue for level order traversal
    q = []

    # Enqueue root and initialize height
    q.append(root)

    while q:

        # nodeCount (queue size) indicates number
        # of nodes at current lelvel.
        count = len(q)

        # Dequeue all nodes of current level and
        # Enqueue all nodes of next level
        while count > 0:
            temp = q.pop(0)
            print(temp.val, end=' ')
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

            count -= 1
        print(' ')

        # Driver Code


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

printLevelOrder(root)
