###########################################################################
# Mutable vs. Immutable Python objects
###########################################################################

# mutable objects: list, dictionary, set

mutable_list = [1, 2, 3]
mutable_list[-1] = 4

# immutable objects: tuple, string, frozenset
frozen_set = frozenset([1, 2, 3])

# mutable object within an immutable object
t = (1, [1, 2, 3], 'word')
t[1][2] = 4

# this shows that if the tuple is immutable, that does not
# guarantee that the object referenced by the tuple is immutable too.

###########################################################################
# Lists
###########################################################################

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3]

del list1[2]                        # delete list elements
list1 = list1 + list2               # concatenation
list3 = ['Hi!'] * 4                 # repetition
TorF = 3 in [1, 2, 3]	            # membership

###########################################################################
# Tuples
###########################################################################
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

tup_singular = (50,)                # that comma is important
tup3 = tup1 + tup2                  # concatenation
del tup3                            # delete a whole tuple
tup4 = ('Hi!',) * 4                 # repetition
TrueOrFalse = 3 in (1, 2, 3)	    # membership


###########################################################################
# Dictionary (Hash Table)
###########################################################################
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict_keys = dict.keys()             # of type dict_keys
dict_values = dict.values()         # of type dict_types
# the two above types do not support indexing; but are iterable

del dict['Name']                    # remove entry with key 'Name'
dict.clear()                        # remove all entries in dict (outputs is an empty dict)
del dict                            # delete entire dictionary

# Keys must be immutable. Which means you can use strings, numbers or tuples as dictionary keys
#  but something like ['key'] is not allowed.

###########################################################################
# Set
###########################################################################
# A set is created by using the set() function or placing all the elements within a pair of curly braces.
Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
Months = {"Jan", "Feb", "Mar"}

# sets are not ordered and do not support indexing
# still we can iterate through the elements:
for d in Days:
    print(d)

Days.discard("Sun")                     # removing Item from a Set

DaysA = {"Mon", "Tue", "Wed"}
DaysB = {"Wed", "Thu", "Fri", "Sat", "Sun"}
AllDays = DaysA | DaysB                 # union of sets
SomeDays = DaysA & DaysB                # intersection
DifDays = DaysA - DaysB                 # difference

# compare sets
DaysA = {"Mon", "Tue", "Wed"}
DaysB = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)



print()
