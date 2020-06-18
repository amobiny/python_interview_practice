# https://pyformat.info/

print('My name is {0}, and I\'m {1} years old'.format('Aryan', 32))

# specify the minimum number of characters occupied
print('My name is {0:12}, and I\'m {1} years old'.format('Aryan', 32))

# right (>), left (<) and center(^) align
print('My name is {0:>13}, and I\'m a {1:^12} years old {2:<12}.'.format('Aryan', 32, 'Scientist'))

# truncate to specific number of characters
print('{:.5}'.format('xylophone'))
# xylop

# total of 6 characters with 2 after the decimal points (f specifies the float; use d for integer and s for string)
print('{0:6.4f}'.format(3.141592653589793))

# or only mention the number of decimal points
print('{0:.4f}'.format(3.141592653589793))

