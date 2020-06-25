# https://www.geeksforgeeks.org/cutting-a-rod-dp-13/

###########################################################################
# Solution #1: recursive
###########################################################################


def cut_rod(price, n):
    if n == 0:
        return 0

    rod = []
    for i in range(n):
        rod.append(price[i] + cut_rod(price, n-i-1))
    return max(rod)


# Driver code
arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is", cut_rod(arr, size))


###########################################################################
# Solution #2: DP
###########################################################################

def cut_rod(price, n):
    if n == 0:
        return 0
    val = [0] * (n+1)               # the ith element of this vector shows the maximum we can get for a rod of length i
    for i in range(1, n+1):         # different lengths of rods
        for j in range(i):          # different cuts of the rod
            val[i] = max(val[i], price[j] + val[i-j-1])
    return val[n]


# Driver code
arr = [1, 5, 8, 9, 10, 17, 17, 20]
rod_length = len(arr)
print("Maximum Obtainable Value is", cut_rod(arr, rod_length))
