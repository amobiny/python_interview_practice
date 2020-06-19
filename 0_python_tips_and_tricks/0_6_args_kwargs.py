# unpacking operators (* and **)

my_list = [1, 2, 3]
print(my_list)
# [1, 2, 3]
print(*my_list)
# 1 2 3
# Here, the * operator tells print() to unpack the list first.
# In this case, the output is no longer the list itself, but rather the content of the list.
def my_sum(a, b, c):
    print(a + b + c)

my_list = [1, 2, 3]
my_sum(*my_list)
# 6

def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum(*list1, *list2, *list3))
# 45
# If you run this example, all three lists are unpacked.

my_list = [1, 2, 3, 4, 5, 6]

a, *b, c = my_list

print(a)
print(b)
print(c)
# 1
# [2, 3, 4, 5]
# 6

my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list)
# [1, 2, 3, 4, 5, 6]

my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)
# {'A': 1, 'B': 2, 'C': 3, 'D': 4}

# Remember that the * operator works on any iterable object. It can also be used to unpack a string:
a = [*"RealPython"]
print(a)
# ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n']


# *args and **kwargs allow you to pass multiple arguments (args) or keyword arguments (kwargs) to a function.

def my_sum1(a, b):
    return a + b

# This function is limited to only two arguments. What if you need to sum a varying number of arguments,
#  where the specific number of arguments passed is only determined at runtime?

#approach#1:
def my_sum2(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3]
print(my_sum2(list_of_integers))


#approach#2:
def my_sum3(*args):
    result = 0                                  # args is the tuple (1, 2, 3)
    for arg in args:
        result += arg
    return result

print(my_sum3(1, 2, 3))
# no longer passing a list to my_sum(). Just passing three different positional arguments.
# * is the unpacking operator

# we could also do
numbers = (1, 2, 3)
print(my_sum3(numbers))
# note that we have to feed the unpacked version to the function
# because if we do not unpack numbers, args will be ((1, 2, 3), )

def concatenate(**kwargs):
    result = ""                             # kwargs is the dictionary {a:"Python", b:"Is", c:"Great"}
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Python ", b="Is ", c="Great"))

# we could also do
info = {'a': "Python ", 'b': "Is ", 'c': "Great"}
print(concatenate(**info))

# this will not be printed correctly; because dictionary is not an ordered object.


