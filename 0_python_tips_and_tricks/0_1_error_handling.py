import sys
# https://realpython.com/python-exceptions/#raising-an-exception
# https://docs.python.org/2/tutorial/errors.html

# A Python program terminates as soon as it encounters an error. In Python, an error can be a
#  syntax error or an exception.

# print( 0 / 0 ))               # extra parenthesis here
#   File "<stdin>", line 1
#     print( 0 / 0 ))
#                   ^
# SyntaxError: invalid syntax

# "Exception error" occurs whenever syntactically correct Python code results in an error.

# print( 0 / 0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: integer division or modulo by zero

###########################################################################
# Raise
###########################################################################
# we can use "raise" to throw an exception when a certain condition happens

# x = 10
# if x > 5:
#     raise Exception('Text to show')

# The raise statement allows the programmer to force a specified exception to occur. For example:

# raise NameError('HiThere')

###########################################################################
# Assert
###########################################################################
# The goal of using assertions is to let developers find the likely root cause of a bug more quickly.
# An assertion error should never be raised unless there’s a bug in your program.

# assert eval_condition, 'optional text to print if condition is False'
# eval_condition: 'some condition that we want to be True'

# a = 2
# assert a == 6, "expected to get a=6."

# import sys
# assert 'linux' in sys.platform, "This code runs on Linux only."


# assert throws an "AssertionError" exception and halts the program.
# what if that is not all we want?

###########################################################################
# Try and Except
###########################################################################
# The try and except block in Python is used to catch and handle exceptions.
# Python executes code following the try statement as a “normal” part of the program.
# The code that follows the except statement is the program’s response to any exceptions in the preceding try clause.
# The except clause determines how your program responds to exceptions.

# A try clause is executed up until the point where the first exception is encountered.
# Inside the except clause, or the exception handler, you determine how the program responds to the exception.
# You can anticipate multiple exceptions and differentiate how the program should respond to them.
# Avoid using bare except clauses.


print('-'*20)

# case 1: when we don't want to do anything with the exception
try:
    a = float('salam')
    print('Executing some function.')
except:
    print('cannot make the conversion.')
print('Program does not crash. So this also gets executed.')
print('-'*20)

# case 2: when we want to see the exception

try:
    a = float('salam')
    print('Executing some function.')
except Exception as e:
    print("The exception was: {}".format(e))            # The exception was: could not convert string to float: 'salam'
print('Program does not crash. So this also gets executed.')
print('-'*20)


# case 3: when we want to see the exception (similar to 2; with assert in try)
a = 2
try:
    assert a == 6, "a=6 was expected."
    print('Executing some function.')
except Exception as e:
    print(e)            # "a=6 was expected."
    print('Function was not executed because {}'.format(e))
print('Program does not crash. So this also gets executed.')
print('-'*20)

# case 4: when specifying the exception type
try:
    assert a == 6, "a=6 was expected."
    print('Executing some function.')
except AssertionError as e:
    print(e)            # "a=6 was expected."
    print('Function was not executed because {}'.format(e))
except Exception as e:  # for any other kind of error
    print(e)            # "name 'a' is not defined"
    print('Function was not executed because {}'.format(e))

print('Program does not crash. So this also gets executed.')
print('-'*20)


def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')


try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    print('Executing the else clause.')
finally:
    print('Cleaning up, irrespective of any exceptions.')

# Because the program did not run into any exceptions, the else clause was executed.

# -----------------------------SUMMARY-----------------------------------
# raise allows you to throw an exception at any time.
# assert enables you to verify if a certain condition is met and throw an exception if it isn’t.
# In the try clause, all statements are executed until an exception is encountered.
# except is used to catch and handle the exception(s) that are encountered in the try clause.
# else lets you code sections that should run only when no exceptions are encountered in the try clause.
# finally execute sections of code that should always run, with or without any previously encountered exceptions.
# print()

# An except clause may name multiple exceptions as a parenthesized tuple, for example:
# except (RuntimeError, TypeError, NameError):
#   pass
