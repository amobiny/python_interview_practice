###########################################################################
# How to use sys.argv in Python
###########################################################################
# in command line: python sample_code.py 'aryan' 43
import sys
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))
print("My name is: ", str(sys.argv[1]))
print("and I'm {} years old".format(str(sys.argv[2])))
