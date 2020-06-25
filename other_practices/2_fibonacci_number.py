# https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/
# gives the nth number in the sequence of Fibonacci numbers
# form a sequence such that each number is the sum of the two preceding ones.
# fib(0)=0, fib(1)=1, fib(2)=1, fib(3)=2, fib(4)=3, fib(5)=5, fib(6)=8, fib(7)=13, fib(8)=21, ...


# recursive solution
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


print(fib(2))

# Time complexity: O(2^n); (Think of the recursive calls as a tree)


# DP1:
# Python program for Memoized version of nth Fibonacci number
# Function to calculate nth Fibonacci number
def fib_dp1(n, lookup):
    # Base case
    if n == 0 or n == 1:
        lookup[n] = n

    # If the value is not calculated previously then calculate it
    if lookup[n] is None:
        lookup[n] = fib_dp1(n - 1, lookup) + fib_dp1(n - 2, lookup)

    # return the value corresponding to that value of n
    return lookup[n]


# end of function

# Driver program to test the above function
n = 34
# Declaration of lookup table
# Handles till n = 100
lookup = [None] * 101
result = fib_dp1(n, lookup)
print("Fibonacci Number is ", result)

# Time Complexity:O(n)
# Extra Space: O(n) if we consider the function call stack size, otherwise O(1).

# DP2:
# Python program Tabulated (bottom up; because we compute the values for smaller numbers first) version
# this is the space-optimized method

def fib_dp2(n):
    # array declaration
    memo = [0] * (n + 1)

    # base case assignment
    memo[1] = 1

    # calculating the fibonacci and storing the values
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


# Driver program to test the above function
n = 9
result = fib_dp2(n)
print("Fibonacci number is ", result)


# we can also get rid of the "memo" array to save some space:

def fib_dp3(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return c


# Driver program to test the above function
n = 9
result = fib_dp2(n)
print("Fibonacci number is ", result)

# Time Complexity:O(n)
# Extra Space: O(1)
