# Write a function to find the kth largest element in a binary search tree


# Solution:

# Our first thought might be to do an in-order traversal of the BST and return the second-to-last item.
#  This means looking at every node in the BST. That would take O(n) time and O(h) space, where h is
#  the max height of the tree (which is lg(n) if the tree is balanced, but could be as much as n if not).

# The second largest element is kth last element in inorder traversal and kth element
# in reverse inorder traversal. We traverse given Binary Search Tree in reverse inorder and
# keep track of counts of nodes visited. Once the count becomes k, we print the node.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_left(self, data):
        self.left = Node(data)

    def insert_right(self, data):
        self.right = Node(data)


def kth_largest_number(root, k, c):

    # Base cases, the second condition
    # is important to avoid unnecessary
    # recursive calls
    if root is None or c[0] >= k:
        return

    # Follow reverse inorder traversal
    # so that the largest element is
    # visited first
    if root.right:
        kth_largest_number(root.right, k, c)

    # Increment count of visited nodes
    c[0] += 1

    # If c becomes k now, then this is
    # the k'th largest
    if c[0] == k:
        print('The {}th largest number is: {}'.format(k, root.data))

    # Recur for left subtree
    if root.left:
        kth_largest_number(root.left, k, c)


# code to generate a binary BST with a particular root node value
def insert(node, data):
    if node is None:
        return Node(data)

    if data < node.data:
        node.left = insert(node.left, data)

    if data > node.data:
        node.right = insert(node.right, data)

    return node



root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

for k in range(1, 5):
    count_of_visited_nodes = [0]
    kth_largest_number(root, k, count_of_visited_nodes)


# The code first traverses down to the rightmost node which takes O(h) time,
# then traverses k elements in O(k) time. Therefore overall time complexity is O(h + k).

# space complexity: O(h) (read the Google Doc about stack calls and frames)
