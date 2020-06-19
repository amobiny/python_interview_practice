# a generator does not create the actual object (e.g. a list) and does not store it on memory; just creates an stream

gen_1 = range(5)

xyz_list = [i**2 for i in range(100000)]    # this is a simple list

###########################################################################
# generator comprehension
###########################################################################
xyz_gen = (i**2 for i in range(100000))     # this is a generator; just a stream
print(xyz_gen)                              # <generator object <genexpr> at 0x7fedbabb8af0>

# let's see how much space they take on memory
import sys
print(sys.getsizeof(xyz_list))          # 824464
print(sys.getsizeof(xyz_gen))           # 88

# let's compare their speed
import cProfile
cProfile.run('sum(xyz_list)')           # 4 function calls in 0.001 seconds
cProfile.run('sum(xyz_gen)')            # 100005 function calls in 0.029 seconds

xyz_to_list = list(xyz_gen)                 # convert to a list

###########################################################################
# generator functions
###########################################################################
# they do not return things; they "yield"
# they can be iterators; in case they have multiple yields (or yield in a loop)
# they are able to keep their state; meaning that every time we iterate over a generator function,
# it executes codes until the first yield, yields the proper value and stays there (at that yield).


def simple_gen():
    yield 'oh'
    yield 'my'
    yield 'lord!'


gen_2 = simple_gen()
type(gen_2)             # this is a generator; <generator object <genexpr> at 0x7f76069ec360>

# now if we run next on it, it runs until the first yield and stop there
print(next(gen_2))      # 'oh'
print(next(gen_2))      # 'my'
print(next(gen_2))      # 'lord!'


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


gen_3 = infinite_sequence()
print(next(gen_3))      # 0
print(next(gen_3))      # 1
print(next(gen_3))      # 2

# we could similarly do (this loop ):
# for i in gen_3:
#     print(i)


def infinite_sequence_2():
    num = 0
    while True:
        yield num
        num += 1
        yield "This is the second yield"


gen_4 = infinite_sequence_2()
print(next(gen_4))      # 0
print(next(gen_4))      # This is the second yield
print(next(gen_4))      # 1
print(next(gen_4))      # This is the second yield
print(next(gen_4))      # 2


def finite_sequence():
    num = [0, 1, 2]
    for n in num:
        yield n


gen_5 = finite_sequence()
print(next(gen_5))      # 0
print(next(gen_5))      # 1
print(next(gen_5))      # 2
print(next(gen_5))      # StopIteration

print()


