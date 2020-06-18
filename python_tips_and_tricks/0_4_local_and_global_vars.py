
x = 5       # this is a global variable


def example_func1():
    print(x)            # can print it
    print(x + 5)        # can print this too
    # x += 5            # but cannot change the global variable inside another function


# this means that we can access the global variable within a function, but cannot change it
example_func1()
print('-'*20)


def example_func2():
    x = 10              # this creates a new local variable whose id is different from the global x
    print('inside: {}, with ID: {}'.format(x, id(x)))   # *** local variable has priority ***


example_func2()
print('outside: {}, with ID: {}'.format(x, id(x)))
# inside: 10, with ID: 10919616
# outside: 5, with ID: 10919456
print('-'*20)


# def example_func3():
#     print('Global: {}, with ID: {}'.format(x, id(x)))
#     x = 10              # this creates a new local variable whose id is different from the global x
#     print('Local: {}, with ID: {}'.format(x, id(x)))
#
#
# example_func3()
# running this function returns error; because Python does not allow to have a single variable as both
# global and local "in a single scope". A variable can't be both local and global inside a function.


# To tell Python, that we want to use the global variable, we have to explicitly state this
def example_func4():
    global x            # to specify that we want to use the global one
    print('Global: {}, with ID: {}'.format(x, id(x)))
    x = 10              # this modifies the global x (its value and ID)
    print('Local: {}, with ID: {}'.format(x, id(x)))


example_func4()
print('outside: {}, with ID: {}'.format(x, id(x)))
# Global: 5, with ID: 10919456
# Local: 10, with ID: 10919616
# outside: 10, with ID: 10919616


def foo(x, y):
    global a
    a = 42
    x, y = y, x
    b = 33
    b = 17
    c = 100
    print(a, b, x, y)


a, b, x, y = 1, 15, 3, 4
foo(17, 4)
print(a, b, x, y)

# 42 17 4 17
# 42 15 3 4


# Nested functions

def f():
    city = "Hamburg"

    def g():
        global city
        city = "Geneva"

    print("Before calling g: " + city)                              # *** local variable has priority ***
    print("Calling g now:")
    g()
    print("After calling g: " + city)                               # *** local variable has priority ***


f()
print("Value of city in main: " + city)

# Before calling g: Hamburg
# Calling g now:
# After calling g: Hamburg
# Value of city in main: Geneva




