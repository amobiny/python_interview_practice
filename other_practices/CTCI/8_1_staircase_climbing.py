num_stairs = 20

###########################################################################
# Brute Force
###########################################################################


def count_ways(n):
    if n < 0:
        return 0
    if n <= 3:
        return n
    return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)


print(count_ways(num_stairs))


# time complexity: O(3^n)

###########################################################################
# DP_1
###########################################################################

def count_ways_dp1(n, memo):
    if n < 0:
        return 0
    if n <= 3:
        return n
    memo[n] = count_ways_dp1(n-1, memo) + count_ways_dp1(n-2, memo) + count_ways_dp1(n-3, memo)
    return memo[n]


memo = [0] * (num_stairs + 1)     # first element: total of 0 stairs
memo[1], memo[2], memo[3] = 1, 2, 3
print(count_ways_dp1(num_stairs, memo))


###########################################################################
# DP_2
###########################################################################

def count_ways_dp2(n):
    if n < 0:
        return 0
    if n <= 3:
        return n
    count = [1] * n
    count[1], count[2] = 2, 3
    for num_stairs in range(3, n):
        count[num_stairs] = count[num_stairs-1] + count[num_stairs-2] + count[num_stairs-3]
    return count[-1]


print(count_ways_dp2(num_stairs))



