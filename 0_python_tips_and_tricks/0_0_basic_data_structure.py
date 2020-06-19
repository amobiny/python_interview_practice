###########################################################################
# Mutable vs. Immutable Python objects
###########################################################################

# mutable objects: list, dictionary, set

mutable_list = [1, 2, 3]
mutable_list[-1] = 4

# immutable objects: tuple, string, integer, boolean, float, frozenset
frozen_set = frozenset([1, 2, 3])

# mutable object within an immutable object
t = (1, [1, 2, 3], 'word')
t[1][2] = 4

# this shows that if the tuple is immutable, that does not
# guarantee that the object referenced by the tuple is immutable too.

###########################################################################
# Type
###########################################################################
type(2) == int              # type(var) returns the type of the var; int, str, or float
type(2.453) == float
type('hola') == str

###########################################################################
# Integer operations
###########################################################################

a = 2 ** 3              # 8
b = 2 // 3              # floor(2 / 3) = 0
c = 2 / 3               # 0.666666
d = 13 % 5              # 3 (remainder)

for a in range(1, 10, 2):       # start:1, stop:10, step_size
    print('a = {}'.format(a))   # prints 1, 3, 5, 7, 9

###########################################################################
# String operations
###########################################################################
sample_string = "Aryan loves Peggy and Hannah"
list_of_words = sample_string.split()           # splits the words (separated by space)
lower_case = sample_string.lower()              # lower case for all characters

print()

###########################################################################
# Lists
###########################################################################

list1 = ['physics', 'chemistry', 'Math', 'Programming']
list2 = [1, 12, 3, 7]

del list1[2]                        # delete list elements
list2 = list2 + list2               # concatenation
list1.append('asal')                # appending
list3 = ['Hi!'] * 4                 # repetition
TorF = 3 in [1, 2, 3]	            # membership
list2.sort()                        # sorts "in place"

list1.sort()                        # default is to sort capitals and then smalls
# ['Math', 'Programming', 'chemistry', 'physics']

list1.sort(key=str.lower)           # sorts irrespective of capital and small letters
# ['chemistry', 'Math', 'physics', 'Programming']

list4 = [2, 4, 7, 11]
a = list4.pop()                     # removes the last element from list4 and assign it to a    list4 = [2, 4, 7]
b = list4.pop(2)                    # removes the third element from list4 and assign it to b   list4 = [2, 4]
list4.append(13)                    # appends 13 to the list                                    list4 = [2, 4, 13]
list4.insert(2, 14)                 # inserts 14 as the element with index2                     list4 = [2, 4, 14, 13]
list4.remove(2)                     # removes the value=2 from the list                         list4 = [4, 14, 13]
list4.remove(list4[2])              # removes the third element                                 list4 = [4, 14]
list4.reverse()                     # reverses the list                                         list4 = [14, 4]
list4 = list4[::-1]                 # reverse again                                             list4 = [4, 14]
list4.extend([7, 4])                # extends it (append would make it [4, 14, [7, 4]])         list4 = [4, 14, 7, 4]
list4.count(4)                      # repetitions of 4 in the list                              2
list4.index(14)                     # returns the index of element with value 14                1


###########################################################################
# Tuples
###########################################################################
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
tup3 = 3, 7, 12
tup_singular = (50,)                # that comma is important

tup4 = tup1 + tup2                  # concatenation
del tup3                            # delete a whole tuple
tup5 = ('Hi!',) * 4                 # repetition
TrueOrFalse = 3 in (1, 2, 3)	    # membership


###########################################################################
# Dictionary (Hash Table)
###########################################################################
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict_keys = dict.keys()             # of type dict_keys(['Name', 'Age', 'Class'])
dict_values = dict.values()         # of type dict_values(['Zara', 7, 'First'])
dict_items = dict.items()           # of type of dict_items([(Name', 'Zara'), ('Age', 7), ('Class', 'First')])

# the above types do not support indexing; but are iterable
for key, value in dict.items():
    pass

for key in dict:
    pass

for key in dict.keys():
    pass

for value in dict.values():
    pass

del dict['Name']                    # remove entry with key 'Name'
dict.clear()                        # remove all entries in dict (outputs is an empty dict)
del dict                            # delete entire dictionary

# Keys must be immutable. Which means you can use strings, numbers or tuples as dictionary keys
#  but something like ['key'] is not allowed.

dict2 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict2['level'] = 3                              # adding new key-value
level_val = dict2.pop('level')                  # removes the key-value from the dictionary and level_val=3
dict2.update({'level': 4, 'Name': 'Asghar'})    # to update and add multiple elements
                                                # {'Age': 7, 'Class': 'First', 'Name': 'Asghar', 'level': 4}

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


###########################################################################
# Data Comprehension
###########################################################################
Name = ['Aryan', 'Pegah', 'Hannah']
Family = ['Mobiny', 'Chavoshi', 'Mobiny']

my_dict = {n: m for n, m in zip(Name, Family)}
my_list = [n for n in Name]
my_set = {n for n in Family}
my_gen = (n for n in Name)          # this doesn't create a tuple; generates a generator (iterable)
print()
