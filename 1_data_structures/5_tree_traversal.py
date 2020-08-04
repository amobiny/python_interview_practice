# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/?ref=lbp


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def print_preorder(self):
        print(self.data)
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()

    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print(self.data)
        if self.right:
            self.right.print_inorder()

    def print_postorder(self):
        if self.left:
            self.left.print_postorder()
        if self.right:
            self.right.print_postorder()
        print(self.data)


def recursive_inorder_traversal(root):

    if root is None:
        return

    if root.left:
        recursive_inorder_traversal(root.left)

    print(root.data)

    if root.right:
        recursive_inorder_traversal(root.right)


def iterative_inorder_traversal(root):
    # https: // www.geeksforgeeks.org / inorder - tree - traversal - without - recursion /
    # Set current to root of binary tree
    current = root
    stack = []  # initialize stack

    while True:

        # Reach the left most Node of the current Node
        if current is not None:

            # Place pointer to a tree node on the stack
            # before traversing the node's left subtree
            stack.append(current)

            current = current.left


        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is
        # empty you are done
        elif (stack):
            current = stack.pop()
            print(current.data, end=" ")  # Python 3 printing

            # We have visited the node and its left
            # subtree. Now, it's right subtree's turn
            current = current.right

        else:
            break
    print()



root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

root.print_preorder()
print('-'*20)
root.print_inorder()
print('-'*20)
root.print_postorder()
print('-'*20)
recursive_inorder_traversal(root)
print('-'*20)
iterative_inorder_traversal(root)
