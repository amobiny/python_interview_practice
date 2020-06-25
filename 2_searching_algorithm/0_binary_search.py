# In binary search we take a sorted list of elements and start looking for an element at the middle of the list.
# If the search value matches with the middle value in the list we complete the search. Otherwise we eleminate
# half of the list of elements by choosing whether to procees with the right or left half of the list depending
# on the value of the item searched. This is possible as the list is sorted and it is much quicker than linear
# search. Here we divide the given list and conquer by choosing the proper half of the list. We repeat this
# approach till we find the element or conclude about it's absence in the list.


# https://www.geeksforgeeks.org/binary-search/
# https://www.tutorialspoint.com/python_data_structure/python_divide_and_conquer.htm
# https://www.tutorialspoint.com/python_data_structure/python_recursion.htm

# (iterative)
def binary_search_1(arr, val):
    length = len(arr)
    start_idx = 0
    end_idx = length - 1

    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2
        if arr[mid_idx] == val:
            return mid_idx
        elif arr[mid_idx] < val:
            start_idx = mid_idx + 1
        elif arr[mid_idx] > val:
            end_idx = mid_idx - 1

    if start_idx > end_idx:
        return None


# (recursion)
def binary_search_2(arr, start_idx, end_idx, val):
    if end_idx >= start_idx:                            # equal sign is very important
        mid_idx = (start_idx + end_idx) // 2
        if arr[mid_idx] == val:
            return mid_idx
        elif arr[mid_idx] > val:
            return binary_search_2(arr, start_idx, mid_idx-1, val)
        elif arr[mid_idx] < val:
            return binary_search_2(arr, mid_idx+1, end_idx, val)
    else:
        return None


my_list = [2, 4, 64, 67, 88]
value = 88
print(binary_search_1(my_list, val=value))
print(binary_search_2(my_list, 0, len(my_list), val=value))
