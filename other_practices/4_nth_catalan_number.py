# https://www.geeksforgeeks.org/program-nth-catalan-number/
# The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …
import time


###########################################################################
# Solution #1: recursive
###########################################################################

def catalan(n):
    # Base Case
    if n <= 1:
        return 1

        # Catalan(n) is the sum of catalan(i)*catalan(n-i-1)
    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n - i - 1)

    return res

start_time = time.time()
# Driver Program to test above function
for c in range(10):
    print(catalan(c))
print('Run Time: {}'.format(time.time() - start_time))
# Run Time: 0.0022079944610595703


###########################################################################
# Solution #2: DP
###########################################################################


def catalan_dp1(n, lookup):
    if n <= 1:
        return 1
    if lookup[n] == 0:
        for i in range(n):
            lookup[n] += catalan_dp1(i, lookup) * catalan_dp1(n-1-i, lookup)
    return lookup[n]

max_n = 10
start_time = time.time()

lookup = [0] * max_n
lookup[0], lookup[1] = 1, 1
for c in range(max_n):
    print(catalan_dp1(c, lookup))
print('Run Time: {}'.format(time.time() - start_time))
# Run Time: 3.838539123535156e-05


###########################################################################
# Solution #3: DP
###########################################################################

def catalan_dp2(n):
    if n <= 1:
        return 1

    # Table to store results of sub-problems
    catalan = [0 for i in range(n + 1)]

    # Initialize first two values in table
    catalan[0] = 1
    catalan[1] = 1

    # Fill entries in catalan[] using recursive formula
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j] * catalan[i - j - 1]

            # Return last entry
    return catalan[n]


max_n = 10
start_time = time.time()
for c in range(max_n):
    print(catalan_dp2(c))

print('Run Time: {}'.format(time.time() - start_time))
# Run Time: 5.364418029785156e-05





