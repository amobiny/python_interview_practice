# https://www.geeksforgeeks.org/bubble-sort/
# https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

my_arr = [7, 3, 5, 1, 0, 4]
print(bubble_sort(my_arr))


# The above function always runs O(n^2) time even if the array is sorted.
# It can be optimized by stopping the algorithm if inner loop didn’t cause any swap.

# An optimized version of Bubble Sort
def bubble_sort_2(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already
        #  in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # IF no two elements were swapped
        # by inner loop, then break
        if swapped is False:
            break
    return arr


print(bubble_sort_2(my_arr))
