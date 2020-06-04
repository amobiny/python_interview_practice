# linked list is a sequence of data elements, which are connected together via links.
# Each data element contains a connection to another data element in form of a pointer.
# Python does not have linked lists in its standard library. We implement the concept
# of linked lists using the concept of nodes.

# we are going to study the types of linked lists known as "singly linked lists".
# In this type of data structure there is only one link between any two data elements.

# We create a Node object and create another class to use this node object.
# We pass the appropriate values through the node object to point the to the next data elements.
# The below program creates the linked list with three data elements.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None         # node


class SLinkedList:
    def __init__(self):
        self.head = None         # node

    def listprint(self):
        """
        To show how to traverse a linked list
        """
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def insert_at_beginning(self, newdata):
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, newdata):
        new_node = Node(newdata)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def insert_in_between(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        new_node = Node(newdata)
        new_node.next = middle_node.next
        middle_node.next = new_node

    def removenode(self, remove_key):
        pass


list1 = SLinkedList
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thu")

# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list1.listprint()
list1.insert_at_beginning("Sun")
list1.insert_at_end("Fri")
list1.insert_in_between(list1.headval.nextval, "Wed")

list.listprint()

