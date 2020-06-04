"""
In the english dictionary the word stack means arranging objects on over another.
It is the same way memory is allocated in this data structure. It stores the data
elements in a similar fashion as a bunch of plates are stored one above another
in the kitchen. So stack data strcuture allows operations at one end which can
be called top of the stack. We can add elements or remove elements only form this
end of the stack.

In a stack the element inserted last in sequence will come out first as we can remove
only from the top of the stack. Such feature is known as Last in First Out(LIFO) feature.
The operations of adding and removing the elements is known as PUSH and POP.
"""


class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        """To push into stack"""
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    def peek(self):
        """To look at the top of the stack"""
        return self.stack[-1]

    def remove(self):
        """To pop from stack"""
        if len(self.stack) <= 0:
            print("No element in the Stack")
        else:
            return self.stack.pop()


AStack = Stack()
AStack.add("Mon")
print(AStack.peek())
AStack.add("Tue")
print(AStack.peek())
AStack.add("Wed")
print(AStack.peek())
AStack.add("Thu")
print(AStack.peek())
AStack.remove()
print(AStack.peek())
AStack.remove()
print(AStack.peek())

