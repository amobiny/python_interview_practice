# https://www.geeksforgeeks.org/ugly-numbers/


###########################################################################
# Solution #1: the inefficient one
###########################################################################

# This function divides a by greatest
# divisible power of b
def maxDivide(a, b):
    while a % b == 0:
        a = a / b
    return a


# Function to check if a number
# is ugly or not
def isUgly(no):
    no = maxDivide(no, 2)
    no = maxDivide(no, 3)
    no = maxDivide(no, 5)
    return 1 if no == 1 else 0


# Function to get the nth ugly number
def getNthUglyNo(n):
    i = 1
    count = 1  # ugly number count

    # Check for all integers untill
    # ugly count becomes n
    while n > count:
        i += 1
        if isUgly(i):
            count += 1
    return i


# Driver code to test above functions
no = getNthUglyNo(150)
print("150th ugly no. is ", no)

# This method is not time efficient as it checks for all integers until ugly number count becomes n,
# but space complexity of this method is O(1)

###########################################################################
# Solution #2: the inefficient one
###########################################################################

def getNthUglyNo_2(n):
    ugly = [0] * n  # To store ugly numbers

    # 1 is the first ugly number
    ugly[0] = 1

    # i2, i3, i5 will indicate indices for 2,3,5 respectively
    i2 = i3 = i5 = 0

    # set initial multiple value
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    # start loop to find value from ugly[1] to ugly[n]
    for l in range(1, n):

        # choose the min value of all available multiples
        ugly[l] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)

        # increment the value of index accordingly
        if ugly[l] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2

        if ugly[l] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3

        if ugly[l] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5

    # return ugly[n] value
    return ugly[-1]


# Driver code to test above functions
no = getNthUglyNo_2(150)
print("150th ugly no. is ", no)


# Time Complexity: O(n)
# Auxiliary Space: O(n)

