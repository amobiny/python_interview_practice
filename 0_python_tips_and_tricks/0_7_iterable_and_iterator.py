
# iterable: anything thet can be looped over
#           anything that can appear on the right side of the loop; e.g.: for i in iterable:
#           calling iter on it, returns and iterator:  ****   iterator = iter(iterable)  ****
s = 'abc'
l = [1, 2, 3, 4]
s_iter = iter(s)
print(s_iter)                   # <str_iterator object at 0x7f3e7c68ab70>
l_iter = iter(l)
print(l_iter)                   # <list_iterator object at 0x7fa7ed4dcd68>

print(next(s_iter))             # a
print(next(s_iter))             # b
print(next(s_iter))             # c
# print(next(s_iter))             # Error; StopIteration

# this is similar to:
for i in s:
    print(i)

# How to add iterator behavior to a class?
#   1. add __iter__ method
#   2. add __next__ method
#   3. take care of the indexing

# write an iterable class which can return a reverse of a string


class Reverse:
    def __init__(self, in_str):
        self.in_str = in_str
        self.index = len(in_str)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.in_str[self.index]


rev = Reverse('spam')
print(rev)                      # <__main__.Reverse object at 0x7f1957047240>
# now rev is an iterable object which we can loop over

for c in rev:
    print(c)
# m
# a
# p
# s

# similarly we could do:
rev_iter = iter(rev)
print(next(rev_iter))       # m
print(next(rev_iter))       # a
print(next(rev_iter))       # p
print(next(rev_iter))       # s
print(next(rev_iter))       # StopIteration
