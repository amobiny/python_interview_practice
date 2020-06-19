###########################################################################
# enumerate
###########################################################################
list1 = ['physics', 'chemistry', 1997, 2000]
for idx, element in enumerate(list1):
    pass

# can also be used for dictionaries
my_dict = {'name': 'aryan', 'age': 32, 'occupation': 'unemployed'}

my_list = [(i, j) for i, j in enumerate(my_dict)]
# [(0, 'name'), (1, 'occupation'), (2, 'age')]

mylist = ['aryan', 'pegah', 'hannah', 'jana']
mydict = dict(enumerate(mylist))
# {0: 'aryan', 1: 'pegah', 2: 'hannah', 3: 'jana'}


###########################################################################
# zip
###########################################################################
# iterates through multiple iterators
# zip(x, y) --> generates a zip object <zip at 0A134877492>

x = [1, 3, 5, 7, 9]
y = [2, 4, 6, 8, 10]
for i, j in zip(x, y):
    print(i, j)
# 1 2
# 3 4
# 5 6
# 7 8
# 9 10

for i in zip(x, y):
    print(i)
# (1, 2)
# (3, 4)
# (5, 6)
# (7, 8)
# (9, 10)

for i in zip(x, y):
    print(*i)
# 1 2
# 3 4
# 5 6
# 7 8
# 9 10
###########################################################################
# lambda
###########################################################################
# function with no name; not good for multi-line functions


def f1(x):
    x = 3 * x + 1
    return x


f2 = lambda x: 3 * x + 1

print(f1(2))
print(f2(2))

f3 = lambda x, y: 3 * x + 2 * y
print(f3(2, 4))


def build_quad_func(a, b, c):
    return lambda x: a * x * x + b *x + c


f = build_quad_func(2, 3, 4)
print(f(0))


###########################################################################
# map
###########################################################################
# map(f, a) applies the function f to all elements of a (any iterable)

f_area = lambda r: 3.14 * r * r
radius = [2, 3, 7]
all_areas = list(map(f_area, radius))
print(all_areas)

###########################################################################
# filter
###########################################################################
# filter(f, a) returns only the elements of a (iterable) for which the function f is True

data = [1, 5, 3, 2, 4]
new_data = list(filter(lambda x: x > 3, data))
print(new_data)

# write an script that takes the following list and removes the empty elements
countries = ['Iran', '', 'Argentina', '', 'Madagascar']

new_countries = list(filter(lambda x: x is not '', countries))
# this would work too: new_countries = list(filter(None, countries))
print(new_countries)


