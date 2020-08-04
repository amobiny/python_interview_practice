# We can do k=2 for the earlier code; but is there a way to do O(1) space complexity for this case?


# Solution:

# We start with a function for getting the largest value. The largest value is simply the "rightmost" one,
# so we can get it in one walk down the tree by traversing rightward until we don't have a right child anymore

# With this in mind, we can also find the second largest in one walk down the tree. At each step, we have a few cases:
#
# 1. If we have a left subtree but not a right subtree, then the current node is the largest overall (the "rightmost")
# node. The second largest element must be the largest element in the left subtree. We use our find_largest() function
# above to find the largest in that left subtree!

# 2. If we have a right child, but that right child node doesn't have any children, then the right child must be the
# largest element and our current node must be the second largest element!

# 3. Else, we have a right subtree with more than one element, so the largest and second largest are somewhere
# in that subtree. So we step right.


def find_largest(root_node):
    current = root_node
    while current:
        if not current.right:
            return current.value
        current = current.right


def find_second_largest(root_node):
    if (root_node is None or
            (root_node.left is None and root_node.right is None)):
        raise ValueError('Tree must have at least 2 nodes')

    current = root_node
    while current:
        # Case: current is largest and has a left subtree
        # 2nd largest is the largest in that subtree
        if current.left and not current.right:
            return find_largest(current.left)

        # Case: current is parent of largest, and largest has no children,
        # so current is 2nd largest
        if (current.right and
                not current.right.left and
                not current.right.right):
            return current.value

        current = current.right

