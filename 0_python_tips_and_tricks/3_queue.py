
# We are familiar with queue in our day to day life as we wait for a service.
# The queue data structure aslo means the same where the data elements are arranged in a queue.
# The uniqueness of queue lies in the way items are added and removed.
# The items are allowed at on end but removed form the other end. So it is a First-in-First out method.
# An queue can be implemented using python list where we can use the insert() and pop() methods
# to add and remove elements.

# [add to this side, ..........., remove from this side]


class Queue:
    def __init__(self):
        self.queue = []

    def add(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)

    def remove(self):
        if len(self.queue) > 0:
            self.queue.pop()
        else:
            print('No item in the queue!')

    def print_queue(self):
        if len(self.queue) > 0:
            print(*self.queue)
        else:
            print('No item in queue!')


my_queue = Queue()
my_queue.add('Mon')
my_queue.add('Tue')
my_queue.add('We')
my_queue.remove()
my_queue.print_queue()




